FROM python:3.7-slim as production
ENV PYTHONUNBUFFERED=1
WORKDIR  /esociety/
RUN apt-get update  
# RUN pip3 install mysqlclient
RUN  apt-get install -y libmysqlclient*-dev
COPY requirements.txt ./requirements.txt
RUN  pip3 install -r ./requirements.txt
COPY manage.py ./manage.py
COPY esociety ./esociety
EXPOSE 8000
FROM production as development
COPY requirements.txt ./requirements.txt
RUN pip3 install -r ./requirements.txt
COPY . .