FROM python:3.7.3-stretch
ENV PYTHONUNBUFFERED 1

run mkdir /Model_api
WORKDIR /Model_api

COPY requirements.txt /Model_api/

run pip install -r requirements.txt

COPY . /Model_api/

CMD ["/bin/bash","/Model_api/start.sh"]

EXPOSE $PORT  