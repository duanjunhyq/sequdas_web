FROM php:7.3-apache
#Install git
#RUN apt-get update
#RUN apt-get install -y --no-install-recommends libjpeg-dev libpng-dev
RUN apt-get update \
  && apt-get install -y --no-install-recommends libpq-dev \
  && docker-php-ext-install mysqli pdo_pgsql pdo_mysql
RUN a2enmod rewrite
EXPOSE 80