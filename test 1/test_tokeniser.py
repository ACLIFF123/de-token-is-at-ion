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
    pass