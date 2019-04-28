# Document Scanner

![Docker Automated build](https://img.shields.io/docker/automated/richteaman/document-scanner.svg)

A project for scanning articles with the SpaCy library.

## Installing and Running

Installing:
```bash
pip install virtualenv
virtualenv venv
pip install -r requirements.txt
python -m spacy download en
```

Running:
```bash
python server.py
```

## Docker

Create image:
```bash
sudo docker build -t article-scanner .
```

Run container:
```bash
sudo docker run -d -p 5002:5002 --name article-scanner article-scanner
```

## API Reference

A Swagger reference is available in swagger.yml.

### Curl Example

```bash
curl -X POST http://localhost:5002/scan -F 'document=I do not like green eggs and ham'
```

A scanUpload endpoint also exists that can parse file attachments. This is
useful for larger documents that would otherwise cause 414 URI too long
problems.
```bash
curl -X POST -F document=@data.txt http://localhost:5002/scanUpload
```
data.txt is expected to be a plain text file for the document to be analysed.


Response
```json
{
    "tokens": [
        {
            "dep": "nsubj",
            "isAlpha": true,
            "isStop": true,
            "lemma": "-PRON-",
            "pos": "PRON",
            "shape": "X",
            "tag": "PRP",
            "text": "I"
        },
        {
            "dep": "aux",
            "isAlpha": true,
            "isStop": true,
            "lemma": "do",
            "pos": "VERB",
            "shape": "xx",
            "tag": "VBP",
            "text": "do"
        },
        {
            "dep": "neg",
            "isAlpha": true,
            "isStop": true,
            "lemma": "not",
            "pos": "ADV",
            "shape": "xxx",
            "tag": "RB",
            "text": "not"
        },
        {
            "dep": "ROOT",
            "isAlpha": true,
            "isStop": false,
            "lemma": "like",
            "pos": "VERB",
            "shape": "xxxx",
            "tag": "VB",
            "text": "like"
        },
        {
            "dep": "amod",
            "isAlpha": true,
            "isStop": false,
            "lemma": "green",
            "pos": "ADJ",
            "shape": "xxxx",
            "tag": "JJ",
            "text": "green"
        },
        {
            "dep": "dobj",
            "isAlpha": true,
            "isStop": false,
            "lemma": "egg",
            "pos": "NOUN",
            "shape": "xxxx",
            "tag": "NNS",
            "text": "eggs"
        },
        {
            "dep": "cc",
            "isAlpha": true,
            "isStop": true,
            "lemma": "and",
            "pos": "CCONJ",
            "shape": "xxx",
            "tag": "CC",
            "text": "and"
        },
        {
            "dep": "conj",
            "isAlpha": true,
            "isStop": false,
            "lemma": "ham",
            "pos": "NOUN",
            "shape": "xxx",
            "tag": "NN",
            "text": "ham"
        }
    ]
}
```