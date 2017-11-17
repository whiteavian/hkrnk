def rotate_matrix_n_times(mat, m, n, n_times):
    """Rotate each ring of the matrix counterclockwise n_times."""
    # If we're rotating more than the size of the outer ring, there's no need to go around
    # more than once.
    new_matrix = [[None for i in xrange(n)] for j in xrange(m)]
    for indent in xrange(min(m, n) / 2):
        mod = (2 * (n + m - 4) - (4 * indent))
        local_n_times = n_times % mod if mod > n_times else n_times

        i_fill, j_fill = indent, indent
        i, j = i_fill, j_fill
        while local_n_times > 0:
            local_n_times -= 1
            i, j = get_next_indices(i, j, m, n, indent)

        new_matrix[j_fill][i_fill] = mat[j][i]
        i_fill, j_fill = get_next_indices(i_fill, j_fill, m, n, indent)

        while not (i_fill == indent and j_fill == indent):
            i, j = get_next_indices(i, j, m, n, indent)
            new_matrix[j_fill][i_fill] = mat[j][i]
            i_fill, j_fill = get_next_indices(i_fill, j_fill, m, n, indent)


    return new_matrix

def get_next_indices(i, j, m, n, indent):
    """Get the next index pair traversing a matrix clockwise indent from the edge.

    i, j are the "current" location. m and n are the row and column size of the
    matrix. indent is how far the the edge of the matrix we are traversing."""

    # We are on the first row and want the element to the right of the current.
    if (i + 1 < n - indent) and j == indent:
        return i + 1, j
    # We are on the last column and want to get the element beneath the current.
    elif (j + 1 < m - indent) and i == (n - indent - 1):
        return i, j + 1
    # We are on the last row and want to element to the left of the current.
    elif (i - 1 >= indent) and j == (m - indent - 1):
        return i - 1, j
    # We are on the first column and want the element above the current.
    elif (j - 1 >= indent) and i == indent:
        return i, j - 1
    else:
        print "Don't you wish we were working in a language that had case " \
              "exhaustivity checking so we could be extra sure we don't need " \
              "this else?"