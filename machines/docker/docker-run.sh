sleep 15
/usr/bin/docker rm postgresql
/usr/bin/docker run --name postgresql -e POSTGRES_PASSWORD=Guatemala1 -v /var/postgresql:/var/lib/postgresql/data -p 5432:5432 -d postgres
/usr/bin/docker rm nginxserver
/usr/bin/docker run --name nginxserver  -v /var/www/html/:/usr/share/nginx/html/ -p 80:80  -d nginx
