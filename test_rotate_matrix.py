from rotate_matrix import rotate_matrix_n_times

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

m6 = \
    [
        [52846, 537577, 232587, 987588, 518174, 529424, 79721, 416452, 993668],
        [535325, 281752, 497258, 219905, 160534, 574701, 962429, 178685, 32694],
        [314491, 439513, 664831, 854827, 109256, 87523, 218950, 10633, 375085],
        [990357, 197207, 88639, 684249, 384429, 331717, 263532, 144363, 47318],
        [858470, 337586, 660540, 831968, 579084, 826854, 318971, 594068, 815839],
        [360254, 203426, 53216, 970443, 957394, 560022, 778625, 895713, 640443],
        [909668, 637062, 625963, 219916, 95712, 888610, 190928, 986027, 423796],
        [873077, 142471, 234152, 597538, 361372, 493936, 214000, 419399, 597288],
    ]

def pprint_matrix(mat):
    for row in mat:
        print row

for m in (m0, m1, m2, m3, m4):
    print "ORIGINAL"
    pprint_matrix(m)
    print "NEW MATRIX"
    pprint_matrix(rotate_matrix_n_times(m, len(m), len(m[0]), 1))

pprint_matrix(m0)
pprint_matrix(rotate_matrix_n_times(m0, 2, 2, 2))

print "M5"
print "ORIGINAL"
pprint_matrix(m5)
print "NEW MATRIX"
assert rotate_matrix_n_times(m5, 5, 4, 1) == rotate_matrix_n_times(m5, 5, 4, 15)
pprint_matrix(rotate_matrix_n_times(m5, 5, 4, 15))
assert rotate_matrix_n_times(m5, 5, 4, 300) == rotate_matrix_n_times(m5, 5, 4, 6)

print "M6"
print "ORIGINAL"
pprint_matrix(m6)
print "NEW MATRIX"
pprint_matrix(rotate_matrix_n_times(m6, 8, 9, 301))
