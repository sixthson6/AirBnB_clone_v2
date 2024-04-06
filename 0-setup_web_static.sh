#!/usr/bin/env bash
-- setup web server for application deployment

sudo apt-get update -y

sudo apt-get install nginx -y

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

echo -e "this is an nginx server" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown --recursive ubuntu:ubuntu /data/

my_setup="server {
	listen 80;
	listen [::]:80;

	root /var/www/html;
	server_name _;
	
	location / {
		try_files $uri $uri/ =404;
	}

	location /hnbn_static/ {
		alias /data/web_static/current/;
	}
	
	error_page 404 /404.html;

	location = /404.html {
		internal;
	}
};"

echo -e "$my_setup" | sudo tee /etc/nginx/sites-available/default > /dev/null

sudo service nginx restart
