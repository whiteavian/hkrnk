def rotate_matrix_n_times(mat, m, n, times):
    """Rotate each ring of the matrix counterclockwise times."""
    # If we're rotating more than the size of the outer ring, there's no need to go around
    # more than once.
    new_matrix = [[None for i in xrange(n)] for j in xrange(m)]
    for indent in xrange(min(m, n) / 2):
        mod = (2 * (n + m - 4) - (4 * indent))
        local_times = times % mod if mod > times else times

        i_fill, j_fill = indent, indent
        i, j = get_next_indices(i_fill, j_fill, m, n, indent, local_times)

        new_matrix[j_fill][i_fill] = mat[j][i]
        i_fill, j_fill = get_next_indices(i_fill, j_fill, m, n, indent, 1)

        while not (i_fill == indent and j_fill == indent):
            i, j = get_next_indices(i, j, m, n, indent, 1)
            new_matrix[j_fill][i_fill] = mat[j][i]
            i_fill, j_fill = get_next_indices(i_fill, j_fill, m, n, indent, 1)

    return new_matrix

def get_next_indices(i, j, m, n, indent, times):
    """Get the next index pair traversing a matrix clockwise indent from the edge.

    i, j are the "current" location. m and n are the row and column size of the
    matrix. indent is how far the the edge of the matrix we are traversing."""

    # We are on the first row and want the element to the right of the current.
    while times > 0:
        if (i < n - indent - 1) and j == indent:
            inc = n - indent - i - 1 if i + times >= n - indent else times
            i, j = i + inc, j
        # We are on the last column and want to get the element beneath the current.
        elif (j < m - indent - 1) and i == (n - indent - 1):
            inc = m - indent - j - 1 if j + times >= m - indent else times
            i, j = i, j + inc
        # We are on the last row and want to element to the left of the current.
        elif (i > indent) and j == (m - indent - 1):
            inc = i - indent if i - times < indent else times
            i, j = i - inc, j
        # We are on the first column and want the element above the current.
        elif (j > indent) and i == indent:
            inc = j - indent if j - times < indent else times
            i, j = i, j - inc
        else:
            print "Don't you wish we were working in a language that had case " \
                  "exhaustivity checking so we could be extra sure we don't need " \
                  "this else?"

        times -= inc
        assert times >= 0

    return i, j