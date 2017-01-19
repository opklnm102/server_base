# Base Image
# - python3.6, uwsgi, postgresql-client
# - nodejs, npm, nginx, supervisor
FROM perhapsspy/django_bundle
# Python Package
WORKDIR /home/service/
ADD ./requirements.txt /home/service/requirements.txt
RUN pip install -r requirements.txt
# Front-end Package
ADD ./bower.json     /home/service/
RUN npm install bower -g
RUN bower update --allow-root
# Service Configrations
ADD ./etc/           /home/service/etc/
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN ln -s /home/service/etc/danbi.nginx /etc/nginx/sites-enabled/danbi.conf
RUN rm /etc/nginx/sites-enabled/default
COPY ./etc/supervisord.conf /etc/supervisor/conf.d/danbi.conf
# Copy App
ADD ./manage.py      /home/service/
ADD ./danbi/         /home/service/danbi/
ADD ./sample/        /home/service/sample/
ADD ./board/         /home/service/board/
# Prepare
RUN python manage.py collectstatic --noinput --no-post-process
RUN python manage.py migrate --settings=danbi.settings_staging
# Port
EXPOSE 80
# Run
CMD ["supervisord", "-n"]
