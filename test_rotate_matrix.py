from rotate_matrix import rotate_matrix, rotate_matrix_n_times

m0 = \
    [
        [1, 2],
        [3, 4],
    ]

m1 = \
    [
        [1, 2, 3],
        [4, 5, 6],
    ]

m2 = \
    [
        [1, 2],
        [3, 4],
        [5, 6],
    ]

m3 = \
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]

m4 = \
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
        [17, 18, 19, 20],
    ]

m5 = \
    [
        [1, 2, 3, 4],
        [7, 8, 9, 10],
        [13, 14, 15, 16],
        [19, 20, 21, 22],
        [25, 26, 27, 28],
    ]

def pprint_matrix(mat):
    for row in mat:
        print row

for m in (m0, m1, m2, m3, m4):
    print "ORIGINAL"
    pprint_matrix(m)
    print "NEW MATRIX"
    pprint_matrix(rotate_matrix(m, len(m), len(m[0])))

pprint_matrix(m0)
pprint_matrix(rotate_matrix_n_times(m0, 2, 2, 2))

print "M5"
print "ORIGINAL"
pprint_matrix(m5)
print "NEW MATRIX"
pprint_matrix(rotate_matrix_n_times(m5, 5, 4, 7))
