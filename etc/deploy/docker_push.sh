#! /bin/bash
if  [[ ${TRAVIS_BRANCH} == "master" ]] && [[ ${TRAVIS_PULL_REQUEST} == "false" ]]; then
  # AWS LOGIN
  eval $(aws ecr get-login --region ap-northeast-1)
  # DOCKER
  docker --version
  # - cache load
  if [[ -e docker/image.tar ]]; then
   docker load -i ${HOME}/docker/image.tar
  fi
  # - build and push
  docker build -t ${IMAGE_NAME} .
  echo "Pushing ${IMAGE_NAME}:latest"
  docker tag ${IMAGE_NAME}:latest "${REMOTE_IMAGE_URL}:latest"
  docker push "${REMOTE_IMAGE_URL}:latest"
  echo "Pushed ${IMAGE_NAME}:latest"
  # - cache save
  mkdir -p ~/docker;
  docker save ${IMAGE_NAME}:latest > ${HOME}/docker/image.tar
else
  echo "Skipping deploy because branch is not 'master'"
fi
