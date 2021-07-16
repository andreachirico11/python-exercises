
# Valid Sudoku
# Determine if a 9x9 Sudoku board is valid.
# Only the filled cells need to be validated according to the following rules:
# 1. Each row must contain the digits 1-9 without repetition.
# 2. Each column must contain the digits 1-9 without repetition.
# 3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# A partially filled sudoku which is valid.
# The Sudoku board could be partially filled, where empty cells are filled with the character ‘.’.
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
# The given board contain only digits 1-9 and the character ‘.’. The given board size is always 9x9.
# e.g.,
# Example 1:
# Input:

valid = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
# 5
# Output: true
# Example 2:
# Input:
invalid = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8.
# Since there are two 8’s in the top left 3x3 sub-box, it is invalid.
# [ ]:


def row_col_validator(row):
    for element in row:
        if element == '.':
            continue
        if row.count(element) > 1:
            return False
    return True


def get_col_from_row(mat, n):
    output = []
    for row in mat:
        output.append(row[n])
    return output


def get_mat_slice(mat, length, start_x, start_y):
    output = []
    i = start_y
    while i <= length + start_y - 1:
        output.append(mat[i][start_x: start_x+length])
        i += 1
    return output


def mat_n_occurrence(mat):
    linear_mat = []
    for row in mat:
        linear_mat += row
    return row_col_validator(linear_mat)


def sudoku_validator(sudoku):
    for row in sudoku:
        if not row_col_validator(row):
            return False
    for i, _ in enumerate(sudoku[0]):
        if not row_col_validator(get_col_from_row(sudoku, i)):
            return False
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            mat_slice = get_mat_slice(sudoku, 3, i, j)
            if not mat_n_occurrence(mat_slice):
                return False
    return True
