from typing import List
import string

class Tokeniser:
    END_OF_WORD_SYMBOL = "</w>"
    

    def __init__(self):
        self.vocab: set[str] = set()

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
    
    def merge_most_frequent_pair(self,subword_tokens: list[list[str]],pair_counts: dict[tuple[str, str], int]) -> list[list[str]]:
        pair_counts = self.count_symbol_pairs(subword_tokens)
        if not pair_counts:
            return subword_tokens
        sorted_pairs = self.sort_vocab(pair_counts)
        most_frequent_pairs = sorted_pairs[0][0]
        first, second = most_frequent_pairs

        merged_output = []

        for token in subword_tokens:
            new_token = []
            i = 0

            while i < len(token):
                if i < len(token) - 1 and token[i] == first and token[i+1] == second:
                    new_token.append(first + second)
                    i += 2
                else:
                    new_token.append(token[i])
                    i += 1

            merged_output.append(new_token)

        return merged_output
        
    def build_bpe_vocab(self,tokens: list[str],num_merges: int) -> list[list[str]]:
        

        subword_tokens = self.split_into_subwords(tokens)

        for word in subword_tokens:
            for symbol in word:
                 self.vocab.add(symbol)
    
        for _ in range(num_merges):
            pair_counts = self.count_symbol_pairs(subword_tokens)
    
            subword_tokens = self.merge_most_frequent_pair(subword_tokens, pair_counts)

        return subword_tokens
    
    def get_vocab(self) -> set[str]:
        return self.vocab
        
