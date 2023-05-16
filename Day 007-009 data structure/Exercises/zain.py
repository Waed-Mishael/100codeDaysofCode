import copy

board = [[0,0,0,0,0,0,0,0,9],
         [0,0,0,0,0,0,0,0,0],
         [4,0,7,2,0,8,0,0,0],
         [0,0,0,1,8,0,7,0,0],
         [0,0,0,0,0,0,4,0,0],
         [7,0,0,0,0,5,3,1,0],
         [0,3,0,0,0,6,1,0,0],
         [0,0,0,0,0,1,2,0,0],
         [0,0,4,0,0,3,6,0,0]]

def _col_options(board,i,j,lst):
    the_col = []
    copy_lst = copy.deepcopy(lst)
    for index in range(9):
        if board[i][j]!= board[i][index]:
            the_col.append(board[i][index])
    set_lst = set(lst)
    the_set = set(the_col) & set_lst
    for element in copy_lst:
        if element in the_set:
            lst.remove(element)
    return lst


def _row_options(board,i,j,lst):
    the_row = []
    copy_lst = copy.deepcopy(lst)
    for index in range(9):
        if board[i][j] != board[index][j] :
            the_row.append(board[index][j])
    set_lst = set(lst)
    the_set = set(the_row) & set_lst
    for element in copy_lst:
        if element in the_set:
            lst.remove(element)
    return lst


def _diag_options(board,i,j,lst):
    the_diag = []
    copy_lst = copy.deepcopy(lst)
    for index in range(9):
        if index != i:
            the_diag.append(board[index][index])
    set_lst = set(lst)
    the_set = set(the_diag) & set_lst
    for element in copy_lst:
        if element in the_set:
            lst.remove(element)
    return lst


def _other_diag_options(board,i,j,lst):
    the_other_diag = []
    copy_lst = copy.deepcopy(lst)
    for g in range(9):
        for index in range(8,-1,-1):
            if g + index == 8:
                the_other_diag.append(board[index][g])
    the_other_diag.remove(board[i][j])
    set_lst = set(lst)
    the_set = set(the_other_diag) & set_lst
    for element in copy_lst:
        if element in the_set:
            lst.remove(element)
    return lst


def _square_options(board,i,j,lst):
    square_lst = []
    copy_lst = copy.deepcopy(lst)
    #square = sudoku_square3x3(board,i,j)
    square = [[0,0,0],[0,0,0],[0,0,9]]
    for outer in range(len(square)):
        for insider in range(len(square[0])):
            if square[outer][insider] != board[i][j]:
                square_lst.append(square[outer][insider])
    set_lst = set(lst)
    the_set = set(square_lst) & set_lst
    for element in copy_lst:
        if element in the_set:
            lst.remove(element)
    return lst

def sudoku_options(board,i,j,diag = False):
    all_options = [1,2,3,4,5,6,7,8,9]
    col_options = _col_options(board,i,j,all_options)
    row_options = _row_options(board,i,j,col_options)
    square_options = _square_options(board,i,j,row_options)
    if diag:
        if i == j:
            diag_options = _diag_options(board,i,j,square_options)
            return set(diag_options)
        other_diag_opyions = _other_diag_options(board,i,j,square_options)
        return set(other_diag_opyions)
    return set(square_options)

print(sudoku_options(board,0,8,True))