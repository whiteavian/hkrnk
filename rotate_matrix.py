def rotate_matrix_n_times(mat, m, n, n_times):
    """Rotate each ring of the matrix counterclockwise n_times."""
    # If we're rotating more than the size of the outer ring, there's no need to go around
    # more than once.
    for indent in xrange(min(m, n) / 2):
        mod = (2 * (n + m - 4) - (4 * indent))
        local_n_times = n_times % mod if mod > n_times else n_times

        while local_n_times > 0:
            local_n_times -= 1
            mat = rotate_matrix_indent(mat, m, n, indent)

    return mat

def rotate_matrix_indent(mat, m, n, indent):
    """Given a matrix and dimensions, rotate counterclockwise each ring."""
    # Store the first element so it isn't lost during overwriting.
    first = mat[indent][indent]

    i, j = get_next_indices(indent, indent, m, n, indent)
    mat[indent][indent] = mat[j][i]

    # Set each index to the successor value.
    while not (i == indent and j == indent):
        ip1, jp1 = get_next_indices(i, j, m, n, indent)
        mat[j][i] = mat[jp1][ip1]
        i, j = ip1, jp1

    # Set the final spot to the first.
    mat[indent + 1][indent] = first

    return mat

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