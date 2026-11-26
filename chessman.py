import multiprocessing as mp
from pprint import pprint

class __MatrixOperation:
    # constructor
    _rowlen = 0
    _collen = 0
    __matrix = None
    __king = None
    __enemy = None
    
    # update the inside matrix and current king on which the further matrix operation is performed
    def _current_matrix(self, matrix, king, enemy):
        self.__matrix = matrix
        self.__king = king
        self.__enemy = enemy
    
    # check that the chessman can move or not
    def _can_move(self, matrix, pos):
        row, col = pos
        if matrix[row][col] == 1:
            if row+1 > 0 and row+1 < self._rowlen and col-1 >= 0 and col-1 < self._collen and (matrix[row+1][col-1] > 6):
                return True
            elif row+1 > 0 and row+1 < self._rowlen and col+1 >= 0 and col+1 < self._collen and (matrix[row+1][col+1] > 6):
                return True
            elif row+1 > 0 and row+1 < self._rowlen and col >= 0 and col < self._collen and (matrix[row+1][col] == 0):
                return True
            else:
                return False
        elif matrix[row][col] == 2:
            if row-2 >= 0 and row-2 < self._rowlen and col+1 >= 0 and col+1 < self._collen and ((matrix[row-2][col+1] > 6) or (matrix[row-2][col+1] == 0)):
                return True
            elif row-1 >= 0 and row-1 < self._rowlen and col+2 >= 0 and col+2 < self._collen and ((matrix[row-1][col+2] > 6) or (matrix[row-1][col+2] == 0)):
                return True
            elif row+1 >= 0 and row+1 < self._rowlen and col+2 >= 0 and col+2 < self._collen and ((matrix[row+1][col+2] > 6) or (matrix[row+1][col+2] == 0)):
                return True
            elif row+2 >= 0 and row+2 < self._rowlen and col+1 >= 0 and col+1 < self._collen and ((matrix[row+2][col+1] > 6) or (matrix[row+2][col+1] == 0)):
                return True
            elif row+2 >= 0 and row+2 < self._rowlen and col-1 >= 0 and col-1 < self._collen and ((matrix[row+2][col-1] > 6) or (matrix[row+2][col-1] == 0)):
                return True
            elif row+1 >= 0 and row+1 < self._rowlen and col-2 >= 0 and col-2 < self._collen and ((matrix[row+1][col-2] > 6) or (matrix[row+1][col-2] == 0)):
                return True
            elif row-1 >= 0 and row-1 < self._rowlen and col-2 >= 0 and col-2 < self._collen and ((matrix[row-1][col-2] > 6) or (matrix[row-1][col-2] == 0)):
                return True
            elif row-2 >= 0 and row-2 < self._rowlen and col-1 >= 0 and col-1 < self._collen and ((matrix[row-2][col-1] > 6) or (matrix[row-2][col-1] == 0)):
                return True
            else:
                return False
        elif matrix[row][col] == 3:
            if row-1 >= 0 and row-1 < self._rowlen and col+1 >= 0 and col+1 < self._collen and ((matrix[row-1][col+1] > 6) or (matrix[row-1][col+1] == 0)):
                return True
            elif row+1 >= 0 and row+1 < self._rowlen and col+1 >= 0 and col+1 < self._collen and ((matrix[row+1][col+1] > 6) or (matrix[row+1][col+1] == 0)):
                return True
            elif row+1 >= 0 and row+1 < self._rowlen and col-1 >= 0 and col-1 < self._collen and ((matrix[row+1][col-1] > 6) or (matrix[row+1][col-1] == 0)):
                return True
            elif row-1 >= 0 and row-1 < self._rowlen and col-1 >= 0 and col-1 < self._collen and ((matrix[row-1][col-1] > 6) or (matrix[row-1][col-1] == 0)):
                return True
            else:
                return False
        elif matrix[row][col] == 4:
            if row-1 >= 0 and row-1 < self._rowlen and col >= 0 and col < self._collen and ((matrix[row-1][col] > 6) or (matrix[row-1][col] == 0)):
                return True
            elif row >= 0 and row < self._rowlen and col+1 >= 0 and col+1 < self._collen and ((matrix[row][col+1] > 6) or (matrix[row][col+1] == 0)):
                return True
            elif row+1 >= 0 and row+1 < self._rowlen and col >= 0 and col < self._collen and ((matrix[row+1][col] > 6) or (matrix[row+1][col] == 0)):
                return True
            elif row >= 0 and row < self._rowlen and col-1 >= 0 and col-1 < self._collen and ((matrix[row][col-1] > 6) or (matrix[row][col-1] == 0)):
                return True
            else:
                return False
        elif (matrix[row][col] == 5) or (matrix[row][col] == 6):
            if row-1 >= 0 and row-1 < self._rowlen and col >= 0 and col < self._collen and ((matrix[row-1][col] > 6) or (matrix[row-1][col] == 0)):
                return True
            elif row-1 >= 0 and row-1 < self._rowlen and col+1 >= 0 and col+1 < self._collen and ((matrix[row-1][col+1] > 6) or (matrix[row-1][col+1] == 0)):
                return True
            elif row >= 0 and row < self._rowlen and col+1 >= 0 and col+1 < self._collen and ((matrix[row][col+1] > 6) or (matrix[row][col+1] == 0)):
                return True
            elif row+1 >= 0 and row+1 < self._rowlen and col+1 >= 0 and col+1 < self._collen and ((matrix[row+1][col+1] > 6) or (matrix[row+1][col+1] == 0)):
                return True
            elif row+1 >= 0 and row+1 < self._rowlen and col >= 0 and col < self._collen and ((matrix[row+1][col] > 6) or (matrix[row+1][col] == 0)):
                return True
            elif row+1 >= 0 and row+1 < self._rowlen and col-1 >= 0 and col-1 < self._collen and ((matrix[row+1][col-1] > 6) or (matrix[row+1][col-1] == 0)):
                return True
            elif row >= 0 and row < self._rowlen and col-1 >= 0 and col-1 < self._collen and ((matrix[row][col-1] > 6) or (matrix[row][col-1] == 0)):
                return True
            elif row-1 >= 0 and row-1 < self._rowlen and col-1 >= 0 and col-1 < self._collen and ((matrix[row-1][col-1] > 6) or (matrix[row-1][col-1] == 0)):
                return True
            else:
                return False
        elif matrix[row][col] == 7:
            if row-1 >= 0 and row-1 < self._rowlen and col-1 >= 0 and col-1 < self._collen and ((matrix[row-1][col-1] <= 6) and (matrix[row-1][col-1] != 0)):
                return True
            elif row-1 >= 0 and row-1 < self._rowlen and col+1 >= 0 and col+1 < self._collen and ((matrix[row-1][col+1] <= 6) and (matrix[row-1][col+1] != 0)):
                return True
            elif row-1 >= 0 and row-1 < self._rowlen and col >= 0 and col < self._collen and (matrix[row-1][col] == 0):
                return True
            else:
                return False
        elif matrix[row][col] == 8:
            if row-2 >= 0 and row-2 < self._rowlen and col+1 >= 0 and col+1 < self._collen and (matrix[row-2][col+1] <= 6):
                return True
            elif row-1 >= 0 and row-1 < self._rowlen and col+2 >= 0 and col+2 < self._collen and (matrix[row-1][col+2] <= 6):
                return True
            elif row+1 >= 0 and row+1 < self._rowlen and col+2 >= 0 and col+2 < self._collen and (matrix[row+1][col+2] <= 6):
                return True
            elif row+2 >= 0 and row+2 < self._rowlen and col+1 >= 0 and col+1 < self._collen and (matrix[row+2][col+1] <= 6):
                return True
            elif row+2 >= 0 and row+2 < self._rowlen and col-1 >= 0 and col-1 < self._collen and (matrix[row+2][col-1] <= 6):
                return True
            elif row+1 >= 0 and row+1 < self._rowlen and col-2 >= 0 and col-2 < self._collen and (matrix[row+1][col-2] <= 6):
                return True
            elif row-1 >= 0 and row-1 < self._rowlen and col-2 >= 0 and col-2 < self._collen and (matrix[row-1][col-2] <= 6):
                return True
            elif row-2 >= 0 and row-2 < self._rowlen and col-1 >= 0 and col-1 < self._collen and (matrix[row-2][col-1] <= 6):
                return True
            else:
                return False
        elif matrix[row][col] == 9:
            if row-1 >= 0 and row-1 < self._rowlen and col+1 >= 0 and col+1 < self._collen and (matrix[row-1][col+1] <= 6):
                return True
            elif row+1 >= 0 and row+1 < self._rowlen and col+1 >= 0 and col+1 < self._collen and (matrix[row+1][col+1] <= 6):
                return True
            elif row+1 >= 0 and row+1 < self._rowlen and col-1 >= 0 and col-1 < self._collen and (matrix[row+1][col-1] <= 6):
                return True
            elif row-1 >= 0 and row-1 < self._rowlen and col-1 >= 0 and col-1 < self._collen and (matrix[row-1][col-1] <= 6):
                return True
            else:
                return False
        elif matrix[row][col] == 10:
            if row-1 >= 0 and row-1 < self._rowlen and col >= 0 and col < self._collen and (matrix[row-1][col] <= 6):
                return True
            elif row >= 0 and row < self._rowlen and col+1 >= 0 and col+1 < self._collen and (matrix[row][col+1] <= 6):
                return True
            elif row+1 >= 0 and row+1 < self._rowlen and col >= 0 and col < self._collen and (matrix[row+1][col] <= 6):
                return True
            elif row >= 0 and row < self._rowlen and col-1 >= 0 and col-1 < self._collen and (matrix[row][col-1] <= 6):
                return True
            else:
                return False
        elif (matrix[row][col] == 11) or (matrix[row][col] == 12):
            if row-1 >= 0 and row-1 < self._rowlen and col >= 0 and col < self._collen and (matrix[row-1][col] <= 6):
                return True
            elif row-1 >= 0 and row-1 < self._rowlen and col+1 >= 0 and col+1 < self._collen and (matrix[row-1][col+1] <= 6):
                return True
            elif row >= 0 and row < self._rowlen and col+1 >= 0 and col+1 < self._collen and (matrix[row][col+1] <= 6):
                return True
            elif row+1 >= 0 and row+1 < self._rowlen and col+1 >= 0 and col+1 < self._collen and (matrix[row+1][col+1] <= 6):
                return True
            elif row+1 >= 0 and row+1 < self._rowlen and col >= 0 and col < self._collen and (matrix[row+1][col] <= 6):
                return True
            elif row+1 >= 0 and row+1 < self._rowlen and col-1 >= 0 and col-1 < self._collen and (matrix[row+1][col-1] <= 6):
                return True
            elif row >= 0 and row < self._rowlen and col-1 >= 0 and col-1 < self._collen and (matrix[row][col-1] <= 6):
                return True
            elif row-1 >= 0 and row-1 < self._rowlen and col-1 >= 0 and col-1 < self._collen and (matrix[row-1][col-1] <= 6):
                return True
            else:
                return False
        return False

    # make the nodes by checking
    def _make_node(self, pos, only_move, pawn_change):
        if not only_move and not self.__check_bool(pos):
            return [*pos, pawn_change]
        else:
            if (pos[2], pos[3]) in only_move:
                if not self.__check_bool(pos):
                    return [*pos, pawn_change]
    
    # it checks that after mive does the king have check or not an return True or False
    def __check_bool(self, pos):
        old_row, old_col, new_row, new_col = pos
        kr, kc = self.__king
        check = False
        
        # played the move
        kill = self.__matrix[new_row][new_col]
        self.__matrix[new_row][new_col] = self.__matrix[old_row][old_col]
        self.__matrix[old_row][old_col] = 0
        
        # check the current side
        if self.__matrix[kr][kc] == 6:
            for x in self.__enemy:
                r, c = x
                steps = []
                if self.__matrix[r][c] == 7:
                    if r - 1 == kr and c - 1 == kc:
                        check = True
                    elif r - 1 == kr and c + 1 == kc:
                        check = True
                elif self.__matrix[r][c] == 8:
                    if (abs(r - kr) == 1 and abs(c - kc) == 2) or (abs(r - kr) == 2 and abs(c - kc) == 1):
                        check = True
                elif self.__matrix[r][c] == 9:
                    if kr - r == kc - c > 0:
                        steps = [1, 1]
                    elif r - kr == kc - c > 0:
                        steps = [-1, 1]
                    elif kr - r == c - kc > 0:
                        steps = [1, -1]
                    elif r - kr == c - kc > 0:
                        steps = [-1, -1]
                elif self.__matrix[r][c] == 10:
                    if r == kr and c < kc:
                        steps = [0, 1]
                    elif r == kr and c > kc:
                        steps = [0, -1]
                    elif r < kr and c == kc:
                        steps = [1, 0]
                    elif r > kr and c == kc:
                        steps = [-1, 0]
                elif self.__matrix[r][c] == 11:
                    if kr - r == kc - c > 0:
                        steps = [1, 1]
                    elif r - kr == kc - c > 0:
                        steps = [-1, 1]
                    elif kr - r == c - kc > 0:
                        steps = [1, -1]
                    elif r - kr == c - kc > 0:
                        steps = [-1, -1]
                    elif r == kr and c < kc:
                        steps = [0, 1]
                    elif r == kr and c > kc:
                        steps = [0, -1]
                    elif r < kr and c == kc:
                        steps = [1, 0]
                    elif r > kr and c == kc:
                        steps = [-1, 0]
                elif self.__matrix[r][c] == 12:
                    continue
                else:
                    continue
                # Sliding pieces: Bishop, Rook, Queen
                if len(steps) == 2:
                    row = r + steps[0]
                    col = c + steps[1]
                    while 0 <= row < self._rowlen and 0 <= col < self._collen:
                        if self.__matrix[row][col] == 0:
                            row += steps[0]
                            col += steps[1]
                        elif self.__matrix[row][col] == 6:
                            check = True
                            break
                        else:
                            break
                if check:
                    break
        elif self.__matrix[kr][kc] == 12:
            for x in self.__enemy:
                r, c = x
                steps = []
                if self.__matrix[r][c] == 1:
                    if r + 1 == kr and c - 1 == kc:
                        check = True
                    elif r + 1 == kr and c + 1 == kc:
                        check = True
                elif self.__matrix[r][c] == 2:
                    if (abs(r - kr) == 1 and abs(c - kc) == 2) or (abs(r - kr) == 2 and abs(c - kc) == 1):
                        check = True
                elif self.__matrix[r][c] == 3:
                    if kr - r == kc - c > 0:
                        steps = [1, 1]
                    elif r - kr == kc - c > 0:
                        steps = [-1, 1]
                    elif kr - r == c - kc > 0:
                        steps = [1, -1]
                    elif r - kr == c - kc > 0:
                        steps = [-1, -1]
                elif self.__matrix[r][c] == 4:
                    if r == kr and c < kc:
                        steps = [0, 1]
                    elif r == kr and c > kc:
                        steps = [0, -1]
                    elif r < kr and c == kc:
                        steps = [1, 0]
                    elif r > kr and c == kc:
                        steps = [-1, 0]
                elif self.__matrix[r][c] == 5:
                    if kr - r == kc - c > 0:
                        steps = [1, 1]
                    elif r - kr == kc - c > 0:
                        steps = [-1, 1]
                    elif kr - r == c - kc > 0:
                        steps = [1, -1]
                    elif r - kr == c - kc > 0:
                        steps = [-1, -1]
                    elif r == kr and c < kc:
                        steps = [0, 1]
                    elif r == kr and c > kc:
                        steps = [0, -1]
                    elif r < kr and c == kc:
                        steps = [1, 0]
                    elif r > kr and c == kc:
                        steps = [-1, 0]
                elif self.__matrix[r][c] == 6:
                    continue
                else:
                    continue
                # Sliding pieces: Bishop, Rook, Queen
                if len(steps) == 2:
                    row = r + steps[0]
                    col = c + steps[1]
                    while 0 <= row < self._rowlen and 0 <= col < self._collen:
                        if self.__matrix[row][col] == 0:
                            row += steps[0]
                            col += steps[1]
                        elif self.__matrix[row][col] == 12:
                            check = True
                            break
                        else:
                            break
                if check:
                    break
        
        # reverse the play
        self.__matrix[old_row][old_col] = self.__matrix[new_row][new_col]
        self.__matrix[new_row][new_col] = kill
        return check

class BotChessman(__MatrixOperation):
    __check = []
    # constructor
    def __init__(self, chessboard_info):
        self.__matrix = chessboard_info["matrix"]
        self.__player = chessboard_info["player"]
        self.__bot = chessboard_info["bot"]
        self.__king = chessboard_info["bot_king"]
        self.__castle = chessboard_info["castling"]["bot"]
        self._rowlen = len(chessboard_info["matrix"])
        self._collen = len(chessboard_info["matrix"][0])
        self._current_matrix(self.__matrix, self.__king, self.__player)
        
    # inner moves of chessman
    def _slide(self, row, col, dr, dc):
        list1 = []
        r = row + dr
        c = col + dc
        while 0 <= r < self._rowlen and 0 <= c < self._collen:
            if self.__matrix[r][c] == 0:
                if (node := self._make_node([row, col, r, c], self.__check, None)) is not None: list1.append(node)
            elif self.__matrix[r][c] >= 7:
                if (node := self._make_node([row, col, r, c], self.__check, None)) is not None: list1.append(node)
                break
            else:
                break
            r += dr
            c += dc
        return list1
    
    # check where king cannot move
    def _filterEnemy(self, arg):
        enemy, row, col = arg
        if self.__matrix[enemy[0]][enemy[1]] == 7:
            if enemy[0] == row and enemy[1] == col-2:
                return [1]
            elif enemy[0] == row and enemy[1] == col-1:
                return [2]
            elif enemy[0] == row and enemy[1] == col+1:
                return [2]
            elif enemy[0] == row and enemy[1] == col+2:
                return [3]
            elif enemy[0] == row+1 and enemy[1] == col-2:
                return [4]
            elif enemy[0] == row+1 and enemy[1] == col:
                return [4, 5]
            elif enemy[0] == row+1 and enemy[1] == col+2:
                return [5]
            elif enemy[0] == row+2 and enemy[1] == col-2:
                return [6]
            elif enemy[0] == row+2 and enemy[1] == col-1:
                return [7]
            elif enemy[0] == row+2 and enemy[1] == col:
                return [6, 8]
            elif enemy[0] == row+2 and enemy[1] == col+1:
                return [7]
            elif enemy[0] == row+2 and enemy[1] == col+2:
                return [8]
        elif self.__matrix[enemy[0]][enemy[1]] == 8:
            if (enemy[0] == (row-3) and enemy[1] == (col-2)):
                return [1]
            elif (enemy[0] == (row-3) and enemy[1] == (col-1)):
                return [2]
            elif (enemy[0] == (row-3) and enemy[1] == (col)):
                return [1, 3]
            elif (enemy[0] == (row-3) and enemy[1] == (col+1)):
                return [2]
            elif (enemy[0] == (row-3) and enemy[1] == (col+2)):
                return [3]
            elif (enemy[0] == (row-2) and enemy[1] == (col-3)):
                return [1]
            elif (enemy[0] == (row-2) and enemy[1] == (col-2)):
                return [2, 4]
            elif (enemy[0] == (row-2) and enemy[1] == (col-1)):
                return [3]
            elif (enemy[0] == (row-2) and enemy[1] == (col)):
                return [4, 5]
            elif (enemy[0] == (row-2) and enemy[1] == (col+1)):
                return [1]
            elif (enemy[0] == (row-2) and enemy[1] == (col+2)):
                return [2, 5]
            elif (enemy[0] == (row-2) and enemy[1] == (col+3)):
                return [3]
            elif (enemy[0] == (row-1) and enemy[1] == (col-3)):
                return [4]
            elif (enemy[0] == (row-1) and enemy[1] == (col-2)):
                return [6]
            elif (enemy[0] == (row-1) and enemy[1] == (col-1)):
                return [5, 7]
            elif (enemy[0] == (row-1) and enemy[1] == (col)):
                return [6, 8]
            elif (enemy[0] == (row-1) and enemy[1] == (col+1)):
                return [4, 7]
            elif (enemy[0] == (row-1) and enemy[1] == (col+2)):
                return [8]
            elif (enemy[0] == (row-1) and enemy[1] == (col+3)):
                return [5]
            elif (enemy[0] == (row) and enemy[1] == (col-3)):
                return [1, 6]
            elif (enemy[0] == (row) and enemy[1] == (col-2)):
                return [2, 7]
            elif (enemy[0] == (row) and enemy[1] == (col-1)):
                return [3, 8]
            elif (enemy[0] == (row) and enemy[1] == (col+1)):
                return [1, 6]
            elif (enemy[0] == (row) and enemy[1] == (col+2)):
                return [2, 7]
            elif (enemy[0] == (row) and enemy[1] == (col+3)):
                return [3, 8]
            elif (enemy[0] == (row+1) and enemy[1] == (col-3)):
                return [4]
            elif (enemy[0] == (row+1) and enemy[1] == (col-2)):
                return [1]
            elif (enemy[0] == (row+1) and enemy[1] == (col-1)):
                return [2, 5]
            elif (enemy[0] == (row+1) and enemy[1] == (col)):
                return [1, 3]
            elif (enemy[0] == (row+1) and enemy[1] == (col+1)):
                return [2, 4]
            elif (enemy[0] == (row+1) and enemy[1] == (col+2)):
                return [3]
            elif (enemy[0] == (row+1) and enemy[1] == (col+3)):
                return [5]
            elif (enemy[0] == (row+2) and enemy[1] == (col-3)):
                return [6]
            elif (enemy[0] == (row+2) and enemy[1] == (col-2)):
                return [4, 7]
            elif (enemy[0] == (row+2) and enemy[1] == (col-1)):
                return [8]
            elif (enemy[0] == (row+2) and enemy[1] == (col)):
                return [4, 5]
            elif (enemy[0] == (row+2) and enemy[1] == (col+1)):
                return [6]
            elif (enemy[0] == (row+2) and enemy[1] == (col+2)):
                return [5, 7]
            elif (enemy[0] == (row+2) and enemy[1] == (col+3)):
                return [8]
            elif (enemy[0] == (row+3) and enemy[1] == (col-2)):
                return [6]
            elif (enemy[0] == (row+3) and enemy[1] == (col-1)):
                return [7]
            elif (enemy[0] == (row+3) and enemy[1] == (col)):
                return [6, 8]
            elif (enemy[0] == (row+3) and enemy[1] == (col+1)):
                return [7]
            elif (enemy[0] == (row+3) and enemy[1] == (col+2)):
                return [8]
        elif self.__matrix[enemy[0]][enemy[1]] == 9:
            if enemy[0] == (row+2) and enemy[1] == col:
                return [6, 8]
            elif (enemy[0] == (row+1) and enemy[1] == col) or (enemy[0] == (row-1) and enemy[1] == col):
                return [4, 5]
            elif enemy[0] == (row-2) and enemy[1] == col:
                return [1, 3]
            elif enemy[0] == row and enemy[1] == (col+2):
                return [3, 8]
            elif (enemy[0] == row and enemy[1] == (col+1)) or (enemy[0] == row and enemy[1] == (col-1)):
                return [2, 7]
            elif enemy[0] == row and enemy[1] == (col-2):
                return [1, 6]
            else:
                if enemy[0] != (row-1) and enemy[1] != (col-1) and abs(enemy[0]-(row-1)) == abs(enemy[1]-(col-1)):
                    if enemy[0] != (row+1) and enemy[1] != (col+1) and abs(enemy[0]-(row+1)) == abs(enemy[1]-(col+1)):
                        if enemy[0] < (row-1) and enemy[1] < (col-1):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]+x][enemy[1]+x] != 0:
                                    return None
                            if self.__matrix[row-1][col-1] != 0:
                                return [1]
                        elif enemy[0] > (row+1) and enemy[1] > (col+1):
                            for x in range(1, abs(enemy[0]-(row+1))):
                                if self.__matrix[enemy[0]-x][enemy[1]-x] != 0:
                                    return None
                            if self.__matrix[row+1][col+1] != 0:
                                return [8]
                        return [1, 8]
                    else:
                        if enemy[0] < (row-1) and enemy[1] > (col-1):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]+x][enemy[1]-x] != 0:
                                    return None
                        elif enemy[0] > (row-1) and enemy[1] < (col-1):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]-x][enemy[1]+x] != 0:
                                    return None
                        return [1]
                elif enemy[0] != (row-1) and enemy[1] != (col) and abs(enemy[0]-(row-1)) == abs(enemy[1]-(col)):
                    if enemy[0] != (row) and enemy[1] != (col+1) and abs(enemy[0]-(row)) == abs(enemy[1]-(col+1)):
                        if enemy[0] < (row-1) and enemy[1] < (col):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]+x][enemy[1]+x] != 0:
                                    return None
                            if self.__matrix[row-1][col] != 0:
                                return [2]
                        elif enemy[0] > (row) and enemy[1] > (col+1):
                            for x in range(1, abs(enemy[0]-row)):
                                if self.__matrix[enemy[0]-x][enemy[1]-x] != 0:
                                    return None
                            if self.__matrix[row][col+1] != 0:
                                return [5]
                        return [2, 5]
                    elif enemy[0] != (row) and enemy[1] != (col-1) and abs(enemy[0]-(row)) == abs(enemy[1]-(col-1)):
                        if enemy[0] < (row-1) and enemy[1] > (col):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]+x][enemy[1]-x] != 0:
                                    return None
                            if self.__matrix[row-1][col] != 0:
                                return [2]
                        elif enemy[0] > (row) and enemy[1] < (col-1):
                            for x in range(1, abs(enemy[0]-row)):
                                if self.__matrix[enemy[0]-x][enemy[1]+x] != 0:
                                    return None
                            if self.__matrix[row][col-1] != 0:
                                return [4]
                        return [2, 4]
                elif enemy[0] != (row-1) and enemy[1] != (col+1) and abs(enemy[0]-(row-1)) == abs(enemy[1]-(col+1)):
                    if enemy[0] != (row+1) and enemy[1] != (col-1) and abs(enemy[0]-(row+1)) == abs(enemy[1]-(col-1)):
                        if enemy[0] < (row-1) and enemy[1] > (col+1):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]+x][enemy[1]-x] != 0:
                                    return None
                            if self.__matrix[row-1][col+1] != 0:
                                return [3]
                        elif enemy[0] > (row+1) and enemy[1] < (col-1):
                            for x in range(1, abs(enemy[0]-(row+1))):
                                if self.__matrix[enemy[0]-x][enemy[1]+x] != 0:
                                    return None
                            if self.__matrix[row+1][col-1] != 0:
                                return [6]
                        return [3, 6]
                    else:
                        if enemy[0] < (row-1) and enemy[1] < (col+1):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]+x][enemy[1]+x] != 0:
                                    return None
                        elif enemy[0] > (row-1) and enemy[1] > (col+1):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]-x][enemy[1]-x] != 0:
                                    return None
                        return [3]
                elif enemy[0] != (row) and enemy[1] != (col-1) and abs(enemy[0]-(row)) == abs(enemy[1]-(col-1)):
                    if enemy[0] != (row+1) and enemy[1] != (col) and abs(enemy[0]-(row+1)) == abs(enemy[1]-(col)):
                        if enemy[0] < (row) and enemy[1] < (col-1):
                            for x in range(1, abs(enemy[0]-row)):
                                if self.__matrix[enemy[0]+x][enemy[1]+x] != 0:
                                    return None
                            if self.__matrix[row-1][col] != 0:
                                return [4]
                        elif enemy[0] > (row+1) and enemy[1] > (col):
                            for x in range(1, abs(enemy[0]-row)):
                                if self.__matrix[enemy[0]-x][enemy[1]-x] != 0:
                                    return None
                            if self.__matrix[row+1][col] != 0:
                                return [7]
                        return [4, 7]
                elif enemy[0] != (row) and enemy[1] != (col+1) and abs(enemy[0]-(row)) == abs(enemy[1]-(col+1)):
                    if enemy[0] != (row+1) and enemy[1] != (col) and abs(enemy[0]-(row+1)) == abs(enemy[1]-(col)):
                        if enemy[0] < (row) and enemy[1] > (col+1):
                            for x in range(1, abs(enemy[0]-row)):
                                if self.__matrix[enemy[0]+x][enemy[1]-x] != 0:
                                    return None
                            if self.__matrix[row][col+1] != 0:
                                return [5]
                        elif enemy[0] > (row+1) and enemy[1] < (col):
                            for x in range(1, abs(enemy[0]-row)):
                                if self.__matrix[enemy[0]-x][enemy[1]+x] != 0:
                                    return None
                            if self.__matrix[row+1][col] != 0:
                                return [7]
                        return [5, 7]
                elif enemy[0] != (row+1) and enemy[1] != (col-1) and abs(enemy[0]-(row+1)) == abs(enemy[1]-(col-1)):
                    if enemy[0] < (row+1) and enemy[1] < (col-1):
                        for x in range(1, abs(enemy[0]-(row+1))):
                            if self.__matrix[enemy[0]+x][enemy[1]+x] != 0:
                                return None
                    elif enemy[0] > (row+1) and enemy[1] > (col-1):
                        for x in range(1, abs(enemy[0]-(row+1))):
                            if self.__matrix[enemy[0]-x][enemy[1]-x] != 0:
                                return None
                    return [6]
                elif enemy[0] != (row+1) and enemy[1] != (col+1) and abs(enemy[0]-(row+1)) == abs(enemy[1]-(col+1)):
                    if enemy[0] < (row+1) and enemy[1] > (col+1):
                        for x in range(1, abs(enemy[0]-(row+1))):
                            if self.__matrix[enemy[0]+x][enemy[1]-x] != 0:
                                return None
                    elif enemy[0] > (row+1) and enemy[1] < (col+1):
                        for x in range(1, abs(enemy[0]-(row+1))):
                            if self.__matrix[enemy[0]-x][enemy[1]+x] != 0:
                                return None
                    return [8]
        elif self.__matrix[enemy[0]][enemy[1]] == 10:
            if enemy[0] == row-1 and enemy[1] == col-1:
                if self.__matrix[row][col-1] != 0 and self.__matrix[row-1][col] != 0:
                    return [2, 4]
                elif self.__matrix[row][col-1] == 0 and self.__matrix[row-1][col] != 0:
                    return [2, 4, 6]
                elif self.__matrix[row][col-1] != 0 and self.__matrix[row-1][col] == 0:
                    return [2, 3, 4]
                else:
                    return [2, 3, 4, 6]
            elif enemy[0] == row-1 and enemy[1] == col:
                return [1, 3, 7]
            elif enemy[0] == row-1 and enemy[1] == col+1:
                if self.__matrix[row][col+1] != 0 and self.__matrix[row-1][col] != 0:
                    return [2, 5]
                elif self.__matrix[row][col+1] == 0 and self.__matrix[row-1][col] != 0:
                    return [2, 5, 8]
                elif self.__matrix[row][col+1] != 0 and self.__matrix[row-1][col] == 0:
                    return [1, 2, 5]
                else:
                    return [1, 2, 5, 8]
            elif enemy[0] == row and enemy[1] == col-1:
                return [1, 5, 6]
            elif enemy[0] == row and enemy[1] == col+1:
                return [3, 4, 8]
            elif enemy[0] == row+1 and enemy[1] == col-1:
                if self.__matrix[row][col-1] != 0 and self.__matrix[row+1][col] != 0:
                    return [4, 7]
                elif self.__matrix[row][col-1] == 0 and self.__matrix[row+1][col] != 0:
                    return [1, 4, 7]
                elif self.__matrix[row][col-1] != 0 and self.__matrix[row+1][col] == 0:
                    return [4, 7, 8]
                else:
                    return [1, 4, 7, 8]
            elif enemy[0] == row+1 and enemy[1] == col:
                return [2, 6, 8]
            elif enemy[0] == row+1 and enemy[1] == col+1:
                if self.__matrix[row][col+1] != 0 and self.__matrix[row+1][col] != 0:
                    return [5, 7]
                elif self.__matrix[row][col+1] == 0 and self.__matrix[row+1][col] != 0:
                    return [3, 5, 7]
                elif self.__matrix[row][col+1] != 0 and self.__matrix[row+1][col] == 0:
                    return [5, 6, 7]
                else:
                    return [3, 5, 6, 7]
            else:
                if enemy[0] == row-1:
                    if  enemy[1] < col-1:
                        for x in range(enemy[1]+1, col-1):
                            if self.__matrix[row-1][x] != 0:
                                return None
                        if self.__matrix[row-1][col-1] != 0:
                            return [1]
                        elif self.__matrix[row-1][col] != 0:
                            return [1, 2]
                    elif enemy[1] > col+1:
                        for x in range(col+2, enemy[1]):
                            if self.__matrix[row-1][x] != 0:
                                return None
                        if self.__matrix[row-1][col+1] != 0:
                            return [3]
                        elif self.__matrix[row-1][col] != 0:
                            return [2, 3]
                    return [1, 2, 3]
                elif enemy[0] == row:
                    if  enemy[1] < col-1:
                        for x in range(enemy[1]+1, col-1):
                            if self.__matrix[row][x] != 0:
                                return None
                        if self.__matrix[row][col-1] != 0:
                            return [4]
                    elif enemy[1] > col+1:
                        for x in range(col+2, enemy[1]):
                            if self.__matrix[row][x] != 0:
                                return None
                        if self.__matrix[row][col+1] != 0:
                            return [5]
                    return [4, 5]
                elif enemy[0] == row+1:
                    if enemy[1] < col-1:
                        for x in range(enemy[1]+1, col-1):
                            if self.__matrix[row+1][x] != 0:
                                return None
                        if self.__matrix[row+1][col-1] != 0:
                            return [6]
                        elif self.__matrix[row+1][col] != 0:
                            return [6, 7]
                    elif enemy[1] > col+1:
                        for x in range(col+2, enemy[1]):
                            if self.__matrix[row+1][x] != 0:
                                return None
                        if self.__matrix[row+1][col+1] != 0:
                            return [8]
                        elif self.__matrix[row+1][col] != 0:
                            return [7, 8]
                    return [6, 7, 8]
                elif enemy[1] == col-1:
                    if enemy[0] < row-1:
                        for x in range(enemy[0]+1, row-1):
                            if self.__matrix[x][col-1] != 0:
                                return None
                        if self.__matrix[row-1][col-1] != 0:
                            return [1]
                        elif self.__matrix[row][col-1] != 0:
                            return [1, 4]
                    elif enemy[0] > row+1:
                        for x in range(row+2, enemy[0]):
                            if self.__matrix[x][col-1] != 0:
                                return None
                        if self.__matrix[row+1][col-1] != 0:
                            return [6]
                        elif self.__matrix[row][col-1] != 0:
                            return [4, 6]
                    return [1, 4, 6]
                elif enemy[1] == col:
                    if enemy[0] < row-1:
                        for x in range(enemy[0]+1, row-1):
                            if self.__matrix[x][col] != 0:
                                return None
                        if self.__matrix[row-1][col] != 0:
                            return [2]
                    elif enemy[0] > row+1:
                        for x in range(row+2, enemy[0]):
                            if self.__matrix[x][col] != 0:
                                return None
                        if self.__matrix[row+1][col] != 0:
                            return [7]
                    return [2, 7]
                elif enemy[1] == col+1:
                    if enemy[0] < row-1:
                        for x in range(enemy[0]+1, row-1):
                            if self.__matrix[x][col+1] != 0:
                                return None
                        if self.__matrix[row-1][col+1] != 0:
                            return [3]
                        elif self.__matrix[row][col+1] != 0:
                            return [3, 5]
                    elif enemy[0] > row+1:
                        for x in range(row+2, enemy[0]):
                            if self.__matrix[x][col+1] != 0:
                                return None
                        if self.__matrix[row+1][col+1] != 0:
                            return [8]
                        elif self.__matrix[row][col+1] != 0:
                            return [5, 8]
                    return [3, 5, 8]
        elif self.__matrix[enemy[0]][enemy[1]] == 11:
            if enemy[0] == row-1 and enemy[1] == col-1:
                if self.__matrix[row-1][col] != 0 and self.__matrix[row][col-1] != 0:
                    return [2, 4, 8]
                elif self.__matrix[row-1][col] != 0 and self.__matrix[row][col-1] == 0:
                    return [2, 4, 6, 8]
                elif self.__matrix[row-1][col] == 0 and self.__matrix[row][col-1] != 0:
                    return [2, 3, 4, 8]
                else:
                    return [2, 3, 4, 6, 8]
            elif enemy[0] == row-1 and enemy[1] == col:
                return [1, 3, 4, 5, 7]
            elif enemy[0] == row-1 and enemy[1] == col+1:
                if self.__matrix[row-1][col] != 0 and self.__matrix[row][col+1] != 0:
                    return [2, 5, 6]
                elif self.__matrix[row-1][col] != 0 and self.__matrix[row][col+1] == 0:
                    return [2, 5, 6, 8]
                elif self.__matrix[row-1][col] == 0 and self.__matrix[row][col+1] != 0:
                    return [1, 2, 5, 6]
                else:
                    return [1, 2, 5, 6, 8]
            elif enemy[0] == row and enemy[1] == col-1:
                return [1, 2, 5, 6, 7]
            elif enemy[0] == row and enemy[1] == col+1:
                return [2, 3, 4, 7, 8]
            elif enemy[0] == row+1 and enemy[1] == col-1:
                if self.__matrix[row+1][col] != 0 and self.__matrix[row][col-1] != 0:
                    return [3, 4, 7]
                elif self.__matrix[row+1][col] != 0 and self.__matrix[row][col-1] == 0:
                    return [1, 3, 4, 7]
                elif self.__matrix[row+1][col] == 0 and self.__matrix[row][col-1] != 0:
                    return [3, 4, 7, 8]
                else:
                    return [1, 3, 4, 7, 8]
            elif enemy[0] == row+1 and enemy[1] == col:
                return [2, 4, 5, 6, 8]
            elif enemy[0] == row+1 and enemy[1] == col+1:
                if self.__matrix[row+1][col] != 0 and self.__matrix[row][col+1] != 0:
                    return [1, 5, 7]
                elif self.__matrix[row+1][col] != 0 and self.__matrix[row][col+1] == 0:
                    return [1, 3, 5, 7]
                elif self.__matrix[row+1][col] == 0 and self.__matrix[row][col+1] != 0:
                    return [1, 5, 6, 7]
                else:
                    return [1, 3, 5, 6, 7]
            elif enemy[0] == row-2 and enemy[1] == col-1:
                if self.__matrix[row-1][col-1] != 0 and self.__matrix[row-1][col] != 0:
                    return [1, 2]
                elif self.__matrix[row-1][col-1] != 0 and self.__matrix[row-1][col] == 0:
                    return [1, 2, 5]
                elif self.__matrix[row][col-1] != 0 and self.__matrix[row-1][col] != 0:
                    return [1, 2, 4]
                elif self.__matrix[row][col-1] != 0 and self.__matrix[row-1][col] != 0:
                    return [1, 2, 4, 5]
                elif self.__matrix[row-1][col] != 0 and self.__matrix[row][col-1] == 0:
                    return [1, 2, 4, 6]
                else:
                    return [1, 2, 4, 5, 6]
            elif enemy[0] == row-2 and enemy[1] == col:
                if self.__matrix[row-1][col] != 0:
                    return [1, 2, 3]
                else:
                    return [1, 2, 3, 7]
            elif enemy[0] == row-2 and enemy[1] == col+1:
                if self.__matrix[row-1][col+1] != 0 and self.__matrix[row-1][col] != 0:
                    return [2, 3]
                elif self.__matrix[row-1][col+1] != 0 and self.__matrix[row-1][col] == 0:
                    return [2, 3, 4]
                elif self.__matrix[row][col+1] != 0 and self.__matrix[row-1][col] != 0:
                    return [2, 3, 5]
                elif self.__matrix[row][col+1] != 0 and self.__matrix[row-1][col] == 0:
                    return [2, 3, 4, 5]
                elif self.__matrix[row-1][col] != 0 and self.__matrix[row][col+1] == 0:
                    return [2, 3, 5, 8]
                else:
                    return [2, 3, 4, 5, 8]
            elif enemy[0] == row-1 and enemy[1] == col-2:
                if self.__matrix[row-1][col-1] != 0 and self.__matrix[row][col-1] != 0:
                    return [1, 4]
                elif self.__matrix[row-1][col-1] != 0 and self.__matrix[row][col-1] == 0:
                    return [1, 4, 7]
                elif self.__matrix[row-1][col] != 0 and self.__matrix[row][col-1] != 0:
                    return [1, 2, 4]
                elif self.__matrix[row-1][col] != 0 and self.__matrix[row][col-1] == 0:
                    return [1, 2, 4, 7]
                elif self.__matrix[row][col-1] != 0 and self.__matrix[row-1][col] == 0:
                    return [1, 2, 3, 4]
                else:
                    return [1, 2, 3, 4, 7]
            elif enemy[0] == row and enemy[1] == col-2:
                if self.__matrix[row][col-1] != 0:
                    return [1, 4, 6]
                else:
                    return [1, 4, 5, 6]
            elif enemy[0] == row+1 and enemy[1] == col-2:
                if self.__matrix[row+1][col-1] != 0 and self.__matrix[row][col-1] != 0:
                    return [4, 6]
                elif self.__matrix[row+1][col-1] != 0 and self.__matrix[row][col-1] == 0:
                    return [2, 4, 6]
                elif self.__matrix[row+1][col] != 0 and self.__matrix[row][col-1] != 0:
                    return [4, 6, 7]
                elif self.__matrix[row+1][col] != 0 and self.__matrix[row][col-1] == 0:
                    return [2, 4, 6, 7]
                elif self.__matrix[row][col-1] != 0 and self.__matrix[row+1][col] == 0 :
                    return [4, 6, 7, 8]
                else:
                    return [2, 4, 6, 7, 8]
            elif enemy[0] == row+2 and enemy[1] == col-1:
                if self.__matrix[row+1][col-1] != 0 and self.__matrix[row+1][col] != 0:
                    return [6, 7]
                elif self.__matrix[row+1][col-1] != 0 and self.__matrix[row+1][col] == 0:
                    return [5, 6, 7]
                elif self.__matrix[row][col-1] != 0 and self.__matrix[row+1][col] != 0:
                    return [4, 6, 7]
                elif self.__matrix[row][col-1] == 0 and self.__matrix[row+1][col] != 0:
                    return [1, 4, 6, 7]
                elif self.__matrix[row][col-1] != 0 and self.__matrix[row+1][col] == 0:
                    return [4, 5, 6, 7]
                else:
                    return [1, 4, 5, 6, 7]
            elif enemy[0] == row+2 and enemy[1] == col:
                if self.__matrix[row+1][col] != 0:
                    return [6, 7, 8]
                else:
                    return [2, 6, 7, 8]
            elif enemy[0] == row+2 and enemy[1] == col+1:
                if self.__matrix[row+1][col+1] != 0 and self.__matrix[row+1][col] != 0:
                    return [7, 8]
                elif self.__matrix[row+1][col+1] != 0 and self.__matrix[row+1][col] == 0:
                    return [4, 7, 8]
                elif self.__matrix[row][col+1] != 0 and self.__matrix[row+1][col] != 0:
                    return [5, 7, 8]
                elif self.__matrix[row][col+1] == 0 and self.__matrix[row+1][col] != 0:
                    return [3, 5, 7, 8]
                elif self.__matrix[row][col+1] != 0 and self.__matrix[row+1][col] == 0:
                    return [4, 5, 7, 8]
                else:
                    return [3, 4, 5, 7, 8]
            elif enemy[0] == row-1 and enemy[1] == col+2:
                if self.__matrix[row-1][col+1] != 0 and self.__matrix[row][col+1] != 0:
                    return [3, 5]
                elif self.__matrix[row-1][col+1] != 0 and self.__matrix[row][col+1] == 0:
                    return [3, 5, 7]
                elif self.__matrix[row-1][col] != 0 and self.__matrix[row][col+1] != 0:
                    return [2, 3, 5]
                elif self.__matrix[row-1][col] != 0 and self.__matrix[row][col+1] == 0:
                    return [2, 3, 5, 7]
                elif self.__matrix[row-1][col] == 0 and self.__matrix[row][col+1] != 0:
                    return [1, 2, 3, 5]
                else:
                    return [1, 2, 3, 5, 7]
            elif enemy[0] == row and enemy[1] == col+2:
                if self.__matrix[row][col+1] != 0:
                    return [3, 5, 8]
                else:
                    return [3, 4, 5, 8]
            elif enemy[0] == row+1 and enemy[1] == col+2:
                if self.__matrix[row+1][col+1] != 0 and self.__matrix[row][col+1] != 0:
                    return [5, 8]
                elif self.__matrix[row+1][col+1] != 0 and self.__matrix[row][col+1] == 0:
                    return [2, 5, 8]
                elif self.__matrix[row+1][col] != 0 and self.__matrix[row][col+1] != 0:
                    return [5, 7, 8]
                elif self.__matrix[row+1][col] != 0 and self.__matrix[row][col+1] == 0:
                    return [2, 5, 7, 8]
                elif self.__matrix[row+1][col] == 0 and self.__matrix[row][col+1] != 0:
                    return [5, 6, 7, 8]
                else:
                    return [2, 5, 6, 7, 8]
            elif enemy[0] == row-3 and enemy[1] == col-1:
                if self.__matrix[row-2][col-1] != 0 and self.__matrix[row-2][col] != 0:
                    return None
                elif self.__matrix[row-2][col-1] != 0 and self.__matrix[row-2][col] == 0:
                    return [3]
                elif self.__matrix[row-1][col-1] != 0 and self.__matrix[row-2][col] != 0:
                    return [1]
                elif self.__matrix[row-1][col-1] != 0 and self.__matrix[row-2][col] == 0:
                    return [1, 3]
                elif self.__matrix[row][col-1] != 0 and self.__matrix[row-2][col] != 0:
                    return [1, 4]
                elif self.__matrix[row][col-1] != 0 and self.__matrix[row-2][col] == 0:
                    return [1, 4, 3]
                elif self.__matrix[row-2][col] != 0:
                    return [1, 4, 6]
                else:
                    return [1, 3, 4, 6]
            elif enemy[0] == row-3 and enemy[1] == col:
                if self.__matrix[row-2][col] != 0:
                    return None
                elif self.__matrix[row-1][col] != 0:
                    return [2]
                else:
                    return [2, 7]
            elif enemy[0] == row-3 and enemy[1] == col+1:
                if self.__matrix[row-2][col+1] != 0 and self.__matrix[row-2][col] != 0:
                    return None
                elif self.__matrix[row-2][col+1] != 0 and self.__matrix[row-2][col] == 0:
                    return [1]
                elif self.__matrix[row-1][col+1] != 0 and self.__matrix[row-2][col] != 0:
                    return [3]
                elif self.__matrix[row-1][col+1] != 0 and self.__matrix[row-2][col] == 0:
                    return [1, 3]
                elif self.__matrix[row][col+1] != 0 and self.__matrix[row-2][col] != 0:
                    return [3, 5]
                elif self.__matrix[row][col+1] != 0 and self.__matrix[row-2][col] == 0:
                    return [1, 3, 5]
                elif self.__matrix[row-2][col] != 0:
                    return [3, 5, 8]
                else:
                    return [1, 3, 5, 8]
            elif enemy[0] == row-1 and enemy[1] == col-3:
                if self.__matrix[row-1][col-2] != 0 and self.__matrix[row][col-2] != 0:
                    return None
                elif self.__matrix[row-1][col-2] != 0 and self.__matrix[row][col-2] == 0:
                    return [6]
                elif self.__matrix[row-1][col-1] != 0 and self.__matrix[row][col-2] != 0:
                    return [1]
                elif self.__matrix[row-1][col-1] != 0 and self.__matrix[row][col-2] == 0:
                    return [1, 6]
                elif self.__matrix[row-1][col] != 0 and self.__matrix[row][col-2] != 0:
                    return [1, 2]
                elif self.__matrix[row-1][col] != 0 and self.__matrix[row][col-2] == 0:
                    return [1, 2, 6]
                elif self.__matrix[row][col-2] != 0:
                    return [1, 2, 3]
                else:
                    return [1, 2, 3, 6]
            elif enemy[0] == row and enemy[1] == col-3:
                if self.__matrix[row][col-2] != 0:
                    return None
                elif self.__matrix[row][col-1] != 0:
                    return [4]
                else:
                    return [4, 5]
            elif enemy[0] == row+1 and enemy[1] == col-3:
                if self.__matrix[row+1][col-2] != 0 and self.__matrix[row][col-2] != 0:
                    return None
                elif self.__matrix[row+1][col-2] != 0 and self.__matrix[row][col-2] == 0:
                    return [1]
                elif self.__matrix[row+1][col-1] != 0 and self.__matrix[row][col-2] != 0:
                    return [6]
                elif self.__matrix[row+1][col-1] != 0 and self.__matrix[row][col-2] == 0:
                    return [1, 6]
                elif self.__matrix[row+1][col] != 0 and self.__matrix[row][col-2] != 0:
                    return [6, 7]
                elif self.__matrix[row+1][col] != 0 and self.__matrix[row][col-2] == 0:
                    return [1, 6, 7]
                elif self.__matrix[row][col-2] != 0:
                    return [6, 7, 8]
                else:
                    return [1, 6, 7, 8]
            elif enemy[0] == row+3 and enemy[1] == col-1:
                if self.__matrix[row+2][col-1] != 0 and self.__matrix[row+2][col] != 0:
                    return None
                elif self.__matrix[row+2][col-1] != 0 and self.__matrix[row+2][col] == 0:
                    return [8]
                elif self.__matrix[row+1][col-1] != 0 and self.__matrix[row+2][col] != 0:
                    return [6]
                elif self.__matrix[row+1][col-1] != 0 and self.__matrix[row+2][col] == 0:
                    return [6, 8]
                elif self.__matrix[row][col-1] != 0 and self.__matrix[row+2][col] != 0:
                    return [4, 6]
                elif self.__matrix[row][col-1] != 0 and self.__matrix[row+2][col] == 0:
                    return [4, 6, 8]
                elif self.__matrix[row+2][col] != 0:
                    return [1, 4, 6]
                else:
                    return [1, 4, 6, 8]
            elif enemy[0] == row+3 and enemy[1] == col:
                if self.__matrix[row+2][col] != 0:
                    return None
                elif self.__matrix[row+1][col] != 0:
                    return [7]
                else:
                    return [2, 7]
            elif enemy[0] == row+3 and enemy[1] == col+1:
                if self.__matrix[row+2][col+1] != 0 and self.__matrix[row+2][col] != 0:
                    return None
                elif self.__matrix[row+2][col+1] != 0 and self.__matrix[row+2][col] == 0:
                    return [6]
                elif self.__matrix[row+1][col+1] != 0 and self.__matrix[row+2][col] != 0:
                    return [8]
                elif self.__matrix[row+1][col+1] != 0 and self.__matrix[row+2][col] == 0:
                    return [6, 8]
                elif self.__matrix[row][col+1] != 0 and self.__matrix[row+2][col] != 0:
                    return [5, 8]
                elif self.__matrix[row][col+1] != 0 and self.__matrix[row+2][col] == 0:
                    return [5, 6, 8]
                elif self.__matrix[row+2][col] != 0:
                    return [3, 5, 8]
                else:
                    return [3, 5, 6, 8]
            elif enemy[0] == row-1 and enemy[1] == col+3:
                if self.__matrix[row-1][col+2] != 0 and self.__matrix[row][col+2] != 0:
                    return None
                elif self.__matrix[row-1][col+2] != 0 and self.__matrix[row][col+2] == 0:
                    return [8]
                elif self.__matrix[row-1][col+1] != 0 and self.__matrix[row][col+2] != 0:
                    return [3]
                elif self.__matrix[row-1][col+1] != 0 and self.__matrix[row][col+2] == 0:
                    return [3, 8]
                elif self.__matrix[row-1][col] != 0 and self.__matrix[row][col+2] != 0:
                    return [2, 3]
                elif self.__matrix[row-1][col] != 0 and self.__matrix[row][col+2] == 0:
                    return [2, 3, 8]
                elif self.__matrix[row][col+2] != 0:
                    return [1, 2, 3]
                else:
                    return [1, 2, 3, 8]
            elif enemy[0] == row and enemy[1] == col+3:
                if self.__matrix[row][col+2] != 0:
                    return None
                elif self.__matrix[row][col+1] != 0:
                    return [5]
                else:
                    return [4, 5]
            elif enemy[0] == row+1 and enemy[1] == col+3:
                if self.__matrix[row+1][col+2] != 0 and self.__matrix[row][col+2] != 0:
                    return None
                elif self.__matrix[row+1][col+2] != 0 and self.__matrix[row][col+2] == 0:
                    return [3]
                elif self.__matrix[row+1][col+1] != 0 and self.__matrix[row][col+2] != 0:
                    return [8]
                elif self.__matrix[row+1][col+1] != 0 and self.__matrix[row][col+2] == 0:
                    return [3, 8]
                elif self.__matrix[row+1][col] != 0 and self.__matrix[row][col+2] != 0:
                    return [7, 8]
                elif self.__matrix[row+1][col] != 0 and self.__matrix[row][col+2] == 0:
                    return [3, 7, 8]
                elif self.__matrix[row][col+2] != 0:
                    return [6, 7, 8]
                else:
                    return [3, 6, 7, 8]
            elif (((enemy[0] >= 0 and enemy[0] < row-3) or (enemy[0] > row+3 and enemy[0] < self._rowlen)) and (enemy[1] >= col-1 and enemy[1] <= col+1)) or (((enemy[1] >= 0 and enemy[1] < col-3) or (enemy[1] > col+3 and enemy[1] < self._collen)) and (enemy[0] >= row-1 and enemy[0] <= row+1)):
                if enemy[0] == row-1:
                    if  enemy[1] < col-1:
                        for x in range(enemy[1]+1, col-1):
                            if self.__matrix[row-1][x] != 0:
                                return None
                        if self.__matrix[row-1][col-1] != 0:
                            return [1]
                        elif self.__matrix[row-1][col] != 0:
                            return [1, 2]
                    elif enemy[1] > col+1:
                        for x in range(col+2, enemy[1]):
                            if self.__matrix[row-1][x] != 0:
                                return None
                        if self.__matrix[row-1][col+1] != 0:
                            return [3]
                        elif self.__matrix[row-1][col] != 0:
                            return [2, 3]
                    return [1, 2, 3]
                elif enemy[0] == row:
                    if  enemy[1] < col-1:
                        for x in range(enemy[1]+1, col-1):
                            if self.__matrix[row][x] != 0:
                                return None
                        if self.__matrix[row][col-1] != 0:
                            return [4]
                    elif enemy[1] > col+1:
                        for x in range(col+2, enemy[1]):
                            if self.__matrix[row][x] != 0:
                                return None
                        if self.__matrix[row][col+1] != 0:
                            return [5]
                    return [4, 5]
                elif enemy[0] == row+1:
                    if enemy[1] < col-1:
                        for x in range(enemy[1]+1, col-1):
                            if self.__matrix[row+1][x] != 0:
                                return None
                        if self.__matrix[row+1][col-1] != 0:
                            return [6]
                        elif self.__matrix[row+1][col] != 0:
                            return [6, 7]
                    elif enemy[1] > col+1:
                        for x in range(col+2, enemy[1]):
                            if self.__matrix[row+1][x] != 0:
                                return None
                        if self.__matrix[row+1][col+1] != 0:
                            return [8]
                        elif self.__matrix[row+1][col] != 0:
                            return [7, 8]
                    return [6, 7, 8]
                elif enemy[1] == col-1:
                    if enemy[0] < row-1:
                        for x in range(enemy[0]+1, row-1):
                            if self.__matrix[x][col-1] != 0:
                                return None
                        if self.__matrix[row-1][col-1] != 0:
                            return [1]
                        elif self.__matrix[row][col-1] != 0:
                            return [1, 4]
                    elif enemy[0] > row+1:
                        for x in range(row+2, enemy[0]):
                            if self.__matrix[x][col-1] != 0:
                                return None
                        if self.__matrix[row+1][col-1] != 0:
                            return [6]
                        elif self.__matrix[row][col-1] != 0:
                            return [4, 6]
                    return [1, 4, 6]
                elif enemy[1] == col:
                    if enemy[0] < row-1:
                        for x in range(enemy[0]+1, row-1):
                            if self.__matrix[x][col] != 0:
                                return None
                        if self.__matrix[row-1][col] != 0:
                            return [2]
                    elif enemy[0] > row+1:
                        for x in range(row+2, enemy[0]):
                            if self.__matrix[x][col] != 0:
                                return None
                        if self.__matrix[row+1][col] != 0:
                            return [7]
                    return [2, 7]
                elif enemy[1] == col+1:
                    if enemy[0] < row-1:
                        for x in range(enemy[0]+1, row-1):
                            if self.__matrix[x][col+1] != 0:
                                return None
                        if self.__matrix[row-1][col+1] != 0:
                            return [3]
                        elif self.__matrix[row][col+1] != 0:
                            return [3, 5]
                    elif enemy[0] > row+1:
                        for x in range(row+2, enemy[0]):
                            if self.__matrix[x][col+1] != 0:
                                return None
                        if self.__matrix[row+1][col+1] != 0:
                            return [8]
                        elif self.__matrix[row][col+1] != 0:
                            return [5, 8]
                    return [3, 5, 8]
            else:
                if enemy[0] != (row-1) and enemy[1] != (col-1) and abs(enemy[0]-(row-1)) == abs(enemy[1]-(col-1)):
                    if enemy[0] != (row+1) and enemy[1] != (col+1) and abs(enemy[0]-(row+1)) == abs(enemy[1]-(col+1)):
                        if enemy[0] < (row-1) and enemy[1] < (col-1):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]+x][enemy[1]+x] != 0:
                                    return None
                            if self.__matrix[row-1][col-1] != 0:
                                return [1]
                        elif enemy[0] > (row+1) and enemy[1] > (col+1):
                            for x in range(1, abs(enemy[0]-(row+1))):
                                if self.__matrix[enemy[0]-x][enemy[1]-x] != 0:
                                    return None
                            if self.__matrix[row+1][col+1] != 0:
                                return [8]
                        return [1, 8]
                    else:
                        if enemy[0] < (row-1) and enemy[1] > (col-1):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]+x][enemy[1]-x] != 0:
                                    return None
                        elif enemy[0] > (row-1) and enemy[1] < (col-1):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]-x][enemy[1]+x] != 0:
                                    return None
                        return [1]
                elif enemy[0] != (row-1) and enemy[1] != (col) and abs(enemy[0]-(row-1)) == abs(enemy[1]-(col)):
                    if enemy[0] != (row) and enemy[1] != (col+1) and abs(enemy[0]-(row)) == abs(enemy[1]-(col+1)):
                        if enemy[0] < (row-1) and enemy[1] < (col):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]+x][enemy[1]+x] != 0:
                                    return None
                            if self.__matrix[row-1][col] != 0:
                                return [2]
                        elif enemy[0] > (row) and enemy[1] > (col+1):
                            for x in range(1, abs(enemy[0]-row)):
                                if self.__matrix[enemy[0]-x][enemy[1]-x] != 0:
                                    return None
                            if self.__matrix[row][col+1] != 0:
                                return [5]
                        return [2, 5]
                    elif enemy[0] != (row) and enemy[1] != (col-1) and abs(enemy[0]-(row)) == abs(enemy[1]-(col-1)):
                        if enemy[0] < (row-1) and enemy[1] > (col):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]+x][enemy[1]-x] != 0:
                                    return None
                            if self.__matrix[row-1][col] != 0:
                                return [2]
                        elif enemy[0] > (row) and enemy[1] < (col-1):
                            for x in range(1, abs(enemy[0]-row)):
                                if self.__matrix[enemy[0]-x][enemy[1]+x] != 0:
                                    return None
                            if self.__matrix[row][col-1] != 0:
                                return [4]
                        return [2, 4]
                elif enemy[0] != (row-1) and enemy[1] != (col+1) and abs(enemy[0]-(row-1)) == abs(enemy[1]-(col+1)):
                    if enemy[0] != (row+1) and enemy[1] != (col-1) and abs(enemy[0]-(row+1)) == abs(enemy[1]-(col-1)):
                        if enemy[0] < (row-1) and enemy[1] > (col+1):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]+x][enemy[1]-x] != 0:
                                    return None
                            if self.__matrix[row-1][col+1] != 0:
                                return [3]
                        elif enemy[0] > (row+1) and enemy[1] < (col-1):
                            for x in range(1, abs(enemy[0]-(row+1))):
                                if self.__matrix[enemy[0]-x][enemy[1]+x] != 0:
                                    return None
                            if self.__matrix[row+1][col-1] != 0:
                                return [6]
                        return [3, 6]
                    else:
                        if enemy[0] < (row-1) and enemy[1] < (col+1):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]+x][enemy[1]+x] != 0:
                                    return None
                        elif enemy[0] > (row-1) and enemy[1] > (col+1):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]-x][enemy[1]-x] != 0:
                                    return None
                        return [3]
                elif enemy[0] != (row) and enemy[1] != (col-1) and abs(enemy[0]-(row)) == abs(enemy[1]-(col-1)):
                    if enemy[0] != (row+1) and enemy[1] != (col) and abs(enemy[0]-(row+1)) == abs(enemy[1]-(col)):
                        if enemy[0] < (row) and enemy[1] < (col-1):
                            for x in range(1, abs(enemy[0]-row)):
                                if self.__matrix[enemy[0]+x][enemy[1]+x] != 0:
                                    return None
                            if self.__matrix[row-1][col] != 0:
                                return [4]
                        elif enemy[0] > (row+1) and enemy[1] > (col):
                            for x in range(1, abs(enemy[0]-row)):
                                if self.__matrix[enemy[0]-x][enemy[1]-x] != 0:
                                    return None
                            if self.__matrix[row+1][col] != 0:
                                return [7]
                        return [4, 7]
                elif enemy[0] != (row) and enemy[1] != (col+1) and abs(enemy[0]-(row)) == abs(enemy[1]-(col+1)):
                    if enemy[0] != (row+1) and enemy[1] != (col) and abs(enemy[0]-(row+1)) == abs(enemy[1]-(col)):
                        if enemy[0] < (row) and enemy[1] > (col+1):
                            for x in range(1, abs(enemy[0]-row)):
                                if self.__matrix[enemy[0]+x][enemy[1]-x] != 0:
                                    return None
                            if self.__matrix[row][col+1] != 0:
                                return [5]
                        elif enemy[0] > (row+1) and enemy[1] < (col):
                            for x in range(1, abs(enemy[0]-row)):
                                if self.__matrix[enemy[0]-x][enemy[1]+x] != 0:
                                    return None
                            if self.__matrix[row+1][col] != 0:
                                return [7]
                        return [5, 7]
                elif enemy[0] != (row+1) and enemy[1] != (col-1) and abs(enemy[0]-(row+1)) == abs(enemy[1]-(col-1)):
                    if enemy[0] < (row+1) and enemy[1] < (col-1):
                        for x in range(1, abs(enemy[0]-(row+1))):
                            if self.__matrix[enemy[0]+x][enemy[1]+x] != 0:
                                return None
                    elif enemy[0] > (row+1) and enemy[1] > (col-1):
                        for x in range(1, abs(enemy[0]-(row+1))):
                            if self.__matrix[enemy[0]-x][enemy[1]-x] != 0:
                                return None
                    return [6]
                elif enemy[0] != (row+1) and enemy[1] != (col+1) and abs(enemy[0]-(row+1)) == abs(enemy[1]-(col+1)):
                    if enemy[0] < (row+1) and enemy[1] > (col+1):
                        for x in range(1, abs(enemy[0]-(row+1))):
                            if self.__matrix[enemy[0]+x][enemy[1]-x] != 0:
                                return None
                    elif enemy[0] > (row+1) and enemy[1] < (col+1):
                        for x in range(1, abs(enemy[0]-(row+1))):
                            if self.__matrix[enemy[0]-x][enemy[1]+x] != 0:
                                return None
                    return [8]
        elif self.__matrix[enemy[0]][enemy[1]] == 12:
            if enemy[0] == row-2 and enemy[1] == col-2:
                return [1]
            elif enemy[0] == row-2 and enemy[1] == col-1:
                return [1, 2]
            elif enemy[0] == row-2 and enemy[1] == col:
                return [1, 2, 3]
            elif enemy[0] == row-2 and enemy[1] == col+1:
                return [2, 3]
            elif enemy[0] == row-2 and enemy[1] == col+2:
                return [3]
            elif enemy[0] == row-1 and enemy[1] == col-2:
                return [1, 4]
            elif enemy[0] == row-1 and enemy[1] == col-1:
                return [2, 4]
            elif enemy[0] == row-1 and enemy[1] == col:
                return [1, 3, 4, 5]
            elif enemy[0] == row-1 and enemy[1] == col+1:
                return [2, 5]
            elif enemy[0] == row-1 and enemy[1] == col+2:
                return [3, 5]
            elif enemy[0] == row and enemy[1] == col-2:
                return [1, 4, 6]
            elif enemy[0] == row and enemy[1] == col-1:
                return [1, 2, 6, 7]
            elif enemy[0] == row and enemy[1] == col+1:
                return [2, 3, 7, 8]
            elif enemy[0] == row and enemy[1] == col+2:
                return [3, 5, 8]
            elif enemy[0] == row+1 and enemy[1] == col-2:
                return [4, 6]
            elif enemy[0] == row+1 and enemy[1] == col-1:
                return [4, 7]
            elif enemy[0] == row+1 and enemy[1] == col:
                return [4, 5, 6, 8]
            elif enemy[0] == row+1 and enemy[1] == col+1:
                return [5, 7]
            elif enemy[0] == row+1 and enemy[1] == col+2:
                return [5, 8]
            elif enemy[0] == row+2 and enemy[1] == col-2:
                return [6]
            elif enemy[0] == row+2 and enemy[1] == col-1:
                return [6, 7]
            elif enemy[0] == row+2 and enemy[1] == col:
                return [6, 7, 8]
            elif enemy[0] == row+2 and enemy[1] == col+1:
                return [7, 8]
            elif enemy[0] == row+2 and enemy[1] == col+2:
                return [8]
    
    # check if check then get the only positions where it can only move
    def _check(self):
        encounter = 0
        check_box = {}
        kr, kc = self.__king
        for x in self.__player:
            r, c = x
            steps = []
            list1 = {}
            if self.__matrix[r][c] == 7:
                if r - 1 == kr and c - 1 == kc:
                    check_box[(r, c)] = True
                    encounter += 1
                elif r - 1 == kr and c + 1 == kc:
                    check_box[(r, c)] = True
                    encounter += 1
            elif self.__matrix[r][c] == 8:
                if (abs(r - kr) == 1 and abs(c - kc) == 2) or (abs(r - kr) == 2 and abs(c - kc) == 1):
                    check_box[(r, c)] = True
                    encounter += 1
            elif self.__matrix[r][c] == 9:
                if kr - r == kc - c > 0:
                    steps = [1, 1]
                elif r - kr == kc - c > 0:
                    steps = [-1, 1]
                elif kr - r == c - kc > 0:
                    steps = [1, -1]
                elif r - kr == c - kc > 0:
                    steps = [-1, -1]
            elif self.__matrix[r][c] == 10:
                if r == kr and c < kc:
                    steps = [0, 1]
                elif r == kr and c > kc:
                    steps = [0, -1]
                elif r < kr and c == kc:
                    steps = [1, 0]
                elif r > kr and c == kc:
                    steps = [-1, 0]
            elif self.__matrix[r][c] == 11:
                if kr - r == kc - c > 0:
                    steps = [1, 1]
                elif r - kr == kc - c > 0:
                    steps = [-1, 1]
                elif kr - r == c - kc > 0:
                    steps = [1, -1]
                elif r - kr == c - kc > 0:
                    steps = [-1, -1]
                elif r == kr and c < kc:
                    steps = [0, 1]
                elif r == kr and c > kc:
                    steps = [0, -1]
                elif r < kr and c == kc:
                    steps = [1, 0]
                elif r > kr and c == kc:
                    steps = [-1, 0]
            elif self.__matrix[r][c] == 12:
                continue
            # Sliding pieces: Bishop, Rook, Queen
            if len(steps) == 2:
                list1[(r, c)] = True
                row = r + steps[0]
                col = c + steps[1]
                while 0 <= row < self._rowlen and 0 <= col < self._collen:
                    if self.__matrix[row][col] == 0:
                        list1[(row, col)] = True
                    elif self.__matrix[row][col] == 6:
                        encounter += 1
                        break
                    else:
                        list1.clear()
                        break
                    row += steps[0]
                    col += steps[1]
                if list1:
                    check_box = list1.copy()
            # if more than one encounter occur with the king then king will only move in the board
            if encounter == 2:
                return {}, True
        if encounter == 1:
            return check_box, False
        else:
            return {}, False
    
    # gives the result as iterable when the class is been created as an object
    def __iter__(self):
        list1 = []
        if self._can_move(self.__matrix, self.__king):
            list1.extend(self._king(*self.__king))
            check_box, king_only = self._check()
            if not king_only:
                self.__check = check_box
            # castling check
            if not check_box and not king_only:
                s = {item for e in self.__player for result in [self._filterEnemy((e, self.__king[0], self.__king[1]))] if result for item in result if item in (4, 5)}
                if len(s) != 2:
                    for i in self.__castle:
                        if 4 not in s and i < self.__king[1]:
                            list1.extend(self._castling(i))
                        elif 5 not in s and i > self.__king[1]:
                            list1.extend(self._castling(i))
        for x in self.__bot:
            if self._can_move(self.__matrix, x):
                row, col = x
                if self.__matrix[row][col] == 1:
                    list1.extend(self._pawn(row, col))
                elif self.__matrix[row][col] == 2:
                    list1.extend(self._knight(row, col))
                elif self.__matrix[row][col] == 3:
                    list1.extend(self._bishop(row, col))
                elif self.__matrix[row][col] == 4:
                    list1.extend(self._rook(row, col))
                elif self.__matrix[row][col] == 5:
                    list1.extend(self._queen(row, col))
        return iter(list1)

    # castling
    def _castling(self, pos):
        list1 = []
        king_row, king_col = self.__king
        # checking the path is empty or not in between rook and king for castling
        if pos > king_col:
            if king_col >= self._collen - 2:
                castle = False
            else:
                castle = all(self.__matrix[king_row][col] == 0 for col in range(king_col + 1, pos))
        elif pos < king_col:
            if king_col <= 1:
                castle = False
            else:
                castle = all(self.__matrix[king_row][col] == 0 for col in range(pos + 1, king_col))
        else:
            castle = False
        # if castling is possible then check after castling any check occurs
        if castle:
            matrix = self.__matrix
            if pos > self.__king[1]:
                king_next = king_col + 2
                rook_next = king_col + 1
            elif pos < self.__king[1]:
                king_next = king_col - 2
                rook_next = king_col - 1
            # temporary peices moving
            matrix[king_row][rook_next] = 4
            matrix[king_row][pos] = 0
            matrix[king_row][king_next] = 6
            matrix[king_row][king_col] = 0
            self.__king = (king_row, king_next)
            check_box, king_only = self._check()
            if not check_box and not king_only:
                list1.append([king_row, king_col, king_row, king_next, None])
            # restore peices
            matrix[king_row][king_col] = 6
            matrix[king_row][king_next] = 0
            matrix[king_row][pos] = 4
            matrix[king_row][rook_next] = 0
            self.__king = (king_row, king_col)
        return list1

    # chessmen moves
    def _pawn(self, row, col):
        list1 = []
        if row < self._rowlen - 1:
            if row == 1:
                if (self.__matrix[row + 1][col] == 0 and self.__matrix[row + 2][col] == 0):
                    list1 = [node for x in [1, 2] for change in ([2, 5] if row + x == self._rowlen - 1 else [None]) if (node := self._make_node([row, col, row + x, col], self.__check, change)) is not None]
                elif (self.__matrix[row + 1][col] == 0 and self.__matrix[row + 2][col] != 0):
                    list1 = [node for change in ([2, 5] if row + 1 == self._rowlen - 1 else [None]) if (node := self._make_node([row, col, row + 1, col], self.__check, change)) is not None]
            else:
                if (self.__matrix[row + 1][col] == 0):
                    list1 = [node for change in ([2, 5] if row + 1 == self._rowlen - 1 else [None]) if (node := self._make_node([row, col, row + 1, col], self.__check, change)) is not None]
            if col - 1 >= 0:
                if (self.__matrix[row + 1][col - 1] != 0 and self.__matrix[row + 1][col - 1] > 6):
                    list1.extend([node for change in ([2, 5] if row + 1 == self._rowlen - 1 else [None]) if (node := self._make_node([row, col, row + 1, col - 1], self.__check, change)) is not None])
            if col + 1 < self._collen:
                if (self.__matrix[row + 1][col + 1] != 0 and self.__matrix[row + 1][col + 1] > 6):
                    list1.extend([node for change in ([2, 5] if row + 1 == self._rowlen - 1 else [None]) if (node := self._make_node([row, col, row + 1, col + 1], self.__check, change)) is not None])
        return list1
    
    def _knight(self, row, col):
        list1 = []
        moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        for dr, dc in moves:
            r = row + dr
            c = col + dc
            if (0 <= r < self._rowlen and 0 <= c < self._collen and (self.__matrix[r][c] == 0 or self.__matrix[r][c] > 6)):
                if (node := self._make_node([row, col, r, c], self.__check, None)) is not None: list1.append(node)
        return list1
    
    def _bishop(self, row, col):
        directions = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
        list1 = []
        for dr, dc in directions:
            list1.extend(self._slide(row, col, dr, dc))
        return list1
    
    def _rook(self, row, col):
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        list1 = []
        for dr, dc in directions:
            list1.extend(self._slide(row, col, dr, dc))
        return list1
    
    def _queen(self, row, col):
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]
        list1 = []
        for dr, dc in directions:
            list1.extend(self._slide(row, col, dr, dc))
        return list1
    
    def _king(self, row, col):
        list1 = []
        s = {item for e in self.__player for result in [self._filterEnemy((e, row, col))] if result for item in result}
        index = [i + 1 not in s for i in range(8)]
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1),  (1, 0),  (1, 1)]
        for i, (dr, dc) in enumerate(directions):
            r = row + dr
            c = col + dc
            if (0 <= r < self._rowlen and 0 <= c < self._collen and (self.__matrix[r][c] > 6 or self.__matrix[r][c] == 0) and index[i]):
                list1.append([row, col, r, c, None])
        return list1

class PlayerChessman(__MatrixOperation):
    __check = []
    # constructor
    def __init__(self, chessboard_info):
        self.__matrix = chessboard_info["matrix"]
        self.__player = chessboard_info["player"]
        self.__bot = chessboard_info["bot"]
        self.__king = chessboard_info["player_king"]
        self.__castle = chessboard_info["castling"]["player"]
        self._rowlen = len(chessboard_info["matrix"])
        self._collen = len(chessboard_info["matrix"][0])
        self._current_matrix(self.__matrix, self.__king, self.__bot)
        
    # inner moves of chessman
    def _slide(self, row, col, dr, dc):
        list1 = []
        r = row + dr
        c = col + dc
        while 0 <= r < self._rowlen and 0 <= c < self._collen:
            if self.__matrix[r][c] == 0:
                if (node := self._make_node([row, col, r, c], self.__check, None)) is not None: list1.append(node)
            elif self.__matrix[r][c] <= 6:
                if (node := self._make_node([row, col, r, c], self.__check, None)) is not None: list1.append(node)
                break
            else:
                break
            r += dr
            c += dc
        return list1
    
    # check where king cannot move
    def _filterEnemy(self, arg):
        enemy, row, col = arg
        if self.__matrix[enemy[0]][enemy[1]] == 1:
            if enemy[0] == row-2 and enemy[1] == col-2:
                return [1]
            elif enemy[0] == row-2 and enemy[1] == col-1:
                return [2]
            elif enemy[0] == row-2 and enemy[1] == col:
                return [1, 3]
            elif enemy[0] == row-2 and enemy[1] == col+1:
                return [2]
            elif enemy[0] == row-2 and enemy[1] == col+2:
                return [3]
            elif enemy[0] == row-1 and enemy[1] == col-2:
                return [4]
            elif enemy[0] == row-1 and enemy[1] == col:
                return [4, 5]
            elif enemy[0] == row-1 and enemy[1] == col+2:
                return [5]
            elif enemy[0] == row and enemy[1] == col-2:
                return [6]
            elif enemy[0] == row and enemy[1] == col-1:
                return [7]
            elif enemy[0] == row and enemy[1] == col+1:
                return [7]
            elif enemy[0] == row and enemy[1] == col+2:
                return [8]
        elif self.__matrix[enemy[0]][enemy[1]] == 2:
            if (enemy[0] == (row-3) and enemy[1] == (col-2)):
                return [1]
            elif (enemy[0] == (row-3) and enemy[1] == (col-1)):
                return [2]
            elif (enemy[0] == (row-3) and enemy[1] == (col)):
                return [1, 3]
            elif (enemy[0] == (row-3) and enemy[1] == (col+1)):
                return [2]
            elif (enemy[0] == (row-3) and enemy[1] == (col+2)):
                return [3]
            elif (enemy[0] == (row-2) and enemy[1] == (col-3)):
                return [1]
            elif (enemy[0] == (row-2) and enemy[1] == (col-2)):
                return [2, 4]
            elif (enemy[0] == (row-2) and enemy[1] == (col-1)):
                return [3]
            elif (enemy[0] == (row-2) and enemy[1] == (col)):
                return [4, 5]
            elif (enemy[0] == (row-2) and enemy[1] == (col+1)):
                return [1]
            elif (enemy[0] == (row-2) and enemy[1] == (col+2)):
                return [2, 5]
            elif (enemy[0] == (row-2) and enemy[1] == (col+3)):
                return [3]
            elif (enemy[0] == (row-1) and enemy[1] == (col-3)):
                return [4]
            elif (enemy[0] == (row-1) and enemy[1] == (col-2)):
                return [6]
            elif (enemy[0] == (row-1) and enemy[1] == (col-1)):
                return [5, 7]
            elif (enemy[0] == (row-1) and enemy[1] == (col)):
                return [6, 8]
            elif (enemy[0] == (row-1) and enemy[1] == (col+1)):
                return [4, 7]
            elif (enemy[0] == (row-1) and enemy[1] == (col+2)):
                return [8]
            elif (enemy[0] == (row-1) and enemy[1] == (col+3)):
                return [5]
            elif (enemy[0] == (row) and enemy[1] == (col-3)):
                return [1, 6]
            elif (enemy[0] == (row) and enemy[1] == (col-2)):
                return [2, 7]
            elif (enemy[0] == (row) and enemy[1] == (col-1)):
                return [3, 8]
            elif (enemy[0] == (row) and enemy[1] == (col+1)):
                return [1, 6]
            elif (enemy[0] == (row) and enemy[1] == (col+2)):
                return [2, 7]
            elif (enemy[0] == (row) and enemy[1] == (col+3)):
                return [3, 8]
            elif (enemy[0] == (row+1) and enemy[1] == (col-3)):
                return [4]
            elif (enemy[0] == (row+1) and enemy[1] == (col-2)):
                return [1]
            elif (enemy[0] == (row+1) and enemy[1] == (col-1)):
                return [2, 5]
            elif (enemy[0] == (row+1) and enemy[1] == (col)):
                return [1, 3]
            elif (enemy[0] == (row+1) and enemy[1] == (col+1)):
                return [2, 4]
            elif (enemy[0] == (row+1) and enemy[1] == (col+2)):
                return [3]
            elif (enemy[0] == (row+1) and enemy[1] == (col+3)):
                return [5]
            elif (enemy[0] == (row+2) and enemy[1] == (col-3)):
                return [6]
            elif (enemy[0] == (row+2) and enemy[1] == (col-2)):
                return [4, 7]
            elif (enemy[0] == (row+2) and enemy[1] == (col-1)):
                return [8]
            elif (enemy[0] == (row+2) and enemy[1] == (col)):
                return [4, 5]
            elif (enemy[0] == (row+2) and enemy[1] == (col+1)):
                return [6]
            elif (enemy[0] == (row+2) and enemy[1] == (col+2)):
                return [5, 7]
            elif (enemy[0] == (row+2) and enemy[1] == (col+3)):
                return [8]
            elif (enemy[0] == (row+3) and enemy[1] == (col-2)):
                return [6]
            elif (enemy[0] == (row+3) and enemy[1] == (col-1)):
                return [7]
            elif (enemy[0] == (row+3) and enemy[1] == (col)):
                return [6, 8]
            elif (enemy[0] == (row+3) and enemy[1] == (col+1)):
                return [7]
            elif (enemy[0] == (row+3) and enemy[1] == (col+2)):
                return [8]
        elif self.__matrix[enemy[0]][enemy[1]] == 3:
            if enemy[0] == (row+2) and enemy[1] == col:
                return [6, 8]
            elif (enemy[0] == (row+1) and enemy[1] == col) or (enemy[0] == (row-1) and enemy[1] == col):
                return [4, 5]
            elif enemy[0] == (row-2) and enemy[1] == col:
                return [1, 3]
            elif enemy[0] == row and enemy[1] == (col+2):
                return [3, 8]
            elif (enemy[0] == row and enemy[1] == (col+1)) or (enemy[0] == row and enemy[1] == (col-1)):
                return [2, 7]
            elif enemy[0] == row and enemy[1] == (col-2):
                return [1, 6]
            else:
                if enemy[0] != (row-1) and enemy[1] != (col-1) and abs(enemy[0]-(row-1)) == abs(enemy[1]-(col-1)):
                    if enemy[0] != (row+1) and enemy[1] != (col+1) and abs(enemy[0]-(row+1)) == abs(enemy[1]-(col+1)):
                        if enemy[0] < (row-1) and enemy[1] < (col-1):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]+x][enemy[1]+x] != 0:
                                    return None
                            if self.__matrix[row-1][col-1] != 0:
                                return [1]
                        elif enemy[0] > (row+1) and enemy[1] > (col+1):
                            for x in range(1, abs(enemy[0]-(row+1))):
                                if self.__matrix[enemy[0]-x][enemy[1]-x] != 0:
                                    return None
                            if self.__matrix[row+1][col+1] != 0:
                                return [8]
                        return [1, 8]
                    else:
                        if enemy[0] < (row-1) and enemy[1] > (col-1):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]+x][enemy[1]-x] != 0:
                                    return None
                        elif enemy[0] > (row-1) and enemy[1] < (col-1):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]-x][enemy[1]+x] != 0:
                                    return None
                        return [1]
                elif enemy[0] != (row-1) and enemy[1] != (col) and abs(enemy[0]-(row-1)) == abs(enemy[1]-(col)):
                    if enemy[0] != (row) and enemy[1] != (col+1) and abs(enemy[0]-(row)) == abs(enemy[1]-(col+1)):
                        if enemy[0] < (row-1) and enemy[1] < (col):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]+x][enemy[1]+x] != 0:
                                    return None
                            if self.__matrix[row-1][col] != 0:
                                return [2]
                        elif enemy[0] > (row) and enemy[1] > (col+1):
                            for x in range(1, abs(enemy[0]-row)):
                                if self.__matrix[enemy[0]-x][enemy[1]-x] != 0:
                                    return None
                            if self.__matrix[row][col+1] != 0:
                                return [5]
                        return [2, 5]
                    elif enemy[0] != (row) and enemy[1] != (col-1) and abs(enemy[0]-(row)) == abs(enemy[1]-(col-1)):
                        if enemy[0] < (row-1) and enemy[1] > (col):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]+x][enemy[1]-x] != 0:
                                    return None
                            if self.__matrix[row-1][col] != 0:
                                return [2]
                        elif enemy[0] > (row) and enemy[1] < (col-1):
                            for x in range(1, abs(enemy[0]-row)):
                                if self.__matrix[enemy[0]-x][enemy[1]+x] != 0:
                                    return None
                            if self.__matrix[row][col-1] != 0:
                                return [4]
                        return [2, 4]
                elif enemy[0] != (row-1) and enemy[1] != (col+1) and abs(enemy[0]-(row-1)) == abs(enemy[1]-(col+1)):
                    if enemy[0] != (row+1) and enemy[1] != (col-1) and abs(enemy[0]-(row+1)) == abs(enemy[1]-(col-1)):
                        if enemy[0] < (row-1) and enemy[1] > (col+1):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]+x][enemy[1]-x] != 0:
                                    return None
                            if self.__matrix[row-1][col+1] != 0:
                                return [3]
                        elif enemy[0] > (row+1) and enemy[1] < (col-1):
                            for x in range(1, abs(enemy[0]-(row+1))):
                                if self.__matrix[enemy[0]-x][enemy[1]+x] != 0:
                                    return None
                            if self.__matrix[row+1][col-1] != 0:
                                return [6]
                        return [3, 6]
                    else:
                        if enemy[0] < (row-1) and enemy[1] < (col+1):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]+x][enemy[1]+x] != 0:
                                    return None
                        elif enemy[0] > (row-1) and enemy[1] > (col+1):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]-x][enemy[1]-x] != 0:
                                    return None
                        return [3]
                elif enemy[0] != (row) and enemy[1] != (col-1) and abs(enemy[0]-(row)) == abs(enemy[1]-(col-1)):
                    if enemy[0] != (row+1) and enemy[1] != (col) and abs(enemy[0]-(row+1)) == abs(enemy[1]-(col)):
                        if enemy[0] < (row) and enemy[1] < (col-1):
                            for x in range(1, abs(enemy[0]-row)):
                                if self.__matrix[enemy[0]+x][enemy[1]+x] != 0:
                                    return None
                            if self.__matrix[row-1][col] != 0:
                                return [4]
                        elif enemy[0] > (row+1) and enemy[1] > (col):
                            for x in range(1, abs(enemy[0]-row)):
                                if self.__matrix[enemy[0]-x][enemy[1]-x] != 0:
                                    return None
                            if self.__matrix[row+1][col] != 0:
                                return [7]
                        return [4, 7]
                elif enemy[0] != (row) and enemy[1] != (col+1) and abs(enemy[0]-(row)) == abs(enemy[1]-(col+1)):
                    if enemy[0] != (row+1) and enemy[1] != (col) and abs(enemy[0]-(row+1)) == abs(enemy[1]-(col)):
                        if enemy[0] < (row) and enemy[1] > (col+1):
                            for x in range(1, abs(enemy[0]-row)):
                                if self.__matrix[enemy[0]+x][enemy[1]-x] != 0:
                                    return None
                            if self.__matrix[row][col+1] != 0:
                                return [5]
                        elif enemy[0] > (row+1) and enemy[1] < (col):
                            for x in range(1, abs(enemy[0]-row)):
                                if self.__matrix[enemy[0]-x][enemy[1]+x] != 0:
                                    return None
                            if self.__matrix[row+1][col] != 0:
                                return [7]
                        return [5, 7]
                elif enemy[0] != (row+1) and enemy[1] != (col-1) and abs(enemy[0]-(row+1)) == abs(enemy[1]-(col-1)):
                    if enemy[0] < (row+1) and enemy[1] < (col-1):
                        for x in range(1, abs(enemy[0]-(row+1))):
                            if self.__matrix[enemy[0]+x][enemy[1]+x] != 0:
                                return None
                    elif enemy[0] > (row+1) and enemy[1] > (col-1):
                        for x in range(1, abs(enemy[0]-(row+1))):
                            if self.__matrix[enemy[0]-x][enemy[1]-x] != 0:
                                return None
                    return [6]
                elif enemy[0] != (row+1) and enemy[1] != (col+1) and abs(enemy[0]-(row+1)) == abs(enemy[1]-(col+1)):
                    if enemy[0] < (row+1) and enemy[1] > (col+1):
                        for x in range(1, abs(enemy[0]-(row+1))):
                            if self.__matrix[enemy[0]+x][enemy[1]-x] != 0:
                                return None
                    elif enemy[0] > (row+1) and enemy[1] < (col+1):
                        for x in range(1, abs(enemy[0]-(row+1))):
                            if self.__matrix[enemy[0]-x][enemy[1]+x] != 0:
                                return None
                    return [8]
        elif self.__matrix[enemy[0]][enemy[1]] == 4:
            if enemy[0] == row-1 and enemy[1] == col-1:
                if self.__matrix[row][col-1] != 0 and self.__matrix[row-1][col] != 0:
                    return [2, 4]
                elif self.__matrix[row][col-1] == 0 and self.__matrix[row-1][col] != 0:
                    return [2, 4, 6]
                elif self.__matrix[row][col-1] != 0 and self.__matrix[row-1][col] == 0:
                    return [2, 3, 4]
                else:
                    return [2, 3, 4, 6]
            elif enemy[0] == row-1 and enemy[1] == col:
                return [1, 3, 7]
            elif enemy[0] == row-1 and enemy[1] == col+1:
                if self.__matrix[row][col+1] != 0 and self.__matrix[row-1][col] != 0:
                    return [2, 5]
                elif self.__matrix[row][col+1] == 0 and self.__matrix[row-1][col] != 0:
                    return [2, 5, 8]
                elif self.__matrix[row][col+1] != 0 and self.__matrix[row-1][col] == 0:
                    return [1, 2, 5]
                else:
                    return [1, 2, 5, 8]
            elif enemy[0] == row and enemy[1] == col-1:
                return [1, 5, 6]
            elif enemy[0] == row and enemy[1] == col+1:
                return [3, 4, 8]
            elif enemy[0] == row+1 and enemy[1] == col-1:
                if self.__matrix[row][col-1] != 0 and self.__matrix[row+1][col] != 0:
                    return [4, 7]
                elif self.__matrix[row][col-1] == 0 and self.__matrix[row+1][col] != 0:
                    return [1, 4, 7]
                elif self.__matrix[row][col-1] != 0 and self.__matrix[row+1][col] == 0:
                    return [4, 7, 8]
                else:
                    return [1, 4, 7, 8]
            elif enemy[0] == row+1 and enemy[1] == col:
                return [2, 6, 8]
            elif enemy[0] == row+1 and enemy[1] == col+1:
                if self.__matrix[row][col+1] != 0 and self.__matrix[row+1][col] != 0:
                    return [5, 7]
                elif self.__matrix[row][col+1] == 0 and self.__matrix[row+1][col] != 0:
                    return [3, 5, 7]
                elif self.__matrix[row][col+1] != 0 and self.__matrix[row+1][col] == 0:
                    return [5, 6, 7]
                else:
                    return [3, 5, 6, 7]
            else:
                if enemy[0] == row-1:
                    if  enemy[1] < col-1:
                        for x in range(enemy[1]+1, col-1):
                            if self.__matrix[row-1][x] != 0:
                                return None
                        if self.__matrix[row-1][col-1] != 0:
                            return [1]
                        elif self.__matrix[row-1][col] != 0:
                            return [1, 2]
                    elif enemy[1] > col+1:
                        for x in range(col+2, enemy[1]):
                            if self.__matrix[row-1][x] != 0:
                                return None
                        if self.__matrix[row-1][col+1] != 0:
                            return [3]
                        elif self.__matrix[row-1][col] != 0:
                            return [2, 3]
                    return [1, 2, 3]
                elif enemy[0] == row:
                    if  enemy[1] < col-1:
                        for x in range(enemy[1]+1, col-1):
                            if self.__matrix[row][x] != 0:
                                return None
                        if self.__matrix[row][col-1] != 0:
                            return [4]
                    elif enemy[1] > col+1:
                        for x in range(col+2, enemy[1]):
                            if self.__matrix[row][x] != 0:
                                return None
                        if self.__matrix[row][col+1] != 0:
                            return [5]
                    return [4, 5]
                elif enemy[0] == row+1:
                    if enemy[1] < col-1:
                        for x in range(enemy[1]+1, col-1):
                            if self.__matrix[row+1][x] != 0:
                                return None
                        if self.__matrix[row+1][col-1] != 0:
                            return [6]
                        elif self.__matrix[row+1][col] != 0:
                            return [6, 7]
                    elif enemy[1] > col+1:
                        for x in range(col+2, enemy[1]):
                            if self.__matrix[row+1][x] != 0:
                                return None
                        if self.__matrix[row+1][col+1] != 0:
                            return [8]
                        elif self.__matrix[row+1][col] != 0:
                            return [7, 8]
                    return [6, 7, 8]
                elif enemy[1] == col-1:
                    if enemy[0] < row-1:
                        for x in range(enemy[0]+1, row-1):
                            if self.__matrix[x][col-1] != 0:
                                return None
                        if self.__matrix[row-1][col-1] != 0:
                            return [1]
                        elif self.__matrix[row][col-1] != 0:
                            return [1, 4]
                    elif enemy[0] > row+1:
                        for x in range(row+2, enemy[0]):
                            if self.__matrix[x][col-1] != 0:
                                return None
                        if self.__matrix[row+1][col-1] != 0:
                            return [6]
                        elif self.__matrix[row][col-1] != 0:
                            return [4, 6]
                    return [1, 4, 6]
                elif enemy[1] == col:
                    if enemy[0] < row-1:
                        for x in range(enemy[0]+1, row-1):
                            if self.__matrix[x][col] != 0:
                                return None
                        if self.__matrix[row-1][col] != 0:
                            return [2]
                    elif enemy[0] > row+1:
                        for x in range(row+2, enemy[0]):
                            if self.__matrix[x][col] != 0:
                                return None
                        if self.__matrix[row+1][col] != 0:
                            return [7]
                    return [2, 7]
                elif enemy[1] == col+1:
                    if enemy[0] < row-1:
                        for x in range(enemy[0]+1, row-1):
                            if self.__matrix[x][col+1] != 0:
                                return None
                        if self.__matrix[row-1][col+1] != 0:
                            return [3]
                        elif self.__matrix[row][col+1] != 0:
                            return [3, 5]
                    elif enemy[0] > row+1:
                        for x in range(row+2, enemy[0]):
                            if self.__matrix[x][col+1] != 0:
                                return None
                        if self.__matrix[row+1][col+1] != 0:
                            return [8]
                        elif self.__matrix[row][col+1] != 0:
                            return [5, 8]
                    return [3, 5, 8]
        elif self.__matrix[enemy[0]][enemy[1]] == 5:
            if enemy[0] == row-1 and enemy[1] == col-1:
                if self.__matrix[row-1][col] != 0 and self.__matrix[row][col-1] != 0:
                    return [2, 4, 8]
                elif self.__matrix[row-1][col] != 0 and self.__matrix[row][col-1] == 0:
                    return [2, 4, 6, 8]
                elif self.__matrix[row-1][col] == 0 and self.__matrix[row][col-1] != 0:
                    return [2, 3, 4, 8]
                else:
                    return [2, 3, 4, 6, 8]
            elif enemy[0] == row-1 and enemy[1] == col:
                return [1, 3, 4, 5, 7]
            elif enemy[0] == row-1 and enemy[1] == col+1:
                if self.__matrix[row-1][col] != 0 and self.__matrix[row][col+1] != 0:
                    return [2, 5, 6]
                elif self.__matrix[row-1][col] != 0 and self.__matrix[row][col+1] == 0:
                    return [2, 5, 6, 8]
                elif self.__matrix[row-1][col] == 0 and self.__matrix[row][col+1] != 0:
                    return [1, 2, 5, 6]
                else:
                    return [1, 2, 5, 6, 8]
            elif enemy[0] == row and enemy[1] == col-1:
                return [1, 2, 5, 6, 7]
            elif enemy[0] == row and enemy[1] == col+1:
                return [2, 3, 4, 7, 8]
            elif enemy[0] == row+1 and enemy[1] == col-1:
                if self.__matrix[row+1][col] != 0 and self.__matrix[row][col-1] != 0:
                    return [3, 4, 7]
                elif self.__matrix[row+1][col] != 0 and self.__matrix[row][col-1] == 0:
                    return [1, 3, 4, 7]
                elif self.__matrix[row+1][col] == 0 and self.__matrix[row][col-1] != 0:
                    return [3, 4, 7, 8]
                else:
                    return [1, 3, 4, 7, 8]
            elif enemy[0] == row+1 and enemy[1] == col:
                return [2, 4, 5, 6, 8]
            elif enemy[0] == row+1 and enemy[1] == col+1:
                if self.__matrix[row+1][col] != 0 and self.__matrix[row][col+1] != 0:
                    return [1, 5, 7]
                elif self.__matrix[row+1][col] != 0 and self.__matrix[row][col+1] == 0:
                    return [1, 3, 5, 7]
                elif self.__matrix[row+1][col] == 0 and self.__matrix[row][col+1] != 0:
                    return [1, 5, 6, 7]
                else:
                    return [1, 3, 5, 6, 7]
            elif enemy[0] == row-2 and enemy[1] == col-1:
                if self.__matrix[row-1][col-1] != 0 and self.__matrix[row-1][col] != 0:
                    return [1, 2]
                elif self.__matrix[row-1][col-1] != 0 and self.__matrix[row-1][col] == 0:
                    return [1, 2, 5]
                elif self.__matrix[row][col-1] != 0 and self.__matrix[row-1][col] != 0:
                    return [1, 2, 4]
                elif self.__matrix[row][col-1] != 0 and self.__matrix[row-1][col] != 0:
                    return [1, 2, 4, 5]
                elif self.__matrix[row-1][col] != 0 and self.__matrix[row][col-1] == 0:
                    return [1, 2, 4, 6]
                else:
                    return [1, 2, 4, 5, 6]
            elif enemy[0] == row-2 and enemy[1] == col:
                if self.__matrix[row-1][col] != 0:
                    return [1, 2, 3]
                else:
                    return [1, 2, 3, 7]
            elif enemy[0] == row-2 and enemy[1] == col+1:
                if self.__matrix[row-1][col+1] != 0 and self.__matrix[row-1][col] != 0:
                    return [2, 3]
                elif self.__matrix[row-1][col+1] != 0 and self.__matrix[row-1][col] == 0:
                    return [2, 3, 4]
                elif self.__matrix[row][col+1] != 0 and self.__matrix[row-1][col] != 0:
                    return [2, 3, 5]
                elif self.__matrix[row][col+1] != 0 and self.__matrix[row-1][col] == 0:
                    return [2, 3, 4, 5]
                elif self.__matrix[row-1][col] != 0 and self.__matrix[row][col+1] == 0:
                    return [2, 3, 5, 8]
                else:
                    return [2, 3, 4, 5, 8]
            elif enemy[0] == row-1 and enemy[1] == col-2:
                if self.__matrix[row-1][col-1] != 0 and self.__matrix[row][col-1] != 0:
                    return [1, 4]
                elif self.__matrix[row-1][col-1] != 0 and self.__matrix[row][col-1] == 0:
                    return [1, 4, 7]
                elif self.__matrix[row-1][col] != 0 and self.__matrix[row][col-1] != 0:
                    return [1, 2, 4]
                elif self.__matrix[row-1][col] != 0 and self.__matrix[row][col-1] == 0:
                    return [1, 2, 4, 7]
                elif self.__matrix[row][col-1] != 0 and self.__matrix[row-1][col] == 0:
                    return [1, 2, 3, 4]
                else:
                    return [1, 2, 3, 4, 7]
            elif enemy[0] == row and enemy[1] == col-2:
                if self.__matrix[row][col-1] != 0:
                    return [1, 4, 6]
                else:
                    return [1, 4, 5, 6]
            elif enemy[0] == row+1 and enemy[1] == col-2:
                if self.__matrix[row+1][col-1] != 0 and self.__matrix[row][col-1] != 0:
                    return [4, 6]
                elif self.__matrix[row+1][col-1] != 0 and self.__matrix[row][col-1] == 0:
                    return [2, 4, 6]
                elif self.__matrix[row+1][col] != 0 and self.__matrix[row][col-1] != 0:
                    return [4, 6, 7]
                elif self.__matrix[row+1][col] != 0 and self.__matrix[row][col-1] == 0:
                    return [2, 4, 6, 7]
                elif self.__matrix[row][col-1] != 0 and self.__matrix[row+1][col] == 0 :
                    return [4, 6, 7, 8]
                else:
                    return [2, 4, 6, 7, 8]
            elif enemy[0] == row+2 and enemy[1] == col-1:
                if self.__matrix[row+1][col-1] != 0 and self.__matrix[row+1][col] != 0:
                    return [6, 7]
                elif self.__matrix[row+1][col-1] != 0 and self.__matrix[row+1][col] == 0:
                    return [5, 6, 7]
                elif self.__matrix[row][col-1] != 0 and self.__matrix[row+1][col] != 0:
                    return [4, 6, 7]
                elif self.__matrix[row][col-1] == 0 and self.__matrix[row+1][col] != 0:
                    return [1, 4, 6, 7]
                elif self.__matrix[row][col-1] != 0 and self.__matrix[row+1][col] == 0:
                    return [4, 5, 6, 7]
                else:
                    return [1, 4, 5, 6, 7]
            elif enemy[0] == row+2 and enemy[1] == col:
                if self.__matrix[row+1][col] != 0:
                    return [6, 7, 8]
                else:
                    return [2, 6, 7, 8]
            elif enemy[0] == row+2 and enemy[1] == col+1:
                if self.__matrix[row+1][col+1] != 0 and self.__matrix[row+1][col] != 0:
                    return [7, 8]
                elif self.__matrix[row+1][col+1] != 0 and self.__matrix[row+1][col] == 0:
                    return [4, 7, 8]
                elif self.__matrix[row][col+1] != 0 and self.__matrix[row+1][col] != 0:
                    return [5, 7, 8]
                elif self.__matrix[row][col+1] == 0 and self.__matrix[row+1][col] != 0:
                    return [3, 5, 7, 8]
                elif self.__matrix[row][col+1] != 0 and self.__matrix[row+1][col] == 0:
                    return [4, 5, 7, 8]
                else:
                    return [3, 4, 5, 7, 8]
            elif enemy[0] == row-1 and enemy[1] == col+2:
                if self.__matrix[row-1][col+1] != 0 and self.__matrix[row][col+1] != 0:
                    return [3, 5]
                elif self.__matrix[row-1][col+1] != 0 and self.__matrix[row][col+1] == 0:
                    return [3, 5, 7]
                elif self.__matrix[row-1][col] != 0 and self.__matrix[row][col+1] != 0:
                    return [2, 3, 5]
                elif self.__matrix[row-1][col] != 0 and self.__matrix[row][col+1] == 0:
                    return [2, 3, 5, 7]
                elif self.__matrix[row-1][col] == 0 and self.__matrix[row][col+1] != 0:
                    return [1, 2, 3, 5]
                else:
                    return [1, 2, 3, 5, 7]
            elif enemy[0] == row and enemy[1] == col+2:
                if self.__matrix[row][col+1] != 0:
                    return [3, 5, 8]
                else:
                    return [3, 4, 5, 8]
            elif enemy[0] == row+1 and enemy[1] == col+2:
                if self.__matrix[row+1][col+1] != 0 and self.__matrix[row][col+1] != 0:
                    return [5, 8]
                elif self.__matrix[row+1][col+1] != 0 and self.__matrix[row][col+1] == 0:
                    return [2, 5, 8]
                elif self.__matrix[row+1][col] != 0 and self.__matrix[row][col+1] != 0:
                    return [5, 7, 8]
                elif self.__matrix[row+1][col] != 0 and self.__matrix[row][col+1] == 0:
                    return [2, 5, 7, 8]
                elif self.__matrix[row+1][col] == 0 and self.__matrix[row][col+1] != 0:
                    return [5, 6, 7, 8]
                else:
                    return [2, 5, 6, 7, 8]
            elif enemy[0] == row-3 and enemy[1] == col-1:
                if self.__matrix[row-2][col-1] != 0 and self.__matrix[row-2][col] != 0:
                    return None
                elif self.__matrix[row-2][col-1] != 0 and self.__matrix[row-2][col] == 0:
                    return [3]
                elif self.__matrix[row-1][col-1] != 0 and self.__matrix[row-2][col] != 0:
                    return [1]
                elif self.__matrix[row-1][col-1] != 0 and self.__matrix[row-2][col] == 0:
                    return [1, 3]
                elif self.__matrix[row][col-1] != 0 and self.__matrix[row-2][col] != 0:
                    return [1, 4]
                elif self.__matrix[row][col-1] != 0 and self.__matrix[row-2][col] == 0:
                    return [1, 4, 3]
                elif self.__matrix[row-2][col] != 0:
                    return [1, 4, 6]
                else:
                    return [1, 3, 4, 6]
            elif enemy[0] == row-3 and enemy[1] == col:
                if self.__matrix[row-2][col] != 0:
                    return None
                elif self.__matrix[row-1][col] != 0:
                    return [2]
                else:
                    return [2, 7]
            elif enemy[0] == row-3 and enemy[1] == col+1:
                if self.__matrix[row-2][col+1] != 0 and self.__matrix[row-2][col] != 0:
                    return None
                elif self.__matrix[row-2][col+1] != 0 and self.__matrix[row-2][col] == 0:
                    return [1]
                elif self.__matrix[row-1][col+1] != 0 and self.__matrix[row-2][col] != 0:
                    return [3]
                elif self.__matrix[row-1][col+1] != 0 and self.__matrix[row-2][col] == 0:
                    return [1, 3]
                elif self.__matrix[row][col+1] != 0 and self.__matrix[row-2][col] != 0:
                    return [3, 5]
                elif self.__matrix[row][col+1] != 0 and self.__matrix[row-2][col] == 0:
                    return [1, 3, 5]
                elif self.__matrix[row-2][col] != 0:
                    return [3, 5, 8]
                else:
                    return [1, 3, 5, 8]
            elif enemy[0] == row-1 and enemy[1] == col-3:
                if self.__matrix[row-1][col-2] != 0 and self.__matrix[row][col-2] != 0:
                    return None
                elif self.__matrix[row-1][col-2] != 0 and self.__matrix[row][col-2] == 0:
                    return [6]
                elif self.__matrix[row-1][col-1] != 0 and self.__matrix[row][col-2] != 0:
                    return [1]
                elif self.__matrix[row-1][col-1] != 0 and self.__matrix[row][col-2] == 0:
                    return [1, 6]
                elif self.__matrix[row-1][col] != 0 and self.__matrix[row][col-2] != 0:
                    return [1, 2]
                elif self.__matrix[row-1][col] != 0 and self.__matrix[row][col-2] == 0:
                    return [1, 2, 6]
                elif self.__matrix[row][col-2] != 0:
                    return [1, 2, 3]
                else:
                    return [1, 2, 3, 6]
            elif enemy[0] == row and enemy[1] == col-3:
                if self.__matrix[row][col-2] != 0:
                    return None
                elif self.__matrix[row][col-1] != 0:
                    return [4]
                else:
                    return [4, 5]
            elif enemy[0] == row+1 and enemy[1] == col-3:
                if self.__matrix[row+1][col-2] != 0 and self.__matrix[row][col-2] != 0:
                    return None
                elif self.__matrix[row+1][col-2] != 0 and self.__matrix[row][col-2] == 0:
                    return [1]
                elif self.__matrix[row+1][col-1] != 0 and self.__matrix[row][col-2] != 0:
                    return [6]
                elif self.__matrix[row+1][col-1] != 0 and self.__matrix[row][col-2] == 0:
                    return [1, 6]
                elif self.__matrix[row+1][col] != 0 and self.__matrix[row][col-2] != 0:
                    return [6, 7]
                elif self.__matrix[row+1][col] != 0 and self.__matrix[row][col-2] == 0:
                    return [1, 6, 7]
                elif self.__matrix[row][col-2] != 0:
                    return [6, 7, 8]
                else:
                    return [1, 6, 7, 8]
            elif enemy[0] == row+3 and enemy[1] == col-1:
                if self.__matrix[row+2][col-1] != 0 and self.__matrix[row+2][col] != 0:
                    return None
                elif self.__matrix[row+2][col-1] != 0 and self.__matrix[row+2][col] == 0:
                    return [8]
                elif self.__matrix[row+1][col-1] != 0 and self.__matrix[row+2][col] != 0:
                    return [6]
                elif self.__matrix[row+1][col-1] != 0 and self.__matrix[row+2][col] == 0:
                    return [6, 8]
                elif self.__matrix[row][col-1] != 0 and self.__matrix[row+2][col] != 0:
                    return [4, 6]
                elif self.__matrix[row][col-1] != 0 and self.__matrix[row+2][col] == 0:
                    return [4, 6, 8]
                elif self.__matrix[row+2][col] != 0:
                    return [1, 4, 6]
                else:
                    return [1, 4, 6, 8]
            elif enemy[0] == row+3 and enemy[1] == col:
                if self.__matrix[row+2][col] != 0:
                    return None
                elif self.__matrix[row+1][col] != 0:
                    return [7]
                else:
                    return [2, 7]
            elif enemy[0] == row+3 and enemy[1] == col+1:
                if self.__matrix[row+2][col+1] != 0 and self.__matrix[row+2][col] != 0:
                    return None
                elif self.__matrix[row+2][col+1] != 0 and self.__matrix[row+2][col] == 0:
                    return [6]
                elif self.__matrix[row+1][col+1] != 0 and self.__matrix[row+2][col] != 0:
                    return [8]
                elif self.__matrix[row+1][col+1] != 0 and self.__matrix[row+2][col] == 0:
                    return [6, 8]
                elif self.__matrix[row][col+1] != 0 and self.__matrix[row+2][col] != 0:
                    return [5, 8]
                elif self.__matrix[row][col+1] != 0 and self.__matrix[row+2][col] == 0:
                    return [5, 6, 8]
                elif self.__matrix[row+2][col] != 0:
                    return [3, 5, 8]
                else:
                    return [3, 5, 6, 8]
            elif enemy[0] == row-1 and enemy[1] == col+3:
                if self.__matrix[row-1][col+2] != 0 and self.__matrix[row][col+2] != 0:
                    return None
                elif self.__matrix[row-1][col+2] != 0 and self.__matrix[row][col+2] == 0:
                    return [8]
                elif self.__matrix[row-1][col+1] != 0 and self.__matrix[row][col+2] != 0:
                    return [3]
                elif self.__matrix[row-1][col+1] != 0 and self.__matrix[row][col+2] == 0:
                    return [3, 8]
                elif self.__matrix[row-1][col] != 0 and self.__matrix[row][col+2] != 0:
                    return [2, 3]
                elif self.__matrix[row-1][col] != 0 and self.__matrix[row][col+2] == 0:
                    return [2, 3, 8]
                elif self.__matrix[row][col+2] != 0:
                    return [1, 2, 3]
                else:
                    return [1, 2, 3, 8]
            elif enemy[0] == row and enemy[1] == col+3:
                if self.__matrix[row][col+2] != 0:
                    return None
                elif self.__matrix[row][col+1] != 0:
                    return [5]
                else:
                    return [4, 5]
            elif enemy[0] == row+1 and enemy[1] == col+3:
                if self.__matrix[row+1][col+2] != 0 and self.__matrix[row][col+2] != 0:
                    return None
                elif self.__matrix[row+1][col+2] != 0 and self.__matrix[row][col+2] == 0:
                    return [3]
                elif self.__matrix[row+1][col+1] != 0 and self.__matrix[row][col+2] != 0:
                    return [8]
                elif self.__matrix[row+1][col+1] != 0 and self.__matrix[row][col+2] == 0:
                    return [3, 8]
                elif self.__matrix[row+1][col] != 0 and self.__matrix[row][col+2] != 0:
                    return [7, 8]
                elif self.__matrix[row+1][col] != 0 and self.__matrix[row][col+2] == 0:
                    return [3, 7, 8]
                elif self.__matrix[row][col+2] != 0:
                    return [6, 7, 8]
                else:
                    return [3, 6, 7, 8]
            elif (((enemy[0] >= 0 and enemy[0] < row-3) or (enemy[0] > row+3 and enemy[0] < self._rowlen)) and (enemy[1] >= col-1 and enemy[1] <= col+1)) or (((enemy[1] >= 0 and enemy[1] < col-3) or (enemy[1] > col+3 and enemy[1] < self._collen)) and (enemy[0] >= row-1 and enemy[0] <= row+1)):
                if enemy[0] == row-1:
                    if  enemy[1] < col-1:
                        for x in range(enemy[1]+1, col-1):
                            if self.__matrix[row-1][x] != 0:
                                return None
                        if self.__matrix[row-1][col-1] != 0:
                            return [1]
                        elif self.__matrix[row-1][col] != 0:
                            return [1, 2]
                    elif enemy[1] > col+1:
                        for x in range(col+2, enemy[1]):
                            if self.__matrix[row-1][x] != 0:
                                return None
                        if self.__matrix[row-1][col+1] != 0:
                            return [3]
                        elif self.__matrix[row-1][col] != 0:
                            return [2, 3]
                    return [1, 2, 3]
                elif enemy[0] == row:
                    if  enemy[1] < col-1:
                        for x in range(enemy[1]+1, col-1):
                            if self.__matrix[row][x] != 0:
                                return None
                        if self.__matrix[row][col-1] != 0:
                            return [4]
                    elif enemy[1] > col+1:
                        for x in range(col+2, enemy[1]):
                            if self.__matrix[row][x] != 0:
                                return None
                        if self.__matrix[row][col+1] != 0:
                            return [5]
                    return [4, 5]
                elif enemy[0] == row+1:
                    if enemy[1] < col-1:
                        for x in range(enemy[1]+1, col-1):
                            if self.__matrix[row+1][x] != 0:
                                return None
                        if self.__matrix[row+1][col-1] != 0:
                            return [6]
                        elif self.__matrix[row+1][col] != 0:
                            return [6, 7]
                    elif enemy[1] > col+1:
                        for x in range(col+2, enemy[1]):
                            if self.__matrix[row+1][x] != 0:
                                return None
                        if self.__matrix[row+1][col+1] != 0:
                            return [8]
                        elif self.__matrix[row+1][col] != 0:
                            return [7, 8]
                    return [6, 7, 8]
                elif enemy[1] == col-1:
                    if enemy[0] < row-1:
                        for x in range(enemy[0]+1, row-1):
                            if self.__matrix[x][col-1] != 0:
                                return None
                        if self.__matrix[row-1][col-1] != 0:
                            return [1]
                        elif self.__matrix[row][col-1] != 0:
                            return [1, 4]
                    elif enemy[0] > row+1:
                        for x in range(row+2, enemy[0]):
                            if self.__matrix[x][col-1] != 0:
                                return None
                        if self.__matrix[row+1][col-1] != 0:
                            return [6]
                        elif self.__matrix[row][col-1] != 0:
                            return [4, 6]
                    return [1, 4, 6]
                elif enemy[1] == col:
                    if enemy[0] < row-1:
                        for x in range(enemy[0]+1, row-1):
                            if self.__matrix[x][col] != 0:
                                return None
                        if self.__matrix[row-1][col] != 0:
                            return [2]
                    elif enemy[0] > row+1:
                        for x in range(row+2, enemy[0]):
                            if self.__matrix[x][col] != 0:
                                return None
                        if self.__matrix[row+1][col] != 0:
                            return [7]
                    return [2, 7]
                elif enemy[1] == col+1:
                    if enemy[0] < row-1:
                        for x in range(enemy[0]+1, row-1):
                            if self.__matrix[x][col+1] != 0:
                                return None
                        if self.__matrix[row-1][col+1] != 0:
                            return [3]
                        elif self.__matrix[row][col+1] != 0:
                            return [3, 5]
                    elif enemy[0] > row+1:
                        for x in range(row+2, enemy[0]):
                            if self.__matrix[x][col+1] != 0:
                                return None
                        if self.__matrix[row+1][col+1] != 0:
                            return [8]
                        elif self.__matrix[row][col+1] != 0:
                            return [5, 8]
                    return [3, 5, 8]
            else:
                if enemy[0] != (row-1) and enemy[1] != (col-1) and abs(enemy[0]-(row-1)) == abs(enemy[1]-(col-1)):
                    if enemy[0] != (row+1) and enemy[1] != (col+1) and abs(enemy[0]-(row+1)) == abs(enemy[1]-(col+1)):
                        if enemy[0] < (row-1) and enemy[1] < (col-1):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]+x][enemy[1]+x] != 0:
                                    return None
                            if self.__matrix[row-1][col-1] != 0:
                                return [1]
                        elif enemy[0] > (row+1) and enemy[1] > (col+1):
                            for x in range(1, abs(enemy[0]-(row+1))):
                                if self.__matrix[enemy[0]-x][enemy[1]-x] != 0:
                                    return None
                            if self.__matrix[row+1][col+1] != 0:
                                return [8]
                        return [1, 8]
                    else:
                        if enemy[0] < (row-1) and enemy[1] > (col-1):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]+x][enemy[1]-x] != 0:
                                    return None
                        elif enemy[0] > (row-1) and enemy[1] < (col-1):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]-x][enemy[1]+x] != 0:
                                    return None
                        return [1]
                elif enemy[0] != (row-1) and enemy[1] != (col) and abs(enemy[0]-(row-1)) == abs(enemy[1]-(col)):
                    if enemy[0] != (row) and enemy[1] != (col+1) and abs(enemy[0]-(row)) == abs(enemy[1]-(col+1)):
                        if enemy[0] < (row-1) and enemy[1] < (col):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]+x][enemy[1]+x] != 0:
                                    return None
                            if self.__matrix[row-1][col] != 0:
                                return [2]
                        elif enemy[0] > (row) and enemy[1] > (col+1):
                            for x in range(1, abs(enemy[0]-row)):
                                if self.__matrix[enemy[0]-x][enemy[1]-x] != 0:
                                    return None
                            if self.__matrix[row][col+1] != 0:
                                return [5]
                        return [2, 5]
                    elif enemy[0] != (row) and enemy[1] != (col-1) and abs(enemy[0]-(row)) == abs(enemy[1]-(col-1)):
                        if enemy[0] < (row-1) and enemy[1] > (col):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]+x][enemy[1]-x] != 0:
                                    return None
                            if self.__matrix[row-1][col] != 0:
                                return [2]
                        elif enemy[0] > (row) and enemy[1] < (col-1):
                            for x in range(1, abs(enemy[0]-row)):
                                if self.__matrix[enemy[0]-x][enemy[1]+x] != 0:
                                    return None
                            if self.__matrix[row][col-1] != 0:
                                return [4]
                        return [2, 4]
                elif enemy[0] != (row-1) and enemy[1] != (col+1) and abs(enemy[0]-(row-1)) == abs(enemy[1]-(col+1)):
                    if enemy[0] != (row+1) and enemy[1] != (col-1) and abs(enemy[0]-(row+1)) == abs(enemy[1]-(col-1)):
                        if enemy[0] < (row-1) and enemy[1] > (col+1):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]+x][enemy[1]-x] != 0:
                                    return None
                            if self.__matrix[row-1][col+1] != 0:
                                return [3]
                        elif enemy[0] > (row+1) and enemy[1] < (col-1):
                            for x in range(1, abs(enemy[0]-(row+1))):
                                if self.__matrix[enemy[0]-x][enemy[1]+x] != 0:
                                    return None
                            if self.__matrix[row+1][col-1] != 0:
                                return [6]
                        return [3, 6]
                    else:
                        if enemy[0] < (row-1) and enemy[1] < (col+1):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]+x][enemy[1]+x] != 0:
                                    return None
                        elif enemy[0] > (row-1) and enemy[1] > (col+1):
                            for x in range(1, abs(enemy[0]-(row-1))):
                                if self.__matrix[enemy[0]-x][enemy[1]-x] != 0:
                                    return None
                        return [3]
                elif enemy[0] != (row) and enemy[1] != (col-1) and abs(enemy[0]-(row)) == abs(enemy[1]-(col-1)):
                    if enemy[0] != (row+1) and enemy[1] != (col) and abs(enemy[0]-(row+1)) == abs(enemy[1]-(col)):
                        if enemy[0] < (row) and enemy[1] < (col-1):
                            for x in range(1, abs(enemy[0]-row)):
                                if self.__matrix[enemy[0]+x][enemy[1]+x] != 0:
                                    return None
                            if self.__matrix[row-1][col] != 0:
                                return [4]
                        elif enemy[0] > (row+1) and enemy[1] > (col):
                            for x in range(1, abs(enemy[0]-row)):
                                if self.__matrix[enemy[0]-x][enemy[1]-x] != 0:
                                    return None
                            if self.__matrix[row+1][col] != 0:
                                return [7]
                        return [4, 7]
                elif enemy[0] != (row) and enemy[1] != (col+1) and abs(enemy[0]-(row)) == abs(enemy[1]-(col+1)):
                    if enemy[0] != (row+1) and enemy[1] != (col) and abs(enemy[0]-(row+1)) == abs(enemy[1]-(col)):
                        if enemy[0] < (row) and enemy[1] > (col+1):
                            for x in range(1, abs(enemy[0]-row)):
                                if self.__matrix[enemy[0]+x][enemy[1]-x] != 0:
                                    return None
                            if self.__matrix[row][col+1] != 0:
                                return [5]
                        elif enemy[0] > (row+1) and enemy[1] < (col):
                            for x in range(1, abs(enemy[0]-row)):
                                if self.__matrix[enemy[0]-x][enemy[1]+x] != 0:
                                    return None
                            if self.__matrix[row+1][col] != 0:
                                return [7]
                        return [5, 7]
                elif enemy[0] != (row+1) and enemy[1] != (col-1) and abs(enemy[0]-(row+1)) == abs(enemy[1]-(col-1)):
                    if enemy[0] < (row+1) and enemy[1] < (col-1):
                        for x in range(1, abs(enemy[0]-(row+1))):
                            if self.__matrix[enemy[0]+x][enemy[1]+x] != 0:
                                return None
                    elif enemy[0] > (row+1) and enemy[1] > (col-1):
                        for x in range(1, abs(enemy[0]-(row+1))):
                            if self.__matrix[enemy[0]-x][enemy[1]-x] != 0:
                                return None
                    return [6]
                elif enemy[0] != (row+1) and enemy[1] != (col+1) and abs(enemy[0]-(row+1)) == abs(enemy[1]-(col+1)):
                    if enemy[0] < (row+1) and enemy[1] > (col+1):
                        for x in range(1, abs(enemy[0]-(row+1))):
                            if self.__matrix[enemy[0]+x][enemy[1]-x] != 0:
                                return None
                    elif enemy[0] > (row+1) and enemy[1] < (col+1):
                        for x in range(1, abs(enemy[0]-(row+1))):
                            if self.__matrix[enemy[0]-x][enemy[1]+x] != 0:
                                return None
                    return [8]
        elif self.__matrix[enemy[0]][enemy[1]] == 6:
            if enemy[0] == row-2 and enemy[1] == col-2:
                return [1]
            elif enemy[0] == row-2 and enemy[1] == col-1:
                return [1, 2]
            elif enemy[0] == row-2 and enemy[1] == col:
                return [1, 2, 3]
            elif enemy[0] == row-2 and enemy[1] == col+1:
                return [2, 3]
            elif enemy[0] == row-2 and enemy[1] == col+2:
                return [3]
            elif enemy[0] == row-1 and enemy[1] == col-2:
                return [1, 4]
            elif enemy[0] == row-1 and enemy[1] == col-1:
                return [2, 4]
            elif enemy[0] == row-1 and enemy[1] == col:
                return [1, 3, 4, 5]
            elif enemy[0] == row-1 and enemy[1] == col+1:
                return [2, 5]
            elif enemy[0] == row-1 and enemy[1] == col+2:
                return [3, 5]
            elif enemy[0] == row and enemy[1] == col-2:
                return [1, 4, 6]
            elif enemy[0] == row and enemy[1] == col-1:
                return [1, 2, 6, 7]
            elif enemy[0] == row and enemy[1] == col+1:
                return [2, 3, 7, 8]
            elif enemy[0] == row and enemy[1] == col+2:
                return [3, 5, 8]
            elif enemy[0] == row+1 and enemy[1] == col-2:
                return [4, 6]
            elif enemy[0] == row+1 and enemy[1] == col-1:
                return [4, 7]
            elif enemy[0] == row+1 and enemy[1] == col:
                return [4, 5, 6, 8]
            elif enemy[0] == row+1 and enemy[1] == col+1:
                return [5, 7]
            elif enemy[0] == row+1 and enemy[1] == col+2:
                return [5, 8]
            elif enemy[0] == row+2 and enemy[1] == col-2:
                return [6]
            elif enemy[0] == row+2 and enemy[1] == col-1:
                return [6, 7]
            elif enemy[0] == row+2 and enemy[1] == col:
                return [6, 7, 8]
            elif enemy[0] == row+2 and enemy[1] == col+1:
                return [7, 8]
            elif enemy[0] == row+2 and enemy[1] == col+2:
                return [8]
    
    # check if check then get the only positions where it can only move
    def _check(self):
        encounter = 0
        check_box = {}
        kr, kc = self.__king
        for x in self.__bot:
            r, c = x
            steps = []
            list1 = {}
            if self.__matrix[r][c] == 1:
                if r + 1 == kr and c - 1 == kc:
                    check_box[(r, c)] = True
                    encounter += 1
                elif r + 1 == kr and c + 1 == kc:
                    check_box[(r, c)] = True
                    encounter += 1
            elif self.__matrix[r][c] == 2:
                if (abs(r - kr) == 1 and abs(c - kc) == 2) or (abs(r - kr) == 2 and abs(c - kc) == 1):
                    check_box[(r, c)] = True
                    encounter += 1
            elif self.__matrix[r][c] == 3:
                if kr - r == kc - c > 0:
                    steps = [1, 1]
                elif r - kr == kc - c > 0:
                    steps = [-1, 1]
                elif kr - r == c - kc > 0:
                    steps = [1, -1]
                elif r - kr == c - kc > 0:
                    steps = [-1, -1]
            elif self.__matrix[r][c] == 4:
                if r == kr and c < kc:
                    steps = [0, 1]
                elif r == kr and c > kc:
                    steps = [0, -1]
                elif r < kr and c == kc:
                    steps = [1, 0]
                elif r > kr and c == kc:
                    steps = [-1, 0]
            elif self.__matrix[r][c] == 5:
                if kr - r == kc - c > 0:
                    steps = [1, 1]
                elif r - kr == kc - c > 0:
                    steps = [-1, 1]
                elif kr - r == c - kc > 0:
                    steps = [1, -1]
                elif r - kr == c - kc > 0:
                    steps = [-1, -1]
                elif r == kr and c < kc:
                    steps = [0, 1]
                elif r == kr and c > kc:
                    steps = [0, -1]
                elif r < kr and c == kc:
                    steps = [1, 0]
                elif r > kr and c == kc:
                    steps = [-1, 0]
            elif self.__matrix[r][c] == 6:
                continue
            # Sliding pieces: Bishop, Rook, Queen
            if len(steps) == 2:
                list1[(r, c)] = True
                row = r + steps[0]
                col = c + steps[1]
                while 0 <= row < self._rowlen and 0 <= col < self._collen:
                    if self.__matrix[row][col] == 0:
                        list1[(row, col)] = True
                    elif self.__matrix[row][col] == 12:
                        encounter += 1
                        break
                    else:
                        list1.clear()
                        break
                    row += steps[0]
                    col += steps[1]
                if list1:
                    check_box = list1.copy()
            # if more than one encounter occur with the king then king will only move in the board
            if encounter == 2:
                return {}, True
        if encounter == 1:
            return check_box, False
        else:
            return {}, False
    
    # gives the result as iterable when the class is been created as an object
    def __iter__(self):
        list1 = []
        if self._can_move(self.__matrix, self.__king):
            list1.extend(self._king(*self.__king))
            check_box, king_only = self._check()
            if not king_only:
                self.__check = check_box
            # castling check
            if not check_box and not king_only:
                s = {item for e in self.__bot for result in [self._filterEnemy((e, self.__king[0], self.__king[1]))] if result for item in result if item in (4, 5)}
                if len(s) != 2:
                    pos_castle = []
                    for i in self.__castle:
                        if 4 not in s and i < self.__king[1]:
                            list1.extend(self._castling(i))
                        elif 5 not in s and i > self.__king[1]:
                            list1.extend(self._castling(i))
        for x in self.__player:
            if self._can_move(self.__matrix, x):
                row, col = x
                if self.__matrix[row][col] == 7:
                    list1.extend(self._pawn(row, col))
                elif self.__matrix[row][col] == 8:
                    list1.extend(self._knight(row, col))
                elif self.__matrix[row][col] == 9:
                    list1.extend(self._bishop(row, col))
                elif self.__matrix[row][col] == 10:
                    list1.extend(self._rook(row, col))
                elif self.__matrix[row][col] == 11:
                    list1.extend(self._queen(row, col))
        return iter(list1)

    # castling
    def _castling(self, pos):
        list1 = []
        king_row, king_col = self.__king
        # checking the path is empty or not in between rook and king for castling
        if pos > king_col:
            if king_col >= self._collen - 2:
                castle = False
            else:
                castle = all(self.__matrix[king_row][col] == 0 for col in range(king_col + 1, pos))
        elif pos < king_col:
            if king_col <= 1:
                castle = False
            else:
                castle = all(self.__matrix[king_row][col] == 0 for col in range(pos + 1, king_col))
        else:
            castle = False
        # if castling is possible then check after castling any check occurs
        if castle:
            matrix = self.__matrix
            if pos > self.__king[1]:
                king_next = king_col + 2
                rook_next = king_col + 1
            elif pos < self.__king[1]:
                king_next = king_col - 2
                rook_next = king_col - 1    
            # temporary peices moving
            matrix[king_row][rook_next] = 10
            matrix[king_row][pos] = 0
            matrix[king_row][king_next] = 12
            matrix[king_row][king_col] = 0
            self.__king = (king_row, king_next)
            check_box, king_only = self._check()
            if not check_box and not king_only:
                list1.append([king_row, king_col, king_row, king_next, None])
            # restore peices
            matrix[king_row][king_col] = 12
            matrix[king_row][king_next] = 0
            matrix[king_row][pos] = 10
            matrix[king_row][rook_next] = 0
            self.__king = (king_row, king_col)
        return list1

    # chessmen moves
    def _pawn(self, row, col):
        list1 = []
        if row > 0:
            if row == self._rowlen - 2:
                if (self.__matrix[row - 1][col] == 0 and self.__matrix[row - 2][col] == 0):
                    list1 = [node for x in [1, 2] for change in ([8, 9, 10, 11] if row - x == 0 else [None]) if (node := self._make_node([row, col, row - x, col], self.__check, change)) is not None]
                elif (self.__matrix[row - 1][col] == 0 and self.__matrix[row - 2][col] != 0):
                    list1 = [node for change in ([8, 9, 10, 11] if row - 1 == 0 else [None]) if (node := self._make_node([row, col, row - 1, col], self.__check, change)) is not None]
            else:
                if (self.__matrix[row - 1][col] == 0):
                    list1 = [node for change in ([8, 9, 10, 11] if row - 1 == 0 else [None]) if (node := self._make_node([row, col, row - 1, col], self.__check, change)) is not None]
            if col - 1 >= 0:
                if (self.__matrix[row - 1][col - 1] != 0 and self.__matrix[row - 1][col - 1] <= 6):
                    list1.extend([node for change in ([8, 9, 10, 11] if row - 1 == 0 else [None]) if (node := self._make_node([row, col, row - 1, col - 1], self.__check, change)) is not None])
            if col + 1 < self._collen:
                if (self.__matrix[row - 1][col + 1] != 0 and self.__matrix[row - 1][col + 1] <= 6):
                    list1.extend([node for change in ([8, 9, 10, 11] if row - 1 == 0 else [None]) if (node := self._make_node([row, col, row - 1, col + 1], self.__check, change)) is not None])
        return list1
    
    def _knight(self, row, col):
        list1 = []
        moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        for dr, dc in moves:
            r = row + dr
            c = col + dc
            if (0 <= r < self._rowlen and 0 <= c < self._collen and self.__matrix[r][c] < 7):
                if (node := self._make_node([row, col, r, c], self.__check, None)) is not None: list1.append(node)
        return list1
    
    def _bishop(self, row, col):
        directions = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
        list1 = []
        for dr, dc in directions:
            list1.extend(self._slide(row, col, dr, dc))
        return list1
    
    def _rook(self, row, col):
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        list1 = []
        for dr, dc in directions:
            list1.extend(self._slide(row, col, dr, dc))
        return list1
    
    def _queen(self, row, col):
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]
        list1 = []
        for dr, dc in directions:
            list1.extend(self._slide(row, col, dr, dc))
        return list1
    
    def _king(self, row, col):
        list1 = []
        s = {item for e in self.__bot for result in [self._filterEnemy((e, row, col))] if result for item in result}
        index = [i + 1 not in s for i in range(8)]
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1),  (1, 0),  (1, 1)]
        for i, (dr, dc) in enumerate(directions):
            r = row + dr
            c = col + dc
            if (0 <= r < self._rowlen and 0 <= c < self._collen and self.__matrix[r][c] < 7 and index[i]):
                list1.append([row, col, r, c, None])
        return list1


# if __name__ == "__main__":
#     matrix = [
#         [0, 0, 0, 6],
#         [0, 0, 0, 0],
#         [1, 0, 0, 0],
#         [10, 7, 12, 0]
#     ]
#     rowlen = len(matrix)
#     collen = len(matrix[0])
    
#     def make_matrix_data(matrix):
#         meta_data = {}
#         meta_data["points"] = 0
#         meta_data["matrix"] = matrix
#         meta_data["bot"] = {}
#         meta_data["player"] = {}
#         meta_data["castling"] = {"bot": [], "player": []}
#         for i in range(rowlen):
#             for j in range(collen):
#                 if 0 < matrix[i][j] <= 6:
#                     meta_data["bot"][(i, j)] = matrix[i][j]
#                     if matrix[i][j] == 6:
#                         meta_data["bot_king"] = (i, j)
#                     # castling
#                     elif matrix[i][j] == 4 and (j == 0 or j == collen - 1):
#                         meta_data["castling"]["bot"].append((i, j))
#                     # castling
#                 elif 7 <= matrix[i][j] <= 12:
#                     meta_data["player"][(i, j)] = matrix[i][j]
#                     if matrix[i][j] == 12:
#                         meta_data["player_king"] = (i, j)
#                     # castling
#                     elif matrix[i][j] == 10 and (j == 0 or j == collen - 1):
#                         meta_data["castling"]["player"].append((i, j))
#         meta_data["castling"]["bot"] = [rook[1] for rook in meta_data["castling"]["bot"] if rook[0] == meta_data["bot_king"][0]]
#         meta_data["castling"]["player"] = [rook[1] for rook in meta_data["castling"]["player"] if rook[0] == meta_data["player_king"][0]]
#         pprint(meta_data)
#         return meta_data
    
#     pprint(list(BotChessman(make_matrix_data(matrix))))