FROM python:3.6-slim

RUN apt-get clean \
    && apt-get -y update \
    && apt-get -y install --no-install-recommends nginx python3-dev build-essential \
    && rm -rf /var/lib/apt/lists/*

ADD dockerStart.sh /articleScanner/dockerStart.sh
ADD uwsgi.ini /articleScanner/uwsgi.ini
COPY nginx.conf /etc/nginx
RUN chmod +x ./articleScanner/dockerStart.sh

ADD requirements.txt /articleScanner/
WORKDIR /articleScanner
RUN pip install -r requirements.txt \
    && python -m spacy download en

ADD *.py /articleScanner/

ENTRYPOINT ./dockerStart.sh
