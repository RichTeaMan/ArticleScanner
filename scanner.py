import spacy

class Scanner:

    def __init__(self):
        self._nlp = spacy.load('en_core_web_sm')

    def scan(self, document):
        doc = self._nlp(document)

        tokenList = []
        for token in doc:
            tokenList.append(ScanToken(token))
            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
                token.shape_, token.is_alpha, token.is_stop)
        
        return tokenList

class ScanToken:
    def __init__(self, token):
        self.text = token.text

    def serialize(self):
        return {
            'text': self.text
        }