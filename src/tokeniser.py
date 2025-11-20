from typing import List
import string





class Tokeniser:
    END_OF_WORD_SYMBOL = "</w>"
    

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
    
    def sort_vocab(self, token_counts: dict[str, int]) -> list[tuple[str, int]]:
        
        items = list(token_counts.items())

        items.sort(key=lambda x: x[1], reverse= True)

        return items
    
    def split_into_subwords(self, tokens: list[str]) -> list[list[str]]:
        
        result = []

        for token in tokens:
            chars = list(token)
            chars.append(self.END_OF_WORD_SYMBOL)
            result.append(chars)
        return result
        
    def count_symbol_pairs(self, subword_tokens: list[list[str]]) -> dict[tuple[str, str], int]:
        counter = {}

        for word in subword_tokens:
            for i in range(len(word) -1):
                pair_char = (word[i], word[i + 1])
                counter[pair_char] = counter.get(pair_char, 0) + 1 

        return counter

