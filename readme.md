# Article Scanner

A project for scanning articles with the SpaCy libary.

## Docker

Create image:
```
sudo docker build -t article-scanner .
```

Run container:
```
sudo docker run -d -p 5002:5002 --name article-scanner article-scanner
```
