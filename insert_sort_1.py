def insert_sort(ar, n):
    i = n - 1
    e = ar[i]

    while i > 0:
        if ar[i - 1] > e:
            ar[i] = ar[i - 1]
            print(" ".join(map(str, ar)))
            i -= 1
        else:
            ar[i] = e
            print(" ".join(map(str, ar)))
            return None

    ar[0] = e
    print(" ".join(map(str, ar)))

print("NEW")
insert_sort([1, 2, 3, 4, 5, 3], 6)
print("NEW")
insert_sort([1, 2, 3, 4, 5, 1], 6)
print("NEW")
insert_sort([2, 4, 6, 8, 3], 5)
print("NEW")
insert_sort([2, 4, 6, 8, 8], 5)
print("NEW")
insert_sort([2, 1], 2)
print("NEW")
insert_sort([1, 1], 2)
print("NEW")
insert_sort([3], 1)