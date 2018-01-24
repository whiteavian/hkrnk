def letter_dict(string):
    l_dict = {}
    for l in string:
        if l not in l_dict:
            l_dict[l] = 1
        else:
            l_dict[l] += 1

    return l_dict


def number_needed(a, b):
    dict_a = letter_dict(a)
    dict_b = letter_dict(b)

    num = 0

    for l in dict_a:
        if l in dict_b:
            num += abs(dict_a[l] - dict_b[l])
            del dict_b[l]
        else:
            num += dict_a[l]

    num += sum(dict_b.values())

    return num


print number_needed('fcrxzwscanmligyxyvym', 'jxwtrhvujlmrpdoqbisbwhmgpmeoke')