# inspiration from http://paulmouzas.github.io/2014/12/31/implementing-a-hash-table.html


class HashMap:
    def __init__(self, length, hash_function):
        self.length = length
        self.map = [[] for _ in range(length)]
        self.hash_function = lambda key: hash_function(length, key)

    def insert(self, key, value):
        hash_key = self.hash_function(key)
        entries = self.map[hash_key]

        unique_key = True
        for i, (k, v) in enumerate(entries):
            if key == k:
                entries[i] = (key, value)
                unique_key = False
                break

        if unique_key:
            entries.append((key, value))

    def get(self, key):
        hash_key = self.hash_function(key)
        entries = self.map[hash_key]

        for (k, v) in entries:
            if k == key:
                return v

    def remove(self, key):
        hash_key = self.hash_function(key)
        entries = self.map[hash_key]

        for i, (k, v) in enumerate(entries):
            if k == key:
                del entries[i]
                break


def hash_func(length, key):
    return hash(key) % length