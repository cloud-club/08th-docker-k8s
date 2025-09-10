# Docker & Kubernetes 스터디

[![GitHub](https://img.shields.io/badge/GitHub-08th--docker--k8s-blue?style=flat-square&logo=github)](https://github.com/cloud-club/08th-docker-k8s)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)](https://kubernetes.io/)

> Docker와 Kubernetes를 심도 깊게 학습하고 실습하는 8주 스터디 프로그램

## 📋 프로젝트 개요

이 스터디는 컨테이너 기술의 핵심인 Docker와 Kubernetes를 체계적으로 학습하고 실제 프로젝트에 적용할 수 있는 실무 역량을 기르는 것을 목표로 합니다.

### 🎯 학습 목표
- **Docker**: 컨테이너화 기술의 이해와 실무 적용
- **Kubernetes**: 컨테이너 오케스트레이션과 클라우드 네이티브 아키텍처
- **실무 경험**: 실제 프로젝트에서 사용할 수 있는 실전 기술 습득
- **협업 역량**: GitHub을 통한 협업 워크플로우 숙련

### 🕑 스터디 일정
- **기간**: 8주 (2025년 9월 15일 ~ 2025년 11월 9일)
- **형식**: 온오프라인 협업 학습
- **진행**: 주간 학습 + 실습 + 코드 리뷰

## 👥 참여자

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/97tkddnjs">
        <img src="https://avatars.githubusercontent.com/u/46413809?v=4" width="100px;" alt="97tkddnjs"/>
        <br />
        <sub><b>이상원</b></sub>
      </a>
      <br />
      <sub>클라우드 클럽 8기 운영진</sub>
    </td>
    <td align="center">
      <a href="https://github.com/Seo-yul">
        <img src="https://avatars.githubusercontent.com/u/19742930?v=4" width="100px;" alt="seoyul"/>
        <br />
        <sub><b>윤서율</b></sub>
      </a>
      <br />
      <sub>클라우드 클럽 8기 클둥이</sub>
    </td>
  </tr>
</table>

## 📚 커리큘럼

### Phase 1: Docker 기초 (Week 1-4)

| Week | 주제 | 학습 내용 | 실습 |
|------|------|-----------|------|
| **Week 1** | 컨테이너와 오케스트레이션 개요 | • 컨테이너 기술이 등장한 배경 (가상머신 vs 컨테이너)<br>• Docker란 무엇인가? (개념, 장점, 활용 사례)<br>• Kubernetes가 필요한 이유 (컨테이너 오케스트레이션) | • 전체 학습 로드맵 및 실습 환경 구성<br>• Docker 설치 및 기본 환경 설정 |
| **Week 2** | Docker 기초 - 이미지와 컨테이너 | • Docker 설치 및 기본 명령어<br>• 이미지 vs 컨테이너 개념<br>• Docker Hub에서 이미지 다운로드 및 실행 | • 간단한 웹 애플리케이션 컨테이너 실행 실습<br>• 기본 Docker 명령어 연습 |
| **Week 3** | Dockerfile과 이미지 빌드 | • Dockerfile 작성법 및 주요 명령어<br>• 나만의 Docker 이미지 만들기<br>• 레이어 구조와 효율적인 이미지 빌드 | • 커스텀 이미지 생성<br>• 이미지 태깅 및 Docker Hub 푸시 |
| **Week 4** | Docker 네트워킹과 볼륨 | • Docker 네트워크 개념 및 종류<br>• 컨테이너 간 통신 설정<br>• 데이터 영속성을 위한 볼륨 관리 | • Docker Compose로 멀티 컨테이너 애플리케이션 구성<br>• 네트워크 및 볼륨 실습 |

### Phase 2: Kubernetes 기초 (Week 5-8)

| Week | 주제 | 학습 내용 | 실습 |
|------|------|-----------|------|
| **Week 5** | Kubernetes 기초 | • K8s 아키텍처 이해<br>• Pod, Deployment, Service<br>• 클러스터 구성 요소 | • Minikube/Kind 환경 구성<br>• 기본 리소스 배포 |
| **Week 6** | Kubernetes 실습 | • 애플리케이션 배포<br>• 서비스 디스커버리<br>• 로드밸런싱 | • 웹 애플리케이션 배포<br>• 서비스 연결성 테스트 |
| **Week 7** | 네트워킹 & 스토리지 | • Ingress 컨트롤러<br>• PersistentVolume<br>• 스토리지 클래스 | • 외부 접근 설정<br>• 데이터 영속성 구현 |
| **Week 8** | 고급 기능 | • ConfigMap & Secret<br>• StatefulSets & DaemonSets<br>• Helm 패키지 관리 | • 설정 관리<br>• 패키지 배포 자동화 |

## 🛠️ 기술 스택

### Core Technologies
- **Docker**: 컨테이너화 플랫폼
- **Kubernetes**: 컨테이너 오케스트레이션
- **Docker Compose**: 멀티 컨테이너 관리
- **Helm**: Kubernetes 패키지 관리자

### Development Tools
- **Minikube/Kind**: 로컬 Kubernetes 환경
- **Docker Hub**: 컨테이너 레지스트리
- **Git**: 버전 관리
- **GitHub**: 협업 플랫폼

## 📁 프로젝트 구조

```
08th-docker-k8s/
├── .github/                 # GitHub 템플릿 및 설정
│   ├── ISSUE_TEMPLATE/     # 이슈 템플릿
│   └── PULL_REQUEST_TEMPLATE/ # PR 템플릿
├── week1/                  # Week 1 학습 자료
├── week2/                  # Week 2 학습 자료
├── ...
├── week8/                  # Week 8 학습 자료
├── kimyounghee/             # 개인 작업 폴더
│   ├── week1/
│   ├── week2/
│   └── ...
├── kimchulsoo/              # 개인 작업 폴더
│   ├── week1/
│   ├── week2/
│   └── ...
└── README.md              # 프로젝트 문서
```

## 🤝 협업 가이드라인

### 📝 커밋 규칙
```bash
[Week X] 간단한 설명

자세한 변경사항 설명
```

**예시:**
- `[Week 1] Dockerfile 최적화`
- `[Week 5] Kubernetes 배포 매니페스트 추가`

### 🔄 Pull Request 규칙
- **제목**: `[Week X] 이름` 형식
- **예시**: `[Week 1] 김영희`, `[Week 1] 김철수`
- **내용**: 학습 내용, 실습 결과, 개선사항 포함

### 🐛 Issue 규칙
- 버그 리포트, 기능 요청, 일반 이슈 시 이슈 생성
- 적절한 템플릿 사용 권장
- 명확한 제목과 상세한 설명 작성

### 💬 Discussions 사용
- 질문이나 토론은 GitHub Discussions를 이용
- 학습 관련 내용 공유 및 질의응답
- 일반적인 대화와 정보 교환

#### Discussions 템플릿
- **질문**: Docker/Kubernetes 학습 중 질문
- **토론**: 기술적 주제에 대한 토론
- **학습 자료 공유**: 유용한 자료나 링크 공유
- **학습 후기**: 주차별 학습 경험 공유

### 📋 코드 리뷰
- 모든 PR에 대한 코드 리뷰 진행
- 건설적인 피드백 제공
- 학습 내용 공유 및 토론
- 모범 사례 공유 및 개선점 제안

## 🚀 시작하기

### 1. 환경 설정
```bash
# Docker 설치 확인
docker --version
docker-compose --version

# Kubernetes 환경 설정
minikube start
# 또는
kind create cluster
```

### 2. 프로젝트 클론
```bash
git clone https://github.com/cloud-club/08th-docker-k8s.git
cd 08th-docker-k8s
```

### 3. 개인 작업 폴더 생성
```bash
mkdir kimyounghee  # 또는 kimchulsoo
cd kimyounghee
mkdir week1 week2 week3 week4 week5 week6 week7 week8
```

## 📖 학습 자료

### 공식 문서
- [Docker 공식 문서](https://docs.docker.com/)
- [Kubernetes 공식 문서](https://kubernetes.io/docs/)
- [Docker Compose 문서](https://docs.docker.com/compose/)

### 추가 리소스
- [Docker Hub](https://hub.docker.com/)
- [Kubernetes GitHub](https://github.com/kubernetes/kubernetes)
- [Helm 문서](https://helm.sh/docs/)

### 프로젝트 링크
- [프로젝트 GitHub](https://github.com/cloud-club/08th-docker-k8s)
- [참여자: 김영희](https://github.com/kimyounghee)
- [참여자: 김철수](https://github.com/kimchulsoo)

## 📊 진행 상황

- [ ] Week 1: 컨테이너와 오케스트레이션 개요
- [ ] Week 2: Docker 기초 - 이미지와 컨테이너
- [ ] Week 3: Dockerfile과 이미지 빌드
- [ ] Week 4: Docker 네트워킹과 볼륨
- [ ] Week 5: Kubernetes 기초
- [ ] Week 6: Kubernetes 실습
- [ ] Week 7: 네트워킹 & 스토리지
- [ ] Week 8: 고급 기능

## 🏆 출석

| 참여자 | Week 1 | Week 2 | Week 3 | Week 4 | Week 5 | Week 6 | Week 7 | Week 8 |
|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| **이상원** | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| **윤서율** | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| **권시경** | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| **김승현** | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| **김지유** | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| **김지현** | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| **양효빈** | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| **이수민** | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| **이주원** | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| **최도아** | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |

**범례:**
- ✅ 출석
- ⏳ 진행 중
- ❌ 결석

## 🤝 기여하기

1. **이슈 생성**: 질문이나 제안사항을 이슈로 공유
2. **Fork & Branch**: 프로젝트를 포크하고 개인 브랜치에서 작업
3. **Pull Request**: 변경사항을 PR로 제출
4. **코드 리뷰**: 상호 코드 리뷰를 통한 학습
5. **피드백 반영**: 리뷰 의견을 바탕으로 코드 개선


---

**함께 성장하는 Docker & Kubernetes 스터디에 참여해주셔서 감사합니다!** 🚀