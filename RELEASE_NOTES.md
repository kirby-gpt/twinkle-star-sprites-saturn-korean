## xdelta 배포 추가 — 2026-10-11

기존 R3.1 게임 데이터는 그대로이며, Python 없이 외부 xdelta 패처로 적용하는 두 형식을 추가했습니다. ZIP 안의 README를 먼저 읽어 주세요. 자체 EXE는 포함하지 않습니다.

| 파일 | 대상 | 결과 |
|---|---|---|
| [BIN용 xdelta ZIP](https://github.com/kirby-gpt/twinkle-star-sprites-saturn-korean/releases/download/v0.1.0-beta.1/TSS_Saturn_KO_v0.1.0-beta.1_BIN_xdelta.zip) | 분할 원본 Track 01 BIN | 한글 Track 01; 다른 트랙과 CUE 유지 |
| [CHD용 xdelta ZIP](https://github.com/kirby-gpt/twinkle-star-sprites-saturn-korean/releases/download/v0.1.0-beta.1/TSS_Saturn_KO_v0.1.0-beta.1_CHD_xdelta.zip) | 지정 SHA-256의 원본 CHD | 한글 CHD 한 파일 |

CHD는 아무 원본 CHD에나 적용되지 않습니다. 해시가 다르면 BIN용을 적용한 뒤 CUE 전체를 CHD로 변환하세요. ES-DE에는 완성된 CHD 하나를 넣고 CHD 지원 에뮬레이터를 선택하면 됩니다. 두 형식의 적용 결과와 26개 트랙 보존을 검사했으며, ES-DE 실행 검증은 별도로 하지 않았습니다. 기존 Python 패키지도 대안으로 유지합니다.

# v0.1.0-beta.1 — 첫 공개 베타

일본판 세가새턴 Twinkle Star Sprites Disc 1의 비공식 한글패치입니다. R3.1 작업본과 동일한 게임 데이터를 생성합니다.

- 대상: T-37301G V1.003, Disc 1. 오마케 Disc 2 제외.
- 배포 파일: `TSS_Saturn_KO_v0.1.0-beta.1_patch.zip`
- 원본은 별도 준비합니다. 패치 압축 해제 → `Patch_Windows.bat` → 원본 CUE 선택 → 생성된 한글판 CUE로 실행합니다. Python 3.10 이상 필요.
- 데이터 2개·오디오 24개 트랙을 단일 BIN+CUE로 보존합니다.
- **알려진 문제: 점수의 ‘점’ 글자 깨짐, 일부 작은 글꼴 가독성 및 대사 넘침. 이번 버전에서 해결되지 않았습니다.**
- 캐릭터 능력치 표 적용 27/27(100%). 아케이드 모드는 사용자 검수 완료(2026-10-07 확인). 전체 완성률은 미산정이며 전체 플레이 검증은 미완료입니다.

대상 원본 정보와 상세 사용법은 README를 확인해 주세요. 이 릴리스는 **Pre-release(베타)** 로 공개합니다.
