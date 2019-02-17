FROM python

ADD *.py /articleScanner/
ADD requirements.txt /articleScanner/

WORKDIR /articleScanner
RUN pip install -r requirements.txt
RUN python -m spacy download en

ENTRYPOINT python server.py
