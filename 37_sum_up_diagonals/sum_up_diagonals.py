def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    # initialize total = 0
    total = 0
    # iterate over nested list; range of length (2 or 3?)
    for m in range(len(matrix)):
        total += matrix[m][m]
        total += matrix[m][-1 -m] 
    # return total 
    return total 