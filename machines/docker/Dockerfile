FROM ubuntu:18.04
RUN apt-get update && apt-get upgrade -y && apt-get install python-psycopg2 python3 python3-pip libpq-dev python-dev net-tools apt-utils -y
RUN pip3 install flask flask_sqlalchemy flask_httpauth flask_cors werkzeug jwt psycopg2 sqlalchemy
COPY ../*.py /app
#RUN make /app
#CMD python /app/app.py