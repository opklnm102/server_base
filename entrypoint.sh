#!/usr/bin/env bash

# Prepare
if [ $DEPLOYMENT_ROLE = "celery" ]
then
  cp ./etc/supervisord-celery.conf /etc/supervisor/conf.d/danbi.conf
else
  cp ./etc/supervisord-web.conf /etc/supervisor/conf.d/danbi.conf
fi

# Start
supervisord -n
