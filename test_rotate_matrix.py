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
#
# print "M3"
# print "ORIGINAL"
# pprint_matrix(m3)
# print "NEW MATRIX"
# pprint_matrix(rotate_matrix_n_times(m3, 4, 4, 1000000))
# print "NEW MATRIX"
# pprint_matrix(rotate_matrix_n_times(m3, 4, 4, 4))

# print "M4"
# print "ORIGINAL"
# pprint_matrix(m4)
# print "ROTATIONS: 10000001"
# pprint_matrix(rotate_matrix_n_times(m4, 5, 4, 1000001))
# print "ROTATIONS: 9"
# pprint_matrix(rotate_matrix_n_times(m4, 5, 4, 9))
# print "ROTATIONS: 23"
# pprint_matrix(rotate_matrix_n_times(m4, 5, 4, 23))
# print "ROTATIONS: 37"
# pprint_matrix(rotate_matrix_n_times(m4, 5, 4, 37))
# print "ROTATIONS: 51"
# pprint_matrix(rotate_matrix_n_times(m4, 5, 4, 51))
# print "ROTATIONS: 65"
# pprint_matrix(rotate_matrix_n_times(m4, 5, 4, 65))
#
# assert rotate_matrix_n_times(m4, 5, 4, 1000001) == rotate_matrix_n_times(m4, 5, 4, 9) == rotate_matrix_n_times(m4, 5, 4, 23) == rotate_matrix_n_times(m4, 5, 4, 37) == rotate_matrix_n_times(m4, 5, 4, 51) == rotate_matrix_n_times(m4, 5, 4, 65)
# assert rotate_matrix_n_times(m4, 5, 4, 1000002) == rotate_matrix_n_times(m4, 5, 4, 10) == rotate_matrix_n_times(m4, 5, 4, 24) == rotate_matrix_n_times(m4, 5, 4, 38) == rotate_matrix_n_times(m4, 5, 4, 52) == rotate_matrix_n_times(m4, 5, 4, 66)

# for m in (m0, m1, m2, m3, m4):
#     print "ORIGINAL"
#     pprint_matrix(m)
#     print "NEW MATRIX"
#     pprint_matrix(rotate_matrix_n_times(m, len(m), len(m[0]), 1))
#
# pprint_matrix(m0)
# pprint_matrix(rotate_matrix_n_times(m0, 2, 2, 2))
#
# print "M5"
# print "ORIGINAL"
# pprint_matrix(m5)
# print "NEW MATRIX"
# pprint_matrix(rotate_matrix_n_times(m5, 5, 4, 15))
#
# print "M6"
# print "ORIGINAL"
# pprint_matrix(m6)
# print "NEW MATRIX"
# pprint_matrix(rotate_matrix_n_times(m6, 8, 9, 301))
#
#
# import random, math
# rand_mat = [[random.randint(0, math.pow(10, 8)) for e in range(200)] for i in range(299)]
# rand_mat2 = [[random.randint(0, math.pow(10, 8)) for e in range(200)] for i in range(298)]
# rand_mat3 = [[random.randint(0, math.pow(10, 8)) for e in range(200)] for i in range(299)]
#
# i1 = 972035384
# i2 = 254171615
# i3 = 399475085

# assert rotate_matrix_n_times(rand_mat, 299, 200, 1) == rotate_matrix_n_times(rand_mat, 299, 200, 995)
# assert rotate_matrix_n_times(rand_mat, 299, 200, 2) == rotate_matrix_n_times(rand_mat, 299, 200, 996)
# pprint_matrix(rotate_matrix_n_times(rand_mat, 299, 200, i1))
# pprint_matrix(rotate_matrix_n_times(rand_mat, 299, 200, i2))
# pprint_matrix(rotate_matrix_n_times(rand_mat, 299, 200, i3))


why =\
    [
        [9718805, 60013003, 5103628, 85388216, 21884498, 38021292, 73470430, 31785927,],
        [69999937, 71783860, 10329789, 96382322, 71055337, 30247265, 96087879, 93754371,],
        [79943507, 75398396, 38446081, 34699742, 1408833, 51189, 17741775, 53195748,],
        [79354991, 26629304, 86523163, 67042516, 54688734, 54630910, 6967117, 90198864,],
        [84146680, 27762534, 6331115, 5932542, 29446517, 15654690, 92837327, 91644840,],
        [58623600, 69622764, 2218936, 58592832, 49558405, 17112485, 38615864, 32720798,],
        [49469904, 5270000, 32589026, 56425665, 23544383, 90502426, 63729346, 35319547,],
        [20888810, 97945481, 85669747, 88915819, 96642353, 42430633, 47265349, 89653362,],
        [55349226, 10844931, 25289229, 90786953, 22590518, 54702481, 71197978, 50410021,],
        [9392211, 31297360, 27353496, 56239301, 7071172, 61983443, 86544343, 43779176,],
    ]

expected = \
    [
        [93754371, 53195748, 90198864, 91644840, 32720798, 35319547, 89653362, 50410021],
        [31785927, 25289229, 10844931, 97945481, 5270000, 69622764, 27762534, 43779176],
        [73470430, 90786953, 42430633, 96642353, 88915819, 85669747, 26629304, 86544343],
        [38021292, 22590518, 90502426, 67042516, 54688734, 32589026, 75398396, 61983443],
        [21884498, 54702481, 17112485, 5932542, 29446517, 2218936, 71783860, 7071172],
        [85388216, 71197978, 15654690, 58592832, 49558405, 6331115, 10329789, 56239301],
        [5103628, 47265349, 54630910, 56425665, 23544383, 86523163, 96382322, 27353496],
        [60013003, 63729346, 51189, 1408833, 34699742, 38446081, 71055337, 31297360],
        [9718805, 38615864, 92837327, 6967117, 17741775, 96087879, 30247265, 9392211],
        [69999937, 79943507, 79354991, 84146680, 58623600, 49469904, 20888810, 55349226],
    ]

print "Orig"
pprint_matrix(why)
print "Moved 40"
pprint_matrix(rotate_matrix_n_times(why, 10, 8, 40))
print "Moved 8"
pprint_matrix(rotate_matrix_n_times(why, 10, 8, 8))
print "Expected"
pprint_matrix(expected)
