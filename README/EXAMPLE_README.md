# 클라우드 클럽 7기 스터디 템플릿 - (프로젝트형 스터디)

![image](https://github.com/user-attachments/assets/f06df1a0-be1c-4027-8403-915584833069)

## 1. Introduction

> [!NOTE]
>
> ### 스터디 소개
>
> 안녕하세요! 클라우드 클럽 7기 클둥이 여러분!
> 홈서버 프로젝트 스터디에 오신 것을 환영합니다!
> 저희 스터디는 클라우드 기술의 기반이 되는 네트워크와 인프라를
> 실습을 통해 깊이 있게 학습하는 것을 목표로 합니다.

---

<br>

### 🕑 Schedule & Members

주 1회 스터디를 진행하며 비대면 하루, 대면 하루 이렇게 진행합니다.

- 매주 월요일 저녁 (22:00~23:00) 주간회고를 짧게 가집니다.

- 격주 일요일 저녁 1회 (18:00~20:30) 서울 역삼 캠퍼스인근 스터디룸이나 카페에서 홈서버 모각코 프로젝트를 진행합니다.

- 최대 6명의 멤버를 모집합니다. **전공 무관**

<br>

### Who need this study?

> 아래 요건에 2개 이상 해당되면 홈서버 프로젝트에 합류해보세요!

- 정기적으로 오프라인에서 같이 프로젝트 개발을 통해 팀원간 지식 및 노하우를 공유하고 싶으신 분

- 홈 서버를 직접 구축해보면서 클라우드의 기반이 되는 네트워크와 인프라를 심도있게 배우고 싶은 사람

- 클라우드 개발직군과 관련성 깊은 토이 프로젝트를 진행하고 싶으신 분

- 언어 및 프레임워크 사용 경험은 있으나 기반 기술(CS)에 대한 이해가 부족한 분

- 도커, 컨테이너 개념을 포함하여 현대적인 홈 서버 구축에 필요한 기술들을 실습 위주로 역량을 키워나가고 싶은 분

<br>

---

## 2. 👽 Our Squad

<table>
  <tr>
    <td align="center"><a href="https://github.com/markson-42"><img src="https://avatars.githubusercontent.com/u/84828274?v=4" width="100px;" alt=""/><br /><sub><b>
👑스터디장</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/markson-42"><img src="https://avatars.githubusercontent.com/u/84828274?v=4" width="100px;" alt=""/><br /><sub><b>
클둥이1</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/eunah320"><img src="https://avatars.githubusercontent.com/u/84828274?v=4" width="100px;" alt=""/><br /><sub><b>
클둥이2</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/daheepk"><img src="https://avatars.githubusercontent.com/u/84828274?v=4" width="100px;" alt=""/><br /><sub><b>
클둥이3</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/ebeleey"><img src="https://avatars.githubusercontent.com/u/84828274?v=4" width="100px;" alt=""/><br /><sub><b>
클둥이4</b></sub></a><br /></td>
  </tr>
</table>

<br>

## 3. ⛳ Curriculum (Season - 1)

### Season 1 : 25.03.02 ~ 25.05.05 : 홈 서버 구축 프로젝트

| Week   | Learning Content Title      | Details of Learning Content                                                                                                                                                                                   | Completion |
| ------ | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| Week 1 | 홈 서버 기초와 우분투 설치  | - 홈 서버의 개념과 장점 이해<br>- 우분투 서버 ISO 다운로드 및 부팅 USB 생성<br>- BIOS 설정 및 우분투 서버 설치 과정 실습<br>- 초기 시스템 설정 (시간대, 언어, 키보드 레이아웃)                                | ✅         |
| Week 2 | 우분투 서버 관리와 보안     | - 사용자 계정 생성 및 권한 관리 (sudo 설정)<br>- 파일 시스템 구조 이해 및 디스크 파티셔닝<br>- UFW(Uncomplicated Firewall) 설정 및 기본 규칙 생성<br>- SSH 보안 강화 (키 기반 인증, 포트 변경, fail2ban 설치) | ✅         |
| Week 3 | 네트워크 기초와 라우터 설정 | - IP 주소, 서브넷, DHCP 개념 학습<br>- 홈 라우터 관리 인터페이스 접속 및 기본 설정<br>- 포트 포워딩 설정 (SSH, HTTP, HTTPS)<br>- 동적 DNS 서비스 설정 및 도메인 연결                                          | ✅         |
| Week 4 | 웹 서버 구축 - Apache/Nginx | - Apache와 Nginx의 차이점 및 선택 기준<br>- 선택한 웹 서버 소프트웨어 설치 및 기본 설정<br>- 가상 호스트 설정 및 간단한 웹 페이지 배포<br>- [과제1] : SSL/TLS 인증서 발급 및 HTTPS 설정                       | ❌         |
| Week 5 | 도커 기초와 컨테이너화      | - 도커 설치 및 기본 명령어 학습 (pull, run, ps, images)<br>- Dockerfile 작성 및 이미지 빌드 실습<br>- 도커 네트워크 및 볼륨 개념 이해<br>- 간단한 애플리케이션 컨테이너화 및 실행                             | ❌         |
| Week 6 | 쿠버네티스 입문             | - 쿠버네티스 아키텍처 및 주요 컴포넌트 이해<br>- minikube 설치 및 기본 사용법 학습<br>- kubectl 명령어 실습 (get, describe, apply, delete)<br>- 간단한 파드(Pod) 생성 및 관리                                 | ❌         |
| Week 7 | 쿠버네티스 클러스터 구축    | - 멀티노드 클러스터 아키텍처 설계<br>- kubeadm을 이용한 마스터 노드 초기화<br>- 워커 노드 추가 및 네트워크 플러그인 설정<br>- 기본 워크로드 배포 (Deployment, Service 생성)                                   | ❌         |
| Week 8 | 프로젝트 1차 완성 및 리뷰   | - 구축한 홈 서버 환경 최적화 (리소스 할당, 성능 튜닝)<br>- Prometheus와 Grafana를 이용한 모니터링 시스템 구축<br>- 전체 시스템 보안 점검 및 취약점 개선<br>- 프로젝트 발표 및 피드백 세션                     | ❌         |

<br>

---

## 4. GitHub Collaboration Guidelines

이 섹션에서는 프로젝트 참여자를 위한 GitHub 사용 규칙을 상세히 설명합니다. 아래 가이드라인을 따라 효율적이고 일관된 협업 환경을 만들어 나가겠습니다.

### a. 디렉토리 구조

프로젝트의 디렉토리 구조는 다음과 같이 구성됩니다:

```
CloudClub_HomeServer/
├── docs/
│   ├── setup/
│   ├── tutorials/
│   └── api/
├── src/
│   ├── backend/
│   ├── frontend/
│   └── scripts/
├── tests/
│   ├── unit/
│   └── integration/
├── config/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
├── .gitignore
├── README.md
└── LICENSE
```

> 💡 **팁**: 새로운 파일이나 디렉토리를 추가할 때는 항상 이 구조를 참고하세요. 불확실한 경우 팀원들과 상의하여 결정하세요.

### b. 커밋 규칙

커밋 메시지는 다음 형식을 따릅니다. 커밋 내용에 따라서 간략하게 작성하셔도 되고, 더 구체적으로 쓰셔도 됩니다.

##### <간단 버전>

```
feat(nginx): 홈페이지에 방문자 카운터 추가.

홈 서버 메인 페이지에 방문자 수를 보여주는 간단한 카운터를 추가.

```

##### <좀더 자세한 버전>

```
fix(docker): Plex 미디어 서버 컨테이너 재시작 문제 해결.

Plex 미디어 서버 도커 컨테이너가 자동으로 재시작되지 않는 문제 수정.

- docker-compose.yml 파일의 restart 정책을 'always'로 변경했음.

```

<br>

#### 커밋 타입

| 타입     | 설명                                       |
| -------- | ------------------------------------------ |
| feat     | 새로운 기능 추가                           |
| fix      | 버그 수정                                  |
| docs     | 문서 수정                                  |
| style    | 코드 포맷팅, 세미콜론 누락, 코드 변경 없음 |
| refactor | 코드 리팩토링                              |
| test     | 테스트 코드, 리팩토링 테스트 코드 추가     |
| chore    | 빌드 업무 수정, 패키지 매니저 수정         |

<br>

예시:

```
feat(nginx): 리버스 프록시 설정 구현

- Nginx 설정 파일에 리버스 프록시 규칙 추가
- SSL 인증서 적용 및 HTTPS 리다이렉션 설정
- 로드 밸런싱을 위한 업스트림 서버 구성

Resolves: #45

```

<br>

> [!CAUTION]
> 커밋 메시지는 항상 현재 시제로 부탁드립니다. "Added feature"가 아닌 "Add feature"로 작성해주시면 됩니다.

### c. PR(Pull Request) 규칙

PR을 생성할 때는 다음 템플릿을 사용합니다:

```markdown## 📝 PR 설명
<!-- 이 PR에서 변경한 내용을 간략히 설명해주세요 -->
홈서버의 Nginx 설정을 업데이트하여 리버스 프록시 기능을 추가했음.

## 🔍 관련 이슈
<!-- 관련된 이슈 번호를 적어주세요. 예: #123 -->
Closes #45

## ✅ 체크리스트
- [x] Nginx 설정 파일을 수정했습니다.
- [x] SSL 인증서를 적용했습니다.
- [x] 로드 밸런싱 설정을 추가했습니다.
- [x] 설정 변경 후 Nginx를 재시작했습니다.
- [x] 변경사항에 대한 문서를 업데이트했습니다.

## 📸 스크린샷 (선택사항)
![Nginx 상태 페이지](https://example.com/nginx-status.png)

## 🧪 테스트 결과
- [x] `curl` 명령어로 HTTPS 연결 테스트를 수행했습니다.
- [x] 웹 브라우저에서 사이트 접속 테스트를 진행했습니다.

## 📚 추가 정보
- Nginx 버전: 1.18.0
- 사용된 SSL 인증서: Let's Encrypt
- 로드 밸런싱 알고리즘: Round Robin

```

> 🌟 **베스트 프랙티스**: PR을 작게 유지하고 하나의 기능이나 수정에 집중해주세요오... 특히 큰 변경사항은 여러 개의 작은 PR로 나눠주시면 좋겠습니다 :)

### d. Issue 규칙

이슈를 생성할 때는 다음 가이드라인을 따릅니다:

1. **제목**: 간결하고 명확하게 작성
2. **설명**: 문제 또는 기능 요청을 상세히 기술
3. **라벨**: 적절한 라벨 부착 (bug, enhancement, documentation 등)
4. **담당자**: 가능한 경우 담당자 지정

이슈 템플릿 예시:

```markdown
## 📌 이슈 유형

- [x] 버그 리포트
- [ ] 기능 요청
- [ ] 문서 개선

## 🔍 설명

홈 서버의 Nginx 웹 서버에서 문제가 생겼어요. 사진 갤러리 페이지에 들어가려고 하면 404 에러가 뜹니다. 어제까지는 잘 됐는데 쩝..;

## 🔢 재현 단계 (버그)

1. 크롬이나 파이어폭스 아무거나 열고 http://homeserver.local/photos 주소 접속.
2. 페이지가 로딩될 때까지 기다리면 404뜸

## 🎨 기대 결과 vs 실제 결과

기대 결과: /photos 페이지에 들어가면 제가 찍은 사진들이 쫙 올라와야 합니다.
실제 결과: 그런데 404 Not Found 에러 페이지만 뜹니다.

## 💻 환경 정보

- OS: 우분투 서버 22.04 LTS (인스톨 공식문서 그대로 설치함)
- 웹 서버: Nginx 1.18.0 (이것도 최신 유튭 강의대로 설치;)
- 브라우저: 크롬이랑 파이어폭스 최신 버전 엣지까지 셋 다 해봤음

## 📎 추가 정보

- Nginx 에러 로그에서 이런 게 보이더라구요:

- error : hello world kukurubbingbbong~
```

<br>

> 📊 **이슈 관리 팁**:
>
> ```mermaid
> graph TD
>     A[이슈 생성] --> B{유형 분류}
>     B --> C[버그]
>     B --> D[기능 요청]
>     B --> E[문서 개선]
>     C --> F[우선순위 지정]
>     D --> F
>     E --> F
>     F --> G[담당자 할당]
>     G --> H[작업 시작]
> ```

<br>

## 5. Reference

다음은 홈서버 구축 관련 블로그 레퍼런스 5개입니다. 한번 읽어보시고, 더 좋은 추가할만한 자료가 있다면 PR을 통해 추가해주세요.

| 출처 | 제목                                                 | 링크                                                                                                  |
| ---- | ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| 해외 | How to Build a Home Server                           | [Acer Corner](https://blog.acer.com/en/discussion/1163/how-to-build-a-home-server)                    |
| 해외 | Building a full home server- the basics              | [The smarthome journey](https://thesmarthomejourney.com/2021/09/06/home-server-basics-ansible/)       |
| 해외 | How to get started building a Homelab server in 2025 | [Joe Karlsson](https://joekarlsson.com/2023/09/how-to-get-started-building-a-homelab-server-in-2024/) |
| 국내 | [홈서버] 홈서버 만들기                               | [코딩 배우기 ㅋㅋ;; - 티스토리](https://learningcodingreal.tistory.com/64)                            |
| 국내 | [홈서버구축하기 1] 홈서버를 구축 한 이유             | [기록, 꾸준히 작성해보자](https://blog.ewq.kr/69)                                                     |
| 국내 | 7기 부회장 윤태의 블로그                             | [yureutae-log](https://yureutae-log.vercel.app/)                                                      |
