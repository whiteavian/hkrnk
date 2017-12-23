class Trie:
    def __init__(self, parent=None):
        # Keys are letters, values are Tries.
        self.data = {}
        self.parent = parent

        self.sub_levels = 0
        self.cursor = self

    def __repr__(self):
        return "Trie ({!r})".format(self.data)

    def add(self, word):
        """Add a word to the trie.

        If the word is already in the trie, do nothing. If it is not, add the word and increment
        all of the variable counts."""
        i = 0
        while i < len(word):
            letter = word[i]

            if letter not in self.cursor.data:
                self.cursor.data[letter] = Trie(parent=self.cursor)

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
        """Return the number of words found in the trie that start with the given word."""
        # Make sure cursor is reset before starting.
        i = 0
        self.cursor = self

        # An empty word is not in the trie.
        if len(word) == 0:
            return 0

        while i < len(word):
            letter = word[i]
            if letter in self.cursor.data:
                self.cursor = self.cursor.data[letter]
                i += 1
            else:
                return 0

        return self.cursor.sub_levels

    def remove(self, word, remove_partial=False):
        pass
