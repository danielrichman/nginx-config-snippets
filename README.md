nginx config snippets
=====================

Contents

    .
    |-- etc
    |   |-- logrotate
    |   |-- logrotate.d
    |   |   `-- rsyslog-extra
    |   |-- nginx
    |   |   |-- nginx.conf
    |   |   |-- sites-available
    |   |   |   |-- catchall.conf
    |   |   |   |-- main_host.conf
    |   |   |   `-- ssl_server.conf
    |   |   |-- .snippets
    |   |   |   |-- flask-uwsgi.conf
    |   |   |   |-- php.conf
    |   |   |   `-- php-wordpress.conf
    |   |   `-- ssl.conf
    |   |-- php5
    |   |   `-- fpm
    |   |       |-- php.ini
    |   |       `-- pool.d
    |   |           `-- main.conf
    |   |-- rsyslog.d
    |   |   `-- 100-wsgi-apps.conf
    |   `-- supervisor
    |       `-- conf.d
    |           `-- my-flask-app.conf
    |-- opt
    |   `-- my-flask-app
    |       |-- app.debug
    |       |-- app.py
    |       |-- app.wsgi
    |       |-- requirements.txt
    |       `-- uwsgi.yaml
    |-- debian
    |   `-- etc
    |       `-- init.d
    |           `-- run-extra
    `-- ubuntu
        `-- etc
            `-- init
                `-- mounted-run-extra.conf

