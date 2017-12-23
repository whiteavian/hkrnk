class Trie:
    def __init__(self, data={}, parent=None):
        # Keys are letters, values are Tries.
        self.data = data
        self.parent = parent

        self.sub_levels = 0
        self.cursor = self

    def __repr__(self):
        return "Trie ({!r})".format(self.data)

    def add(self, word):
        """Add a word to a simple dict self.data."""
        i = 0
        while i < len(word):
            letter = word[i]

            if letter not in self.cursor.data:
                self.cursor.data[letter] = Trie(data={}, parent=self.cursor)

            self.cursor = self.cursor.data[letter]
            i += 1

        self.increment_sub_levels()

    def increment_sub_levels(self):
        # Should we put the word as the key at the last spot?
        if '' not in self.cursor.data:
            self.cursor.data[''] = None

            # increment the parent sub_levels all the way up.
            while self.cursor.parent is not None:
                self.cursor.sub_levels += 1
                self.cursor = self.cursor.parent

            self.cursor.sub_levels += 1

    def find(self, word):
        """Return the number of words found in the self.data (dict) that start with the given word."""
        if len(word) > 0 and word[0] in self.data:
            return self.data[word[0]].find(word[1:])

        elif len(word) == 0:
            end_nodes = 0

            for letter in self.data:
                if self.data[letter] is None:
                    end_nodes += 1
                else:
                    end_nodes += self.data[letter].find('')

            return end_nodes

        else:
            return 0

    def remove(self, word, remove_partial=False):
        pass
