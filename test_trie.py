from trie import Trie


def unpack(trie):
    final = dict(trie.data)

    for key in trie.data:
        if trie.data[key] is not None:
            final[key] = unpack(trie.data[key])

    return final


def test_add():
    trie = Trie()
    trie.add("foo")
    assert unpack(trie) == {"f": {"o": {"o": {"": None}}}}
    trie.add("fool")
    assert unpack(trie) == {"f": {"o": {"o": {"": None, "l": {"": None}}}}}
    trie.add("foon")
    assert unpack(trie) == {"f": {"o": {"o": {"": None, "l": {"": None}, "n": {"": None}}}}}
    trie.add("loon")
    assert unpack(trie) == {"f":
                        {"o":
                             {"o":
                                  {"": None,
                                   "l": {"": None},
                                   "n": {"": None}
                                  }
                             }
                         },
                    "l":
                        {"o":
                             {"o":
                                  {"n": {"": None}}
                              }
                         }
                    }


def test_sub_levels():
    trie = Trie()
    trie.add("foo")
    assert trie.sub_levels == 1
    trie.add("fools")
    assert trie.sub_levels == 2
    trie.add("loon")
    assert trie.sub_levels == 3
    trie.add("foo")
    assert trie.sub_levels == 3


def test_find():
    trie = Trie()
    trie.add("foo")
    trie.add("fool")
    trie.add("foon")
    trie.add("loon")
    assert trie.find("foo") == 3
    assert trie.find("loo") == 1
    assert trie.find("loop") == 0

