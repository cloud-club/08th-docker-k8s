### 이미지 (Image): 애플리케이션의 설계도

- 이미지는 컨테이너를 만들기 위한 읽기 전용 템플릿 (Read-Only) > '집'을 짓기 위한 '설계도'
- 특징:
  - 애플리케이션을 실행하는 데 필요한 모든 것(코드, 라이브러리, 설정 파일 등)을 포함
  - 이미지 자체는 실행되지 않는, 고정된 상태의 파일 묶음
- 실습
  - `docker pull nginx`

### 컨테이너 (Container): 설계도로 지은 실제 집

- 컨테이너는 이미지의 실행 가능한 인스턴스 > '설계도(이미지)'를 바탕으로 실제로 지어진 '집(컨테이너)'
- 특징:
  - 하나의 이미지로 여러 개의 동일한 컨테이너를 만듬 > 독립적인 공간에서 실행
  - 컨테이너는 실행, 시작, 중지, 삭제될 수 있는 살아있는 프로세스
- 실습
  - `docker run --name sikyung-nginx nginx`

### 레지스트리 (Registry): 설계도 보관소

- 레지스트리는 Docker 이미지를 저장하고 배포하는 장소 > 설계도(이미지)들을 모아놓은 '설계도 도서관'
- docker pull 명령어로 이미지를 다운로드하고, docker push 명령어로 내가 만든 이미지를 업로드할 수 있음

### Docker 명령어

1. `docker pull nginx` 레지스트리(Docker Hub)에서 이미지(nginx 설계도)를 가져옴
2. `docker run --name sikyung-nginx nginx` 컨테이너 생성 및 실행
3. `docker ps` 컨테이너 목록 확인
4. `docker stop/rm sikyung-nginx` 특정 컨테이너 중지/철거 (이미지랑 관련 없음)

### 컨테이너 생명주기 (Lifecycle)

- 컨테이너는 created(생성됨), running(실행 중), paused(일시정지), stopped(중지됨), exited(종료됨) 같은 명확한 상태를 가짐
- `docker start [컨테이너 이름]` 중지된(stopped) 컨테이너를 다시 시작
- `docker stop [컨테이너 이름]` 실행 중인(running) 컨테이너를 정상적으로 중지
- `docker kill [컨테이너 이름]` 실행 중인 컨테이너를 즉시 강제 종료
- `docker logs [컨테이너 이름]` 컨테이너 내부에서 발생하는 로그(출력)를 실시간으로 확인
- `docker exec -it [컨테이너 이름] /bin/bash` 실행 중인 컨테이너 내부에 직접 들어가서 명령어를 실행함
