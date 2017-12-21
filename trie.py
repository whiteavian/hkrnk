def add(trie, word):
    """Add a word to a simple dict trie."""
    if len(word) > 0:
        letter = word[0]

        if trie:
            if letter in trie:
                trie[letter] = add(trie[letter], word[1:])
            else:
                trie[letter] = add({}, word[1:])
        else:
            trie = {letter: add({}, word[1:])}
    else:
        trie[word] = None

    return trie

def find(trie, word):
    """Return the number of words found in the trie (dict) that start with the given word."""
    if len(word) > 0 and word[0] in trie:
        return find(trie[word[0]], word[1:])

    elif len(word) == 0:
        end_nodes = 0

        for letter in trie:
            if trie[letter] is None:
                end_nodes += 1
            else:
                end_nodes += find(trie[letter], '')

        return end_nodes

    else:
        return 0
