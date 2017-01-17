#! /bin/bash
if  [[ ${TRAVIS_BRANCH} == "master" ]] && [[ ${TRAVIS_PULL_REQUEST} == "false" ]]; then
  # Deploy only if we're testing the master branch
  echo "Deploying ${TRAVIS_BRANCH} on ${TASK_DEFINITION}"
  ./ecs-deploy.sh -c ${TASK_DEFINITION} -n ${SERVICE_NAME} -i ${REMOTE_IMAGE_URL}:latest
else
  echo "Skipping deploy because it's not an allowed branch"
fi
