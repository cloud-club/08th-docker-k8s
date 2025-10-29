DIY1
-------

#### 과제 설명

```
로컬 환경에 있는 nginx 이미지를 가지고 외부에서 8000 포트로 접근 가능하도록 nhnedu 이름의 컨테이너를 실행합니다.

index.html 파일에서 welcome to nginx 글자를 자신의 이름으로 변경합니다.

※ nginx 컨테이너 내에서 패키지 업데이트 및 vim 패키지도 설치해주세요.
```

#### 과제 수행

    $ docker pull nginx
    $ docker images
    $ docker run --name nhnedu -d -p 8000:80 nginx
    $ docker ps

#### 컨테이너 내부 접근
    $ docker exec -it nhnedu bash
    $ apt-get update && apt-get install vim
    $ cat /var/log/apt/history.log | more
    $ apt list --installed vim    

DIY2
-------

#### 과제 설명
```
새로운 이미지 제작을 위한 Dockerfile 작성

[조건]
1. nginx 최신 버전 이미지 사용
2. 작업 디렉터리 /app 지정
3. COPY . .
4. 3가지 명령어 실행 (&&으로 연결)
  4-1. apt-get update
  4-2. apt-get install -y vim
  4-3. index.html 파일 대체
5. mynginx 명칭 이미지 빌드 및 이름으로 8002번 포트 컨테이너 실행
```

#### 도커 파일 작성
    # Use latest Nginx base image
    FROM nginx:latest

    # Set working directory
    WORKDIR /app

    # Copy project files
    COPY . .

    # Install vim, replace default page, and clean apt cache
    RUN apt-get update \
        && apt-get install -y vim \
        && echo "<h1>Choi Doa</h1>" > /usr/share/nginx/html/index.html \
        && rm -rf /var/lib/apt/lists/*

    # Expose port 80
    EXPOSE 80

#### 이미지 빌드 및 실행
    $ docker build -t mynginx:latest .
    $ docker images
    $ docker run --name choidoa -d -p 8002:80 mynginx
    $ docker ps

#### kubeadm
    $ kubectl get namespace
    NAME              STATUS   AGE
    default           Active   23m
    kube-node-lease   Active   23m
    kube-public       Active   23m
    kube-system       Active   23m

