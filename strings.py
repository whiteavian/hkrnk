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
        if new_letter > upper:
            new_letter = (new_letter % upper) + lower

    return new_letter

