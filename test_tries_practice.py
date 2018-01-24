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
    t = add('foo', t)
    assert t == {'f':
                     {'o':
                          {'o':
                               {None: None}
                           }
                      }
                 }
    t = add('fool', t)
    assert t == {'f':
                     {'o':
                          {'o':
                               {None: None,
                                'l':
                                    {None: None}
                                }
                           }
                      }
                 }



def test_find_partial():
    t = {'f':
             {'o':
                  {'o':
                       {None: None,
                        'l':
                            {None: None}
                        }
                   }
              }
         }
    assert find_partial('fool', t) == 1
    assert find_partial('f', t) == 2
    assert find_partial('foog', t) == 0
    assert find_partial('g', t) == 0


def test_count_elmts():
    t = {'f':
         {'o':
              {'o':
                   {None: None,
                    'l':
                        {None: None}
                    }
               }
          }
     }
    assert count_elmts(t) == 2
