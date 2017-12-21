from trie import add, find

def test_add():
    trie = {}
    trie = add(trie, "foo")
    assert trie == {"f": {"o": {"o": None}}}
    trie = add(trie, "fool")
    assert trie == {"f": {"o": {"o": {"l": None}}}}
    trie = add(trie, "foon")
    assert trie == {"f": {"o": {"o": {"l": None, "n": None}}}}
    trie = add(trie, "loon")
    assert trie == {"f":
                         {"o":
                             {"o":
                                  {"l": None, "n": None}
                              }
                         },
                    "l":
                        {"o":
                             {"o":
                                  {"n": None}
                              }
                         }
                    }

def test_find():
    trie = {"f":
                 {"o":
                     {"o":
                          {"l": None, "n": None}
                      }
                 },
            "l":
                {"o":
                     {"o":
                          {"n": None}
                      }
                 }
            }
    assert find(trie, "foo") == 2
    assert find(trie, "loo") == 1
    assert find(trie, "loop") == 0
