from tries_practice import add, find_partial, count_elmts


def test_add():
    t = {}
    t = add('foo', t)
    assert t == {'f':
                     {'o':
                          {'o':
                               {None: None}
                           }
                      }
                 }


def test_find_partial():
    pass


def test_count_elmts():
    pass