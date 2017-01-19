FROM perhapsspy/django_bundle

WORKDIR /home/service/
ADD ./requirements.txt /home/service/requirements.txt
RUN pip install -r requirements.txt

ADD ./bower.json     /home/service/
RUN npm install bower -g
RUN bower update --allow-root

ADD ./manage.py      /home/service/
ADD ./danbi/         /home/service/danbi/
ADD ./sample/        /home/service/sample/
ADD ./board/         /home/service/board/

RUN python manage.py collectstatic --noinput --no-post-process

ADD ./etc/           /home/service/etc/
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN ln -s /home/service/etc/danbi.nginx /etc/nginx/sites-enabled/danbi.conf
RUN rm /etc/nginx/sites-enabled/default
COPY ./etc/supervisord.conf /etc/supervisor/conf.d/danbi.conf

EXPOSE 80

CMD ["supervisord", "-n"]
