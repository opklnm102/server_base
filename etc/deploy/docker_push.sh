#! /bin/bash
# AWS LOGIN
eval $(aws ecr get-login --region ap-northeast-1)

# DOCKER
docker --version
# - build and push
docker build -t $IMAGE_NAME .
echo "Pushing $IMAGE_NAME:latest"
docker tag $IMAGE_NAME:latest "$REMOTE_IMAGE_URL:latest"
docker push "$REMOTE_IMAGE_URL:latest"
echo "Pushed $IMAGE_NAME:latest"
