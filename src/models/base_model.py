from typing import List
from abc import abstractmethod
from corpus import Corpus
from document import Document


class BaseModel:

    def __init__(self, corpus: Corpus):
        self.corpus = corpus

    @abstractmethod
    def search(self, query: str) -> List[Document]: 
        """
            Search for the most relevant set of documents in the corpus, 
            given a specific query.
        """
        pass