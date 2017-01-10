FROM python:3.6
RUN apt-get update && apt-get install -y build-essential nginx supervisor nodejs npm
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

RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN bower update --allow-root
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

ADD ./etc/           /home/service/etc/
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN ln -s /home/service/etc/danbi.nginx /etc/nginx/sites-enabled/danbi.conf
RUN rm /etc/nginx/sites-enabled/default
COPY ./etc/supervisord.conf /etc/supervisor/conf.d/danbi.conf

EXPOSE 8000

CMD ["supervisord", "-n"]
