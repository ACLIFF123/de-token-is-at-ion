from src.tokeniser import Tokeniser

def test_returns_list_of_words():
    t = Tokeniser()
    result = t.tokenise('hello world')
    assert result == ["hello", "world"]

def test_for_punctuation():
    t = Tokeniser()
    result = t.tokenise('The world says hello to the world.')
    assert result == ["the", "world", "says", "hello", "to", "the", "world"]

def test_tokenise_returns_dict_mapping_token_to_numbers():
    t = Tokeniser()
    result = t.count_tokens(["the", "cat", "in", "the", "hat"])
    assert result == {
  "the": 2,
  "cat": 1,
  "in": 1,
  "hat": 1
}
def test_sort_vocab():
    t = Tokeniser()
    result = t.sort_vocab({
    "the": 2,
    "cat": 1,
    "in": 1,
    "hat": 1
})
    assert result == [("the", 2), ("cat", 1), ("in", 1), ("hat", 1)]

# def test_split_into_subwords():
#     t = Tokeniser()
#     result = t.split_into_subwords(["the", "hat"])
#     assert result == [["t", "h", "e"], ["h", "a", "t"]]

def test_split_into_subwords_end_of_word():
    t = Tokeniser()
    result = t.split_into_subwords(["the", "hat"])
    assert result == [["t", "h", "e", "</w>"], ["h", "a", "t", "</w>"]]

def test_split_into_subwords_returns_characters_with_end_symbol():
    t = Tokeniser()
    result = t.split_into_subwords(["cat"])
    assert result == [["c", "a", "t", Tokeniser.END_OF_WORD_SYMBOL]]


def test_count_symbol_pairs_returns_expected_pair_frequencies():
    t = Tokeniser()
    subwords = [
        ["c", "a", "t", "</w>"],
        ["c", "a", "r", "</w>"]
    ]
    result = t.count_symbol_pairs(subwords)
    assert result[("c", "a")] == 2
    assert result[("a", "t")] == 1
    assert result[("a", "r")] == 1



def test_merge_most_frequent_pair_merges_correctly():
    t = Tokeniser()
    subwords = [
        ["t", "h", "e", "</w>"],
        ["h", "a", "t", "</w>"]
    ]
    pair_counts = {
        ("t", "h"): 1,
        ("h", "e"): 1,
        ("e", "</w>"): 1,
        ("h", "a"): 1,
        ("a", "t"): 1,
        ("t", "</w>"): 1
    }

    merged = t.merge_most_frequent_pair(subwords, pair_counts)
    assert merged[0] == ["th", "e", "</w>"]
    assert merged[1] == ["h", "a", "t", "</w>"]