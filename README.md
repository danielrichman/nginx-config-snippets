nginx config snippets
=====================

Contents

    .
    |-- etc
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
    |   `-- supervisor
    |       `-- conf.d
    |           `-- my-flask-app.conf
    |-- debian
    |   `-- etc
    |       `-- init.d
    |           `-- run-extra
    `-- ubuntu
        `-- etc
            `-- init
                `-- mounted-run-extra.conf

