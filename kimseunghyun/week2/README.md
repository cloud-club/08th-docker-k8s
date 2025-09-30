## Docker Image

### Lesson

- 컨테이너를 실행하기 위한 읽기 전용 템플릿
- 애플리케이션과 실행에 필요한 모든 것을 포함
- Dockerfile을 통해 빌드하거나 Docker Hub 등 레지스트리에서 Pull

## Docker Container

### Lesson

- 이미지를 기반으로 실행되는 인스턴스
- 실제 기업의 경우 Harbor, Nexus 등 사내 레포지토리로 이미지를 관리
- alpine버전은 경량화에 중점을 둔 배포판

## OverlayFS

### Union Mount File System

하나의 디렉터리 지점에 여러 개의 디렉터리를 마운트함으로써 하나의 통합된 디렉터리처럼 보이게 하는 기술

### OverlayFS

Union Mount를 지원하는 파일 시스템의 한 종류이며, 리눅스 커널의 기능

- 구조
  - **lower** - 읽기 전용(불변)
  - **upper** - 읽기/쓰기 가능, 모든 변경사항 이곳에 저장
  - **merge** - 최종적으로 마운트되는 통합된 뷰
  - **work** - OverlayFS의 내부 작업용 디렉토리
- 동작
  - **읽기**
    1. upper 확인
    2. upper에 없으면 lower 순서대로 확인
    3. 첫번째로 찾은 파일을 반환
  - **쓰기**
    1. 새 파일 생성: upper에 직접 생성
    2. 기존 파일 수정: lower의 파일을 upper로 복사 후 수정
    3. 파일 삭제: upper에 whiteout 파일 생성으로 삭제 표시
  - 참고
    - lower 디렉터리 파일에 변경 사항이 발생할 경우, upper에 그 변경 사항을 기록한다
    - 모든 레이어의 내용은 merge에서 통합되어 사용할 수 있다
    - https://blog.naver.com/alice_k106/221530340759

## Docker에서의 OverlayFS 활용

### Docker 이미지 레이어 구조

```dockerfile
FROM ubuntu:20.04          # Layer 1: Base Ubuntu
RUN apt-get update         # Layer 2: Package update
RUN apt-get install nginx  # Layer 3: Nginx installation
COPY app.py /app/          # Layer 4: Application code
```

이는 다음과 같은 OverlayFS 구조를 만든다

```
┌─────────────────────┐
│  Container Layer    │ ← 읽기/쓰기 (Upper Layer)
├─────────────────────┤
│  Layer 4: app.py    │ ← 읽기 전용 (Lower Layer)
├─────────────────────┤
│  Layer 3: nginx     │ ← 읽기 전용 (Lower Layer)
├─────────────────────┤
│  Layer 2: apt update│ ← 읽기 전용 (Lower Layer)
├─────────────────────┤
│  Layer 1: ubuntu    │ ← 읽기 전용 (Lower Layer)
└─────────────────────┘
```

또한 레이어는 캐시되어 재사용된다. 즉 변경된 레이어부터만 다시 빌드하므로 빌드 속도가 향상된다

```dockerfile
FROM node:16              # Layer 1 - 캐시됨
WORKDIR /app              # Layer 2 - 캐시됨
COPY package.json .       # Layer 3 - 캐시됨
RUN npm install           # Layer 4 - 캐시됨 (package.json 변경 없으면)
COPY . .                  # Layer 5 - 새로 빌드 (소스코드 변경)
RUN npm run build         # Layer 6 - 새로 빌드
```

### 정리

- **이미지의 원본 레이어(lower)**: 읽기 전용으로 불변성을 가져 원본 파일 손상 X
- **컨테이너 레이어(upper)**: 컨테이너 실행 중 발생하는 모든 변경 사항 저장
  - 컨테이너의 루트 파일 시스템(/)은 merge로 지정된다
- 디스크 공간 절약
- 빌드 속도 향상

## 포트 포워딩

### Lesson

- 8080:80
  - 왼쪽은 내 로컬 머신의 포트를 적는 곳
  - 오른쪽에는 컨테이너의 80포트를 열어주겠다
  - 보통은 포트 일치시키는 게 국룰
  - 80번 포트에서 nginx 실행됨을 확인하려면 컨테이너가 몇번 포트가 열려있는지 알기 힘드니까 dockerfile에서 expose 80으로 기록해두는 것

## 멀티스테이지 빌드

### Code

```dockerfile
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY src/ ./src/
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

### Lesson

- 하나의 dockerfile에서 여러 개의 FROM 문을 사용해 빌드 단계를 나누어 최종 이미지 크기를 줄이고 보안을 향상시키는 기법
- 보통 빌드 단계와 실행 단계를 분리 (의존성 감소)
- 레이어 생성 원리
  - 명령어 하나당 레이어 하나 생성
  - 위에서 아래로 순차 실행
  - **하나의 레이어가 실패하면 그 아래 모든 명령어 실행 안됨**
- 명령어 배치
  - **변경 빈도가 높은 코드를 제일 아래에 배치하기**

## 과제

### Code

```Dockerfile
# dockerfile
FROM python:3.9

#
WORKDIR /code

#
COPY ./requirements.txt /code/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
COPY ./app /code/app

#
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
```

```Python
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
	return {"message": "안녕하세요 안녕히가세요"}
```

### 참고

- https://fastapi.tiangolo.com/ko/deployment/docker/#_9
