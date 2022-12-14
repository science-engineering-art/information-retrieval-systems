import re
from typing import List
import spacy
from unidecode import unidecode
from collections import Counter
from models.dict import Dict

NLP = spacy.load('en_core_web_sm') 

class Document(Dict):

    def __new__(cls, _):
        return super().__new__(cls)

    def __init__(self, doc):
        self._doc_id = doc.doc_id
        # tokenization and standardization 
        if 'text' in doc._fields:
            self.__dict__.update(Counter(self.tokenizer(doc.text)))
        elif 'abstract' in doc._fields:
            self.__dict__.update(Counter(self.tokenizer(doc.abstract)))

    def tokenizer(self, text) -> List[str]:
        return [ unidecode(word.lower()) for word in 
            re.findall(r"[\w']+", text) ]

    def __iter__(self):
        for k in self.__dict__:
            if len(k) > 0 and k[0] != '_': yield k


class DocumentWithOnlyNouns(Document):

    def tokenizer(self, text) -> List[str]:
        return [ word.lemma_ for word in NLP(text) 
            if not word.is_stop and not word.conjuncts 
            and not word.is_punct and not word.is_quote
            and not word.is_space ]
