# danbi - django project layout

[![Build Status](https://travis-ci.org/DanbiEduCorp/server_base.svg?branch=master)](https://travis-ci.org/DanbiEduCorp/server_base)
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
