## 하이퍼바이저

### Lesson

- Host OS의 자원을 격리해서 Guest OS를 실행하는 방식
- 각 가상 머신에 필요한 자원을 할당하고 격리 (OS 격리, 무거움)
- 예: VMWare, VirtureBox, KVM

---

## 컨테이너

### Lesson

- Host OS의 커널을 공유하여 프로세스를 격리하는 방식 (가벼움)
- Host OS의 커널을 공유하므로 다른 OS를 실행할 수 없다
- Docker는 커널의 컨테이너 가상화 기술을 쉽게 활용하도록 돕는 도구
- namespaces - 컨테이너간 격리
- cgroups - 컨테이너의 시스템 자원 관리

---

## Docker

### Code

```bash
docker run -d --name test_nginx nginx
```

### Result

```bash
docker ps

CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS     NAMES
d68bba3b5476   nginx     "/docker-entrypoint.…"   4 seconds ago   Up 2 seconds   80/tcp    test_nginx
```

### Lesson

- 도커는 리눅스 커널의 컨테이너화 기술을 쉽게 활용할 수 있도록 돕는 도구
- 이미지는 파일 시스템의 특정 시점을 저장해 놓은 압축 파일
	- 서버에서 프로그램이 실행되기 위해서는 패키지 의존성, 런타임 등 여러 요소가 필요
	- 이미지는 이러한 과정들을 압축, 미리 준비시켜 놓은 것
- 이미지인 상태에서는 디스크 공간만 차지, 컨테이너로 실행 시 CPU, MEM 등 리소스 사용

---

## dockershim

### Lesson

- 쿠버네티스가 도커를 런타임으로 사용하기 위해 필요했던 소프트웨어
- 도커에는 컨테이너의 실행을 관리하는 `containerd`가 존재
  - 따라서 도커 엔진을 거쳐 dockershim까지 사용하는 것은 비효율적
  - containerd가 발전하여 CRI 표준을 직접 지원하며 쿠버네티스 dockershim 지원 종료

---

## podman

### Lesson

- Daemonless
  - 도커와 다르게 중앙 관리 데몬이 없다 (단일 실패지점 제거)
    - 도커 데몬은 중단되면 모든 컨테이너가 영향을 받음
  - 직접 커널과 통신해 컨테이너 관리
- Rootless
  - 일반 사용자가 컨테이너를 생성, 실행 및 관리할 수 있음
  - 커널 수준 격리, 보안 향상
- Docker desktop의 유료화로 인한 대안

## 컨테이너 오케스트레이션

### Lesson

- 수많은 컨테이너의 배포, 관리, 확장 및 네트워킹을 자동화하고 조율하는 기술
- 선언적 방식
  - 우리가 선언한 상태와 일치하도록 모든 작업을 자동으로 수행
  - 예: 컨테이너 10개가 항상 실행되며 외부에서 접근시 80번 포트로만 접근 가능한 상태
- master node가 worker node를 관리하는 구조
- 예: k8s, docker swarm, nomad



