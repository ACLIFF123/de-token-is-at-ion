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




    def test_build_bpe_vocab_merges_common_pairs_first():
        t = Tokeniser()
        tokens = ["aa", "ab", "aa"]

        merged = t.build_bpe_vocab(tokens, num_merges=1)

        expected = [
            ["aa", "</w>"],  # "aa"
            ["a", "b", "</w>"],  # "ab"
            ["aa", "</w>"]  # "aa"
        ]

        assert merged == expected


def test_build_bpe_vocab_multiple_merges():
    t = Tokeniser()
    tokens = ["aa", "ab", "aa"]
   
    result = t.build_bpe_vocab(tokens, num_merges=2)

		# in the second merge, the most common pair is "aa" with "</w>"
    expected = [
        ["aa</w>"],  
        ["a", "b", "</w>"],  
        ["aa</w>"]   
    ]

    assert result == expected

            
def test_vocab_tracks_merged_symbols():
        t = Tokeniser()
        t.build_bpe_vocab(["aa", "ab", "aa"], num_merges=2)
        vocab = t.get_vocab()
        assert "a", "aa" and "aa</w>" in vocab
    