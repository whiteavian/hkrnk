from unittest import TestCase
from hashmap import HashMap, hash_func


class TestHashMap(TestCase):

    def test_create(self):
        hm = HashMap(4, hash_func)
        assert hm.map == [[], [], [], []]

    def test_insert(self):
        hm = HashMap(256, hash_func)
        hm.insert(4, "four")
        index = hash_func(256, 4)
        assert hm.map[index] == [(4, 'four')]

    def test_get(self):
        hm = HashMap(256, hash_func)
        hm.insert(4, "four")
        assert hm.get(4) == "four"

    def test_insert_collision(self):
        pass

    def test_remove(self):
        hm = HashMap(256, hash_func)
        hm.insert(4, "four")
        hm.remove(4)
        assert hm.get(4) is None
