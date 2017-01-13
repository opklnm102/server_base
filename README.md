# danbi - django project layout

[![Build Status](https://travis-ci.com/DanbiEduCorp/server_base.svg?token=poZR3KUr6AFohfxYLU1k&branch=master)](https://travis-ci.com/DanbiEduCorp/server_base)
[![codecov](https://codecov.io/gh/DanbiEduCorp/server_base/branch/master/graph/badge.svg)](https://codecov.io/gh/DanbiEduCorp/server_base)


## 개발환경 설정
python 3.6 가상환경 필요함. django 1.10 기준
```bash

pip install -r dev-requirements.txt
python manage.py migrate
python manage.py runserver 

# 프론트
brew install node # 노드 설치
npm install -g bower # bower 설치
bower update # 프론트 라이브러리 설치
```

## 테스트

```bash
pytest
```

## docker

```bash
# 빌드
docker build -t danbi .

# 이미지 확인
docker images

# 실행
docker run -itd danbi # background

# 실행중인 프로세스 확인
docker ps
# CONTAINER ID   IMAGE   COMMAND   CREATED    STATUS    PORTS    NAMES
# ....

# 실행 후 bash 접속
docker exec -it {CONTAINER ID} /bin/bash

# *안쓰이는 이미지 정리
docker rmi -f $(docker images | grep "<none>" | awk "{print \$3}")
```
