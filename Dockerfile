FROM python:3.6
RUN apt-get update && apt-get install -y build-essential nginx supervisor nodejs npm postgresql-client
RUN \
    pip install setuptools pip --upgrade && \
    pip install uwsgi
RUN npm install bower -g

WORKDIR /home/service/
ADD ./requirements.txt /home/service/requirements.txt
RUN pip install -r requirements.txt

ADD ./bower.json     /home/service/
ADD ./manage.py      /home/service/
ADD ./danbi/         /home/service/danbi/
ADD ./sample/        /home/service/sample/
ADD ./board/         /home/service/board/

RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN bower update --allow-root
RUN python manage.py collectstatic --noinput --no-post-process
RUN python manage.py migrate --settings=danbi.settings_staging

ADD ./etc/           /home/service/etc/
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN ln -s /home/service/etc/danbi.nginx /etc/nginx/sites-enabled/danbi.conf
RUN rm /etc/nginx/sites-enabled/default
COPY ./etc/supervisord.conf /etc/supervisor/conf.d/danbi.conf

EXPOSE 80

CMD ["supervisord", "-n"]
