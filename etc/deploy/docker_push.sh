#! /bin/bash
# AWS LOGIN
eval $(aws ecr get-login --region ap-northeast-1)

# DOCKER
docker --version
# - cache load
if [ -f ${DOCKER_CACHE_FILE} ]; then
    gunzip -c ${DOCKER_CACHE_FILE} | docker load
fi
# - build and push
docker build -t $IMAGE_NAME .
echo "Pushing $IMAGE_NAME:latest"
docker tag $IMAGE_NAME:latest "$REMOTE_IMAGE_URL:latest"
docker push "$REMOTE_IMAGE_URL:latest"
echo "Pushed $IMAGE_NAME:latest"
# - cache save
if [[ ${TRAVIS_BRANCH} == "master" ]] && [[ ${TRAVIS_PULL_REQUEST} == "false" ]];then
    mkdir -p $(dirname ${DOCKER_CACHE_FILE})
    docker save $(docker history -q ${REMOTE_IMAGE_URL}:latest | grep -v '<missing>') | gzip > ${DOCKER_CACHE_FILE}
fi
