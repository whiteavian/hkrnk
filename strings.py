def validate(chars):
    if len(chars) == 1:
        return False
    for i in range(len(chars)-1):
        if chars[i] == chars[i+1]:
            return False
    return True

def longest_two_char_str_from_deletions(s):
    chars = set(s)
    max = 0

    for c1 in chars:
        for c2 in chars:
            char_str = [c for c in s if c == c1 or c == c2]
            if validate(char_str):
                if len(char_str) > max:
                    max = len(char_str)

def caesar_cipher(initial_str, shift_n):
    """Given a string and a shift number, return the Caesar cipher."""
    shift_n = shift_n % 26
    letters = {}
    final_str = ''

    for i in range(len(initial_str)):
        letter = initial_str[i]

        if letter not in letters:
            letter_ascii = ord(letter)
            # Shift lowercase letters
            new_letter = shift(letter_ascii, shift_n, 97, 123)
            # Shift uppercase letters
            new_letter = new_letter if new_letter else shift(letter_ascii, shift_n, 65, 91)
            new_letter = chr(new_letter) if new_letter else letter
            letters[letter] = new_letter
            letter = new_letter
        else:
            letter = letters[letter]

        final_str += letter

    return final_str


def shift(letter, n, lower, upper):
    """Shift an ascii code by n within the lower and upper bounds."""
    new_letter = None

    if letter in range(lower, upper):
        new_letter = letter + n
        if new_letter >= upper:
            new_letter = (new_letter % upper) + lower

    return new_letter

def sos(s):
    sos = "SOS"
    i = 0
    diffs = 0

    for l in s:
        if l != sos[i]:
            diffs += 1
        i += 1
        i = i % 3

    return diffs


def pangrams(s):
    """Return if the string contains each letter of the alphabet at least once, case insensitive."""
    letters = set(s.lower())

    if " " in letters and len(letters) == 27:
        return "pangram"
    elif " " not in letters and len(letters) == 26:
        return "pangram"
    else:
        return "not pangram"


def substring_in_strings(strings, substring):
    """Given a list of strings, return if the substring can be found in order but not consecutively in each.

    For example, if a string is hello, it contains the substrings helo and hlo, but not the substring hle.
    """
    len_substring = len(substring)
    out = []

    for string in strings:
        i = 0

        for l in string:
            if l == substring[i]:
                i += 1
            if i == len_substring:
                out.append(True)
                break

        out.append(False)

    return out

def contiguous_substring_weights(string):
    contig_substr_weights = set()

    previous = None

    for letter in string:
        if letter == previous:
            weight += ord(letter) - 96
        else:
            previous = letter
            weight = ord(letter) - 96

        contig_substr_weights.add(weight)

    return contig_substr_weights

