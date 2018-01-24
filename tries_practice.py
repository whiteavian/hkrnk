class Trie:
    def __init__(self, parent=None):
        self.items = {}
        self.parent = parent
        self.item_count = 0

    def add(self, item):
        cursor = self

        for l in item:
            if l not in cursor.items:
                cursor.items[l] = Trie(parent=cursor)

            cursor = cursor.items[l]

        if None not in cursor.items:
            cursor.items[None] = None

            while cursor.parent is not None:
                cursor.item_count += 1
                cursor = cursor.parent

            cursor.item_count += 1

    def find_partial(self, p):
        cursor = self

        for l in p:
            if l in cursor.items:
                cursor = cursor.items[l]
            else:
                return 0

        return cursor.item_count


def count_elmts(t):
    count = 0

    for k, v in t.items():
        if k is None:
            count += 1
        else:
            count += count_elmts(v)

    return count


def add(e, t):
    if len(e) == 0:
        return t

    l = e[0]

    if l not in t:
        if len(e) == 1:
            t[l] = {None: None}
        else:
            t[l] = add(e[1:], {})
    else:
        if len(e) == 1:
            t[l][None] = None
        else:
            t[l] = add(e[1:], t[l])

    return t


def find_partial(p, t):
    if len(p) == 0:
        return count_elmts(t)
    else:
        if p[0] in t:
            return find_partial(p[1:], t[p[0]])
        else:
            return 0