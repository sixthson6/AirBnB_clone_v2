#!/usr/bin/env bash
<<<<<<< HEAD
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
=======
# script that sets up web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
>>>>>>> 81236c8907067292981ee63fe807a410088415fa

sudo service nginx restart
