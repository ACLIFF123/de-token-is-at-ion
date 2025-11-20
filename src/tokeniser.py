from typing import List
import string


class Tokeniser:
    def __init__(self):
        pass

    def tokenise(self, text:str) -> List[str]:

        if not text:
            return []
        
        text = text.lower()

        for c in string.punctuation:
            text = text.replace(c, "")

        return text.split()

    def count_tokens(self, tokens: list[str]) -> dict[str, int]:
        counter = {} 

        for token in tokens:
            counter[token] = counter.get(token, 0) + 1
        return counter
    
    