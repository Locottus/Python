docker rm postgresql
docker run --name postgresql -e POSTGRES_PASSWORD=Guatemala1 -v /var/postgresql:/var/lib/postgresql/data -p 5432:5432 -d postgres
