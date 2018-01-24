class Trie:

    def __init__(self, count=0, letter=None):
        self.letters = {letter: Trie()} if letter else {}
        self.count = count

    def add(self, word):
        cursor, remainder = self.find(word)

        if remainder and remainder != '':
            letter = remainder[0]
            cursor.count += 1

            next_letter = Trie(1, letter)
            cursor.letters[letter] = next_letter

            next_letter.add(remainder[1:])

    def find(self, word):
        cursor = self
        remainder = word

        for i in range(len(word)):
            letter = word[i]
            if letter in cursor.letters:
                cursor = cursor.letters[letter]
            else:
                remainder = word[i:]
                break

        return cursor, remainder

foo = 1
t = Trie()
cursor, remainder = t.find('fo')
t.add('foo')
cursor, remainder = t.find('fo')

def count_elmts(t):
    count = 0

    for k, v in t:
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