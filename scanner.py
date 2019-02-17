import spacy

class Scanner:

    def __init__(self):
        self._nlp = spacy.load('en_core_web_sm')

    def scan(self, document):
        doc = self._nlp(document)

        tokenList = []
        for token in doc:
            tokenList.append(ScanToken(token))
        
        return tokenList

class ScanToken:
    def __init__(self, token):
        self.text = token.text
        self.lemma = token.lemma_
        self.pos = token.pos_
        self.tag = token.tag_
        self.dep = token.dep_
        self.shape = token.shape_
        self.isAlpha = token.is_alpha
        self.isStop = token.is_stop

    def serialize(self):
        return {
            'text': self.text,
            'lemma': self.lemma,
            'pos': self.pos,
            'tag': self.tag,
            'dep': self.dep,
            'shape': self.shape,
            'isAlpha': self.isAlpha,
            'isStop': self.isStop
        }