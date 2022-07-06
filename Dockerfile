#Dockerfile, image, container

FROM python:3.8-slim-buster
ADD . /python-flask
WORKDIR /python-flask
RUN pip3 install -r requirements.txt
CMD [ "python3", "./app.py" ]