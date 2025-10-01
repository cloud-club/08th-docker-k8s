### Summary

1. 로컬 개발: 로컬에서 FastAPI 앱(main.py)을 개발하고 uvicorn으로 실행
2. 의존성 준비: `pip freeze` > Docker 이미지에 설치할 라이브러리 목록(requirements.txt)을 생성
3. 환경 정의: `Dockerfile` 을 작성하여 애플리케이션을 실행할 컨테이너 환경을 상세히 정의
4. 이미지 빌드: `docker build` > Dockerfile과 소스코드를 합쳐 실행 가능한 이미지를 만듦
5. 컨테이너 실행: `docker run` > 생성된 이미지를 독립된 컨테이너로 실행
6. 결과 확인: `localhost:8080` 접속 > 컨테이너 안에서 실행 중인 앱 확인

### FastAPI 실행 환경 구축

1. 프로젝트 폴더 및 가상 환경 생성 `python3 -m venv venv` > `source venv/bin/activate`
2. 라이브러리 설치 `pip install "fastapi[all]"`
3. 애플리케이션 코드 작성 및 실행 `uvicorn main:app --reload`

### Dockerfile 작성

1. 역할: 애플리케이션 실행에 필요한 모든 것(OS, 언어, 라이브러리, 코드, 실행 명령어)을 순서대로 기록한 설계도. 이 파일을 통해 어디서든 동일한 환경의 컨테이너를 생성 가능함.
2. 내용 `Dockerfile`

   ```
   # 베이스 이미지를 파이썬 3.11 슬림 버전으로 지정
   FROM python:3.11-slim

   # 컨테이너 안에서 작업할 디렉토리를 /app으로 설정
   WORKDIR /app

   # 라이브러리 목록 파일을 먼저 복사
   COPY requirements.txt .

   # 복사한 목록을 이용해 라이브러리를 설치
   RUN pip install --no-cache-dir -r requirements.txt

   # 현재 폴더의 모든 파일을 컨테이너의 /app 디렉토리로 복사
   COPY . .

   # 컨테이너가 시작될 때 실행할 명령어를 지정
   # 0.0.0.0 호스트를 사용해야 외부에서 접속이 가능
   CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

   ```

### 프로젝트 구조

    ```
    DOCKER-PRACTICE/
    ├── .dockerignore
    ├── Dockerfile
    ├── main.py
    ├── requirements.txt # 파이썬 라이브러리 의존성 목록
    └── venv/ # 파이썬 로컬 개발용 가상 환경

    ```
