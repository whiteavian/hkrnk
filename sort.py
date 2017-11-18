def insert_sort_single(ar, n):
    i = n - 1
    e = ar[i]

    while i > 0:
        if ar[i - 1] > e:
            ar[i] = ar[i - 1]
            i -= 1
        else:
            ar[i] = e
            return ar

    ar[0] = e
    return ar

def insert_sort(ar, n):
    for i in range(1, n):
        ar = insert_sort_single(ar[:i + 1], i + 1) + ar[i + 1:]
        print(" ".join(map(str, ar)))

def quicksort(ar):
    piv = ar[0]
    left = []
    right = []

    if len(ar) == 1:
        return ar

    for el in ar[1:]:
        if el <= piv:
            left.append(el)
        elif el > piv:
            right.append(el)
    if len(left) < len(right):
        left.append(piv)
    else:
        right.append(piv)

    return quicksort(left) + quicksort(right)

def lex_quicksort(ar):
    piv = ar[0]
    piv_len = len(piv)
    left = []
    right = []

    if len(ar) == 1:
        return ar

    for el in ar[1:]:
        len_el = len(el)
        if len_el < piv_len:
            left.append(el)
        elif len_el > piv_len:
            right.append(el)

        else:
            # Lex compare if they're the same length.
            el_above_piv = lex_bigger(el, piv)
            if el_above_piv:
                right.append(el)
            else:
                left.append(el)

    if len(left) < len(right):
        left.append(piv)
    else:
        right.append(piv)

    return lex_quicksort(left) + lex_quicksort(right)

def lex_insert_sort_single(ar, n):
    i = n - 1
    e = ar[i]
    elen = len(e)

    while i > 0:
        arlen = len(ar[i - 1])
        if arlen > elen or \
                (arlen == elen and lex_bigger(ar[i-1], e)):
            ar[i] = ar[i - 1]
            i -= 1
        else:
            ar[i] = e
            return ar

    ar[0] = e
    return ar

def lex_insert_sort(ar, n):
    for i in range(1, n):
        ar = lex_insert_sort_single(ar[:i + 1], i + 1) + ar[i + 1:]
    return ar

def lex_bigger(test, control):
    for i in range(len(test)):
        if test[i] > control[i]:
            return True
        elif control[i] > test[i]:
            return False

    return True


# print("NEW")
# insert_sort([1, 2, 3, 4, 5, 3], 6)
# print("NEW")
# insert_sort([1, 2, 3, 4, 5, 1], 6)
# print("NEW")
# insert_sort([2, 4, 6, 8, 3], 5)
# print("NEW")
# insert_sort([2, 4, 6, 8, 8], 5)
# print("NEW")
# insert_sort([2, 1], 2)
# print("NEW")
# insert_sort([1, 1], 2)
# print("NEW")
# insert_sort([3], 1)
# print("NEW")
# insert_sort([4, 3, 2, 1, 8], 5)
#
# print(quicksort([4, 3, 3, 2, 1, 8]))


from input06 import foo
lex_quicksort(foo)
# lex_insert_sort(foo, len(foo))

# print(lex_quicksort([
# "31415926535897932384626433832795",
# "1",
# "3",
# "10",
# "3",
# "5",
# ]))
