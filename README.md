# 트윙클 스타 스프라이츠 세가새턴 한글패치 베타

버전: **v0.1.0-beta.1** · 대상: 일본판 **Disc 1 (Game Disc), T-37301G V1.003**

현재 R3.1 작업본을 그대로 공개하는 테스트용 베타입니다. 완성판이나 전체 플레이 검증 완료판이 아닙니다. Disc 2 오마케는 대상이 아닙니다.

## xdelta 배포 추가 — 2026-10-11

기존 R3.1 게임 데이터는 그대로이며, Python 없이 외부 xdelta 패처로 적용하는 두 형식을 추가했습니다. ZIP 안의 README를 먼저 읽어 주세요. 자체 EXE는 포함하지 않습니다.

| 파일 | 대상 | 결과 |
|---|---|---|
| [BIN용 xdelta ZIP](https://github.com/kirby-gpt/twinkle-star-sprites-saturn-korean/releases/download/v0.1.0-beta.1/TSS_Saturn_KO_v0.1.0-beta.1_BIN_xdelta.zip) | 분할 원본 Track 01 BIN | 한글 Track 01; 다른 트랙과 CUE 유지 |
| [CHD용 xdelta ZIP](https://github.com/kirby-gpt/twinkle-star-sprites-saturn-korean/releases/download/v0.1.0-beta.1/TSS_Saturn_KO_v0.1.0-beta.1_CHD_xdelta.zip) | 지정 SHA-256의 원본 CHD | 한글 CHD 한 파일 |

CHD는 아무 원본 CHD에나 적용되지 않습니다. 해시가 다르면 BIN용을 적용한 뒤 CUE 전체를 CHD로 변환하세요. ES-DE에는 완성된 CHD 하나를 넣고 CHD 지원 에뮬레이터를 선택하면 됩니다. 두 형식의 적용 결과와 26개 트랙 보존을 검사했으며, ES-DE 실행 검증은 별도로 하지 않았습니다. 기존 Python 패키지도 대안으로 유지합니다.

## 기존 Python 방식 다운로드

[GitHub 베타 다운로드](https://github.com/kirby-gpt/twinkle-star-sprites-saturn-korean/releases/tag/v0.1.0-beta.1)에서 `TSS_Saturn_KO_v0.1.0-beta.1_patch.zip`을 받으세요. 패치에는 ROM, BIOS, 에뮬레이터가 포함되지 않습니다.

## 현재 상태와 알려진 문제

- 메뉴, 타이틀, 대사 및 여러 이미지 텍스트의 한글화 작업을 반영했습니다. 미번역·오역·줄바꿈 문제가 남아 있을 수 있습니다.
- 캐릭터 능력치 표 27종의 글자 공간을 넓히고 최대 11픽셀 글자를 적용했습니다. 적용 27/27(100%)이며, 이 수치는 게임 전체 완성률이 아닙니다.
- **점수 뒤의 ‘점’ 글자가 뭉개져 기호처럼 보이는 문제가 있습니다. 이번 베타에서는 수정되지 않았습니다.**
- 작은 글꼴, 로딩 문구, 설명문 등의 가독성과 배경 복원에 추가 점검이 필요합니다. 튜토리얼 대사가 말풍선 밖으로 나가는 화면도 확인됐습니다.
- **아케이드 모드: 사용자 검수 완료(2026-10-07 사용자 확인).**
- 다른 모드·모든 캐릭터·엔딩 전체 검증은 미완료이며 전체 완성률은 산정하지 않았습니다. 아케이드 모드 검수 완료가 알려진 글꼴 문제의 해결을 의미하지는 않습니다.
- Yabause 0.9.15에서 부팅과 일부 화면은 확인했지만, 전 구간 정상 동작을 보장하는 검증은 하지 못했습니다. 기기·에뮬레이터별 호환성 제보를 받습니다.

## 기존 Python 방식 준비물과 원본 정보

- 압축을 해제한 일본판 Disc 1 원본 CUE와 BIN 26개. 동일한 데이터를 합친 단일 BIN도 지원합니다.
- Python 3.10 이상(Windows에서는 tkinter와 Python Launcher를 포함한 일반 설치 권장).
- 출력용 여유 공간 약 1GB 이상. 원본은 덮어쓰지 않습니다.



원본 Track 01의 SHA-256:

```text
5d74b494f33511e0f81f45e75df4196ac25c86c5e22409c76991cb621a99583f
```

모든 트랙의 크기와 해시는 `patch_manifest.json`에 있습니다. 이미 패치된 이미지, 다른 리비전, 일반 ISO, CHD에는 직접 적용하지 않습니다.

## 기존 Python 방식 패치 사용법 — Windows

1. 패치 ZIP을 새 폴더에 모두 압축 해제합니다.
2. 원본 게임 압축 파일도 해제합니다. 원본 CUE와 26개 BIN 파일은 같은 폴더에 둡니다.
3. 패치 폴더의 `Patch_Windows.bat`을 실행합니다.
4. 파일 선택 창에서 **원본 Disc 1의 CUE 파일**을 선택합니다.
5. 원본 해시 검사와 패치를 기다립니다. `SUCCESS`가 표시되면 완료입니다.
6. 원본 폴더에 새로 생긴 `TSS_KO_v0.1.0-beta.1` 폴더에서 **한글판 CUE**를 에뮬레이터의 CD 이미지 열기로 선택합니다. 출력 BIN도 같은 폴더에 있어야 합니다.

출력은 단일 BIN+CUE이며 원본의 데이터 트랙 2개와 오디오 트랙 24개를 유지합니다. 확장자를 ISO로 바꾸지 마세요.

명령행 사용:

```text
python apply_patch.py "D:\Games\Twinkle Star Sprites (Japan) (Disc 1) (Game Disc).cue" --output "D:\Games\TSS-KO-beta"
```

`--output`에는 아직 존재하지 않는 새 폴더를 지정합니다. 파일 선택 창을 쓰지 않으면 tkinter가 없어도 됩니다.

## 오류가 날 때

- `Python` 또는 `py`를 찾을 수 없음: Python 3.10 이상을 설치하고 다시 실행합니다.
- `SHA-256 mismatch`: 다른 원본·손상된 파일·이미 패치된 이미지입니다. 일치하는 원본을 사용하세요. 검사를 무시하는 옵션은 없습니다.
- 출력 폴더가 이미 있음: 기존 파일을 보존하고 다른 새 폴더를 `--output`으로 지정하세요.
- ZIP/7z가 선택되지 않음: 원본 압축을 먼저 해제하고 CUE를 선택하세요.
- 실행 시 음악 누락 또는 부팅 실패: BIN 대신 CUE를 열었는지, BIN을 이동하지 않았는지 확인하세요.

참고 키 설정: 방향키, Z/X/C/A/S/D = A/B/C/Z/X/Y, Q/E = L/R, Space = Start. 에뮬레이터에서 직접 설정해야 하며 패처는 설정을 변경하지 않습니다.

## 제보

버전, 기기, 에뮬레이터 이름/버전, 모드·캐릭터·스테이지, 재현 순서와 스크린샷을 함께 알려 주세요. 원본 ROM이나 BIOS를 이슈에 첨부하지 마세요.

## 글꼴과 권리 표시

Pretendard Regular / Black / SemiBold 1.3.9를 사용했습니다. 글꼴 원본명·버전·SHA-256·저작권은 `font_manifest.json`, SIL OFL 1.1 전문은 `FONT-LICENSE.txt`에 포함했습니다. Galmuri/Dalmoori는 사용하지 않았습니다.

게임과 원본 그래픽·음악 등의 권리는 각 권리자에게 있습니다. 이 프로젝트는 비공식 한글패치입니다.
