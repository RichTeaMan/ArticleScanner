# Article Scanner

A project for scanning articles with the SpaCy library.

## Installing and Running

Installing:
```
pip install virtualenv
virtualenv venv
pip install -r requirements.txt
python -m spacy download en
```

Running:
```
python server.py
```

## Docker

Create image:
```
sudo docker build -t article-scanner .
```

Run container:
```
sudo docker run -d -p 5002:5002 --name article-scanner article-scanner
```

## API Reference

A Swagger reference is available in swagger.yml.
