"""TSS KO beta patcher. Python 3.10+, standard library only.

Patch format: gzip-compressed XOR bytes for Track 01. All inputs and outputs
are SHA-256 checked. Original images are never modified.
"""
import argparse
import gzip
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CHUNK = 1024 * 1024


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(CHUNK), b''):
            h.update(block)
    return h.hexdigest()


def source_parts(source, manifest):
    tracks = manifest['tracks']
    if source.suffix.lower() == '.bin':
        if source.stat().st_size != sum(t['size'] for t in tracks):
            raise ValueError('BIN must contain all 26 tracks. For separate tracks select the original CUE.')
        offset = 0
        result = []
        for t in tracks:
            result.append((source, offset, t))
            offset += t['size']
        return result
    if source.suffix.lower() != '.cue':
        raise ValueError('Select an extracted original .cue or a merged original .bin; not ZIP/7z/ISO/CHD.')
    text = source.read_text(encoding='utf-8-sig')
    names = re.findall(r'^\s*FILE\s+"([^"]+)"\s+BINARY\s*$', text, re.I | re.M)
    if len(names) == 1:
        return source_parts((source.parent / names[0]).resolve(), manifest)
    if len(names) != 26:
        raise ValueError('Expected 26 BINARY files in the original CUE.')
    result = []
    for name, t in zip(names, tracks):
        p = (source.parent / name).resolve()
        if p.stat().st_size != t['size']:
            raise ValueError('Incorrect track size: ' + p.name)
        result.append((p, 0, t))
    return result


def apply(source, output):
    manifest = json.loads((ROOT / 'patch_manifest.json').read_text('utf-8'))
    delta = ROOT / 'track01.xor.gz'
    if digest(delta) != manifest['delta_sha256']:
        raise ValueError('Patch data checksum mismatch. Download and extract the patch again.')
    parts = source_parts(source.resolve(), manifest)
    # Verify every source track before creating any output.
    for i, (p, offset, t) in enumerate(parts, 1):
        h = hashlib.sha256()
        with p.open('rb') as f:
            f.seek(offset)
            remaining = t['size']
            while remaining:
                block = f.read(min(CHUNK, remaining))
                if not block:
                    raise ValueError('Truncated source: ' + p.name)
                h.update(block)
                remaining -= len(block)
        if h.hexdigest() != t['sha256']:
            raise ValueError(f'Track {i:02d} SHA-256 mismatch: wrong revision, modified image, or already patched.')
        print(f'Source checked: {i}/26', flush=True)
    # New directory is mandatory; no existing files are overwritten.
    output.mkdir(parents=True, exist_ok=False)
    binary = output / manifest['output_bin']
    temporary = output / (manifest['output_bin'] + '.partial')
    out_hash = hashlib.sha256()
    try:
        with temporary.open('xb') as dst, gzip.open(delta, 'rb') as patch:
            for i, (p, offset, t) in enumerate(parts):
                with p.open('rb') as src:
                    src.seek(offset)
                    remaining = t['size']
                    while remaining:
                        block = src.read(min(CHUNK, remaining))
                        if not block:
                            raise ValueError('Source changed during patching.')
                        if i == 0:
                            mask = patch.read(len(block))
                            if len(mask) != len(block):
                                raise ValueError('Truncated patch.')
                            block = (int.from_bytes(block, 'little') ^ int.from_bytes(mask, 'little')).to_bytes(len(block), 'little')
                        dst.write(block)
                        out_hash.update(block)
                        remaining -= len(block)
                print(f'Output written: {i + 1}/26', flush=True)
            if patch.read(1):
                raise ValueError('Unexpected trailing patch bytes.')
        if out_hash.hexdigest() != manifest['output_sha256'] or digest(temporary) != manifest['output_sha256']:
            raise ValueError('Output checksum mismatch; do not use this image.')
        temporary.rename(binary)
        (output / manifest['output_cue']).write_text(manifest['cue_text'], encoding='ascii')
    except Exception:
        # Only this invocation's partial output can be removed.
        if temporary.exists():
            temporary.unlink()
        raise
    print('SUCCESS: open ' + str(output / manifest['output_cue']), flush=True)
    return binary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', nargs='?', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.source is None:
        from tkinter import Tk, filedialog
        gui = Tk()
        gui.withdraw()
        selected = filedialog.askopenfilename(title='Select original Disc 1 CUE', filetypes=[('CD image', '*.cue *.bin')])
        gui.destroy()
        if not selected:
            return
        args.source = Path(selected)
    out = args.output or args.source.resolve().parent / 'TSS_KO_v0.1.0-beta.1'
    apply(args.source, out)


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print('ERROR: ' + str(error), file=sys.stderr)
        sys.exit(1)
