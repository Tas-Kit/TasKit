 FROM python:2
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /TasKit
 WORKDIR /TasKit
 ADD requirements.txt /TasKit/
 RUN pip install -r requirements.txt
 RUN apt-get update
 RUN apt-get install -y gettext nodejs npm
 ADD . /TasKit/