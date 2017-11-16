def rotate_matrix_n_times(mat, m, n, n_times):
    """Rotate each ring of the matrix counterclockwise n_times."""
    while n_times > 0:
        rotate_matrix(mat, m, n)
        n_times -= 1

def rotate_matrix(mat, m, n):
    """Given a matrix and dimensions, rotate counterclockwise each ring."""
    for indent in xrange(min(m, n) / 2):
        # Store the first element so it isn't lost during overwriting.
        first = mat[indent][indent]

        i, j = get_next_indices(indent, indent, m, n, indent)
        mat[indent][indent] = mat[i][j]

        # Set each index to the successor value.
        while (i != indent and j != indent):
            ip1, jp1 = get_next_indices(i, j, m, n, indent)
            mat[i][j] = mat[ip1][jp1]
            i, j = ip1, jp1

        # Set the final spot to the first.
        mat[indent + 1][indent] = first

def get_next_indices(i, j, m, n, indent):
    """Get the next index pair traversing a matrix clockwise indent from the edge.

    i, j are the "current" location. m and n are the row and column size of the
    matrix. indent is how far the the edge of the matrix we are traversing."""

    # We are on the first row and want the element to the right of the current.
    if (i + 1 <= n - indent) and j == indent:
        return i + 1, j
    # We are on the last column and want to get the element beneath the current.
    elif (j + 1 <= m - indent) and i == n - indent:
        return i, j + 1
    # We are on the last row and want to element to the left of the current.
    elif (i - 1 >= indent) and j == m - indent:
        return i - 1, j
    # We are on the first column and want the element above the current.
    elif (j - 1 >= indent) and i == indent:
        return i, j - 1
    else:
        print "Don't you wish we were working in a language that had case " \
              "exhaustivity checking so we could be extra sure we don't need " \
              "this else?"