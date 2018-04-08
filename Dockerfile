 FROM python:2
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /TasKit
 WORKDIR /TasKit
 ADD requirements.txt /TasKit/
 RUN pip install -r requirements.txt
 ADD . /TasKit/