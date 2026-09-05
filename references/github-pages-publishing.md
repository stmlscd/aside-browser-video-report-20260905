# GitHub Pages 안전 게시 절차

이 문서는 사용자가 실제 게시를 명시적으로 요청한 경우에만 적용한다.

## 1. 대상 저장소 확인

1. 사용자 지정 저장소·Pages URL을 우선한다.
2. 기존 로컬 clone을 찾고 `remote -v`, 현재 branch, `status --short`, 최근 log를 확인한다.
3. 저장소의 `AGENTS.md`를 끝까지 읽는다.
4. 후보가 여러 개면 remote와 최신 commit으로 canonical clone을 식별한다.
5. 작업 트리에 관련 없는 변경이 있으면 건드리지 않는다. 새 clone 또는 안전한 별도 작업 경로를 사용한다.

## 2. 최신 상태 동기화

- `git pull --ff-only`로 최신 상태를 확인한다.
- 비 fast-forward, 충돌, 인증 오류가 발생하면 강제 push·reset을 하지 않는다.
- 네트워크나 인증에 필요한 승인만 요청하고, 자격 증명을 새 파일에 저장하지 않는다.

## 3. 게시 경로

저장소 관례가 있으면 그대로 따른다. 일반적인 `docs/` Pages 저장소는 다음을 권장한다.

```text
docs/<report-slug>.html
docs/assets/<report-slug>/...
```

- HTML의 자산 경로를 게시 위치 기준 상대경로로 조정한다.
- 기존 관례가 있을 때만 `reports/`에 byte-identical 보존본을 둔다.
- 저장소 인덱스와 README가 보고서 카탈로그 역할을 한다면 새 링크와 한 문단 설명을 추가한다.
- 기존 파일명과 충돌하면 새 slug를 선택한다. 덮어쓰지 않는다.

## 4. 커밋 전 검증

- 게시 위치를 루트로 로컬 서버를 열고 실제 Pages 경로와 같은 URL로 렌더링한다.
- HTML·모든 이미지·필수 자산이 200인지 확인한다.
- `git diff --check`, `git diff --stat`, `git status --short`를 확인한다.
- `git add`에는 의도한 파일만 명시한다.
- 커밋 메시지는 보고서 주제와 게시 사실이 드러나게 쓴다.

## 5. Push와 Pages 확인

1. 지정 branch로 push한다.
2. Pages workflow를 확인하고 완료까지 기다린다. 반복 조회는 짧은 상한을 둔다.
3. workflow가 실패하면 로그를 읽고 현재 변경 범위 안에서 해결 가능한 문제만 수정한다.
4. 성공 후 공개 HTML과 자산을 HTTP 200으로 확인한다.
5. 공개 페이지를 브라우저에서 열어 제목, 이미지 자연 크기, 수평 오버플로, 콘솔 오류를 확인한다.

## 6. 게시 기록

`06_publish/06_publish_record.md`에 다음을 남긴다.

- 공개 URL과 저장소 URL
- branch, 전체 commit SHA, commit message
- Pages workflow ID와 결과
- 저장된 repo 경로
- HTML·자산의 HTTP 상태와 크기
- 게시 파일 SHA-256
- 게시 후 작업 트리 상태

## 중지 조건

- 대상 저장소를 확정할 수 없음
- 사용자가 게시를 승인하지 않음
- 인증이 없거나 다른 계정만 사용 가능
- 충돌 또는 보호 branch 정책으로 안전한 push 불가
- 기존 자료를 덮어써야만 하는 경로

이 경우 로컬 HTML과 게시 준비물까지만 완료하고, 정확한 차단 원인과 필요한 사용자 결정을 보고한다.
