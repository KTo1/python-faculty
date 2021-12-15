FROM ubuntu
  
ENV TZ=Europe/Moscow
 
RUN apt-get update
RUN apt-get install -y nginx
RUN apt-get -y install php7.4 php7.4-cli php7.4-fpm php7.4-json php7.4-pdo php7.4-mysql php7.4-zip php7.4-gd php7.4-mbstring php7.4-curl php7.4-xml php-pear php7.4-bcmath
RUN apt-get -y install supervisor 
COPY www.conf /etc/php/7.4/fpm/pool.d/www.conf
COPY default /etc/nginx/sites-available/default
COPY /html/index.php /var/www/html/index.php
COPY nginx.conf /etc/supervisor/conf.d/nginx.conf
CMD ["supervisord", "-n"]
EXPOSE 80