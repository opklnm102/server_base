# danbi - django project layout

[![Build Status](https://travis-ci.com/DanbiEduCorp/server_base.svg?token=poZR3KUr6AFohfxYLU1k&branch=master)](https://travis-ci.com/DanbiEduCorp/server_base)
[![codecov](https://codecov.io/gh/DanbiEduCorp/server_base/branch/master/graph/badge.svg)](https://codecov.io/gh/DanbiEduCorp/server_base)


## 개발환경 설정

```bash
# redis - celery broker
brew install redis  # 설치
brew services start redis # redis server 실행

# postgresql
brew install postgresql  # 설치
brew services start postgresql # postgresql server 실행

# python (python 3.6 가상 환경 미리 만들어 둬야함 - pyenv 추천)
pip install -r dev-requirements.txt
# database migrate
python manage.py migrate

# front
brew install node # 노드 설치
npm install -g bower # bower 설치
bower update # 프론트 라이브러리 설치

# celery worker 실행
celery -A danbi worker -l info
# django server 실행
python manage.py runserver
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
