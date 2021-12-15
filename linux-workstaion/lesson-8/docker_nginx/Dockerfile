FROM ubuntu

RUN apt-get update && apt-get install -y supervisor nginx && apt clean
COPY nginx.conf /etc/supervisor/conf.d/nginx.conf
COPY index.html /var/www/html
EXPOSE 80
CMD ["supervisord", "-n"]