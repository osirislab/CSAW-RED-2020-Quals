FROM mattrayner/lamp:latest-1804

COPY ./app/intro.html /var/www/html/
COPY ./app/index.php /var/www/html/
COPY ./app/style.css /var/www/html/
COPY ./app/flag_db.sql /home/
COPY ./settings/supervisord.conf /
COPY ./settings/supervisord-db.conf /etc/supervisor/conf.d/
COPY ./settings/createdb.sh /
# RUN "mysql -u root < /home/flag_db.sql"

CMD ["/run.sh"]

# CMD ["/bin/sh", "-c", "mysql -u root < /home/flag_db.sql"]

