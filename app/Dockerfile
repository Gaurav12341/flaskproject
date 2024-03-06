FROM python:3.9-slim

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt
CMD gunicorn --bind 0.0.0.0:5000 wsgi:app


#image name: dockapp, container name flaskcontainer
#docker build -t dockapp .
#docker run -p80:5000 --name flaskcontainer dockapp