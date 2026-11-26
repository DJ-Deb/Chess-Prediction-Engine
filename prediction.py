from chessman import PlayerChessman, BotChessman
from storageProcessing import MovesStorage
import copy

# ============================================================
# POINT TABLE
# ------------------------------------------------------------
# Piece       Bot Value    Player Value
# ------------------------------------------------------------
# Pawn           1             7
# Knight         2             8
# Bishop         3             9
# Rook           4            10
# Queen          5            11
# King           6            12
# ============================================================

# Bot kills Player:
# Player Pawn    (7)  -> +1 point
# Player Knight  (8)  -> +2 points
# Player Bishop  (9)  -> +3 points
# Player Rook   (10)  -> +4 points
# Player Queen  (11)  -> +5 points
# Player King   (12)  -> 2 x init_points

# Player kills Bot:
# Bot Pawn       (1)  -> -1 point
# Bot Knight     (2)  -> -2 points
# Bot Bishop     (3)  -> -3 points
# Bot Rook       (4)  -> -4 points
# Bot Queen      (5)  -> -5 points
# Bot King       (6)  -> -2 x init_points

# ------------------------------------------------------------
# Pawn Promotion
# ------------------------------------------------------------
# When a Pawn reaches the opposite end of the board,
# its piece value changes according to the promoted piece.
#
# Bot Pawn (1):
#     Queen  -> 5
#     Rook   -> 4
#     Bishop -> 3
#     Knight -> 2
#
# Player Pawn (7):
#     Queen  -> 11
#     Rook   -> 10
#     Bishop -> 9
#     Knight -> 8
# ============================================================


def one_integer_to_five_elements(value: int, pos_factor: int) -> list:
    '''
        Decodes a single integer back into a chess move and piece.
        \n\tParameters:
        \n\tvalue (int): Encoded integer containing the move coordinates and the piece code.
        \nReturns:
        \n\tlist: [old_row, old_col, new_row, new_col, piece]
        \nPiece mapping:
        \n\t0 -> None
        \n\t1 -> 2
        \n\t2 -> 5
        \n\t3 -> 8
        \n\t4 -> 9
        \n\t5 -> 10
        \n\t6 -> 11
        \nEncoding format:
        \n\tThe last 3 bits store the piece code.
        \n\tThe remaining bits store the encoded position.
        \nDecoding:
        \n\tvalue & 7  -> extracts the piece code
        \n\tvalue >> 3 -> extracts the encoded position
     '''
    n = pos_factor

    piece_code = value & 7
    position = value >> 3

    old_row = position % n
    position //= n

    old_col = position % n
    position //= n

    new_row = position % n
    position //= n

    new_col = position % n

    code_to_piece = {
        0: None,
        1: 2,
        2: 5,
        3: 8,
        4: 9,
        5: 10,
        6: 11
    }

    piece = code_to_piece[piece_code]

    return [old_row, old_col, new_row, new_col, piece]

def five_elements_to_one_integer(self, move: list, pos_factor: int) -> int:
    change_code = {None: 0, 2: 1, 5: 2, 8: 3, 9: 4, 10: 5, 11: 6}
    old_row, old_col, new_row, new_col, change = move
    n = pos_factor
    code = change_code[change]
    position = (old_row + old_col * n + new_row * n**2 + new_col * n**3)
    return (position << 3) | code


class __Tools:
    def __init__(self, pos_factor: int, init_point: int):
        # calculation config
        self.__pos_factor = pos_factor
        self.__init_point = init_point

        # previous move point
        self.prev_points = 0

    # admin
    __setup_admin = False
    __admin_dict = {}

    # make node
    def _make_node(self, points: list, matrix_data: list, moved: list) -> dict:
        if self.__setup_admin:
            self.__setup_admin_dict(moved[0], points, None, steps_to_checkmate=None)
        
        return {
            "points_table": points,
            "stop": False,
            "matrix_data": matrix_data,
            "moved": moved
        }

    def _database_partition(self, cut_moved: bool, matrix: list, database_object: MovesStorage) -> set:
        data = {}
        key_list = set()
        for node in matrix:
            if cut_moved:
                node["moved"] = node["moved"][2:]
                node["points_table"] = node["points_table"][2:]
            
            result = "-".join(map(str, node["moved"][:2]))
            key_list.add(result)
            if result not in data:
                data[result] = [node]
            else:
                data[result].append(node)
        database_object.insert_many(data)
        return key_list

    def _start_setup_admin(self):
        self.__setup_admin = True

    def __reset_setup_admin(self):
        self.__setup_admin = False
        self.__admin_dict = {}

    def _toggle_checkmate_point(self, move: list, points: list, bot_side: bool, steps_to_checkmate: int):
        if self.__setup_admin:
            self.__setup_admin_dict(move, points, bot_side, steps_to_checkmate)

    def __setup_admin_dict(self, move: list, points: list, bot_side: bool, steps_to_checkmate: int):
        if move in self.__admin_dict:
            self.__update_admin_dict(move, points[-1], bot_side, steps_to_checkmate)
        else:
            self.__admin_dict[move] = {
                # points data
                "next": points[0] - self.prev_points if self.prev_points != 0 else points[0] - self.__init_point if points[0] != 0 else 0,
                "max": points[-1],
                "min": points[-1],

                # bot meta data
                "bot_checkmate_step": 0 if bot_side == None else steps_to_checkmate if not bot_side else 0,
                "bot_num_checkmate": 0 if bot_side == None else 1 if not bot_side else 0,

                # player meta data
                "player_checkmate_step": 0 if bot_side == None else steps_to_checkmate if bot_side else 0,
                "player_num_checkmate": 0 if bot_side == None else 1 if bot_side else 0,
            }

    def __update_admin_dict(self, move: list, points: int, bot_side: bool, steps_to_checkmate: int):
        # update the max point
        if self.__admin_dict[move]["max"] < points:
            self.__admin_dict[move]["max"] = points
        
        # update the min point
        if points != 0 and (self.__admin_dict[move]["min"] == 0 or self.__admin_dict[move]["min"] > points):
            self.__admin_dict[move]["min"] = points
        
        # update the checkmate (lowest number of steps moved for checkmate)
        if bot_side != None:
            if not bot_side:
                if self.__admin_dict[move]["bot_checkmate_step"] == 0 or self.__admin_dict[move]["bot_checkmate_step"] > steps_to_checkmate:
                    self.__admin_dict[move]["bot_checkmate_step"] = steps_to_checkmate
                self.__admin_dict[move]["bot_num_checkmate"] += 1
            else:
                if self.__admin_dict[move]["player_checkmate_step"] == 0 or self.__admin_dict[move]["player_checkmate_step"] > steps_to_checkmate:
                    self.__admin_dict[move]["player_checkmate_step"] = steps_to_checkmate
                self.__admin_dict[move]["player_num_checkmate"] += 1

    def _get_best_move(self) -> int:
        best_move = self.__best_move_selection_by_priority()
        if self.__only_one_best_move(best_move=best_move):
            return best_move.pop()
        best_move = self.__best_move_selection_by_min_max(best_move=best_move)
        if self.__only_one_best_move(best_move=best_move):
            return best_move.pop()
        best_move = self.__best_move_selection_by_checkmate_closest_step(best_moves=best_move)
        if self.__only_one_best_move(best_move=best_move):
            return best_move.pop()
        best_move = self.__best_move_selection_by_next_move(best_move=best_move)
        if self.__only_one_best_move(best_move=best_move):
            return best_move.pop()
        best_move = self.__best_move_selection_by_checkmate_ratio(best_move=best_move)

        self.__reset_setup_admin()
        return best_move.pop()
    
    def __only_one_best_move(self, best_move: set) -> bool:
        if len(best_move) == 0:
            self.__reset_setup_admin()
            return True

    def __best_move_selection_by_priority(self) -> set:
        moves = set()
        eliminate_move = set()
        for key, value in self.__admin_dict.items():
            if value["bot_checkmate_step"] == 1:
                return {key}
            
            # eliminate the queen
            if value["next"] == 5:
                eliminate_move.add(key)
            else:
                moves.add(key)

        if len(eliminate_move) != 0:
            return eliminate_move
        else:
            return moves

    def __best_move_selection_by_min_max(self, best_move: set) -> set:
        top_bot = None
        top_player = None
        top_moves = set()
        for key in best_move:
            bot_side = abs(self.__admin_dict[key]["max"] - self.__init_point) if self.__admin_dict[key]["max"] != 0 else 0
            player_side = abs(self.__admin_dict[key]["min"] - self.__init_point) if self.__admin_dict[key]["min"] != 0 else 0

            # handle initial
            if top_bot == None and top_player == None:
                top_bot = bot_side
                top_player = player_side
                top_moves.add(key)
                continue

            # top moves set
            if top_bot == bot_side and top_player >= player_side:
                top_moves.add(key)
            elif top_bot < bot_side:
                top_bot = bot_side
                top_player = player_side
                top_moves.clear()
                top_moves.add(key)
        
        return top_moves

    def __best_move_selection_by_checkmate_closest_step(self, best_moves: set) -> set:
        bot_step = None
        player_step = None
        top_moves = set()
        for key in best_moves:
            cur_bot_step = self.__admin_dict[key]["bot_checkmate_step"]
            cur_player_step = self.__admin_dict[key]["player_checkmate_step"]

            # handle initial
            if bot_step == None:
                bot_step = cur_bot_step
                player_step = cur_player_step
                top_moves.add(key) 
                continue

            # set top moves
            if bot_step == 0 and player_step == 0:
                if cur_bot_step == 0 and cur_player_step == 0:
                    top_moves.add(key)
                elif cur_bot_step != 0 and cur_player_step ==0:
                    bot_step = cur_bot_step
                    player_step = cur_player_step
                    top_moves.clear()
                    top_moves.add(key)
                elif cur_bot_step != 0 and cur_bot_step < cur_player_step:
                    bot_step = cur_bot_step
                    player_step = cur_player_step
                    top_moves.clear()
                    top_moves.add(key)
            elif bot_step != 0 and player_step == 0:
                if cur_bot_step != 0 and cur_player_step == 0:
                    top_moves.add(key)
                elif cur_bot_step != 0 and cur_bot_step < cur_player_step:
                    bot_step = cur_bot_step
                    player_step = cur_player_step
                    top_moves.clear()
                    top_moves.add(key)
            elif bot_step != 0 and player_step != 0 and bot_step < player_step:
                if cur_bot_step != 0 and cur_bot_step < cur_player_step:
                    top_moves.add(key)
            elif bot_step != 0 and player_step != 0 and bot_step > player_step:
                if cur_bot_step == 0 and cur_player_step == 0:
                    bot_step = cur_bot_step
                    player_step = cur_player_step
                    top_moves.clear()
                    top_moves.add(key)
                elif cur_bot_step != 0 and cur_player_step == 0:
                    bot_step = cur_bot_step
                    player_step = cur_player_step
                    top_moves.clear()
                    top_moves.add(key)
                elif cur_bot_step != 0 and cur_bot_step < cur_player_step:
                    bot_step = cur_bot_step
                    player_step = cur_player_step
                    top_moves.clear()
                    top_moves.add(key)
                elif cur_bot_step != 0 and cur_bot_step > cur_player_step:
                    if cur_bot_step == bot_step and cur_player_step >= player_step:
                        top_moves.add(key)
                    elif cur_bot_step < bot_step and cur_player_step >= player_step:
                        bot_step = cur_bot_step
                        player_step = cur_player_step
                        top_moves.clear()
                        top_moves.add(key)
        return top_moves
        
    def __best_move_selection_by_next_move(self, best_move: set) -> set:
        top_next_move = None
        top_move = set()
        for key in best_move:
            next_move = self.__admin_dict[key]["next"]

            # handle initial
            if top_next_move == None:
                top_next_move = next_move
                top_move.add(key)
                continue

            # top move set
            if top_next_move == next_move:
                top_move.add(key)
            elif top_next_move < next_move:
                top_next_move = next_move
                top_move.clear()
                top_move.add(key)

        return top_move

    def __best_move_selection_by_checkmate_ratio(self, best_move: set) -> set:
        top_ratio = None
        top_move = set()
        for key in best_move:
            ratio = self.__admin_dict[key]["bot_num_checkmate"] - self.__admin_dict[key]["player_num_checkmate"]

            # handle initial
            if top_ratio == None:
                top_ratio = ratio
                top_move.add(key)
                continue

            # top move set
            if top_ratio == ratio:
                top_move.add(key)
            elif top_ratio < ratio:
                top_ratio = ratio
                top_move.clear()
                top_move.add(key)
        
        return top_move

    # convert the four elements [old_row, old_col, new_row, new_col] and piece change into one integer for storage
    __change_code = {None: 0, 2: 1, 5: 2, 8: 3, 9: 4, 10: 5, 11: 6}
    def _five_elements_to_one_integer(self, move: list) -> int:
        old_row, old_col, new_row, new_col, change = move
        n = self.__pos_factor
        change_code = self.__change_code[change]
        position = (old_row + old_col * n + new_row * n**2 + new_col * n**3)
        return (position << 3) | change_code

class __Calculate(__Tools):
    def __init__(self, rowlen: int, collen: int, init_point: int):
        # this will store the next matrix data after each move for the bot and player
        self.__next_matrix_data = {}

        # calculation config
        self.__rowlen = rowlen
        self.__collen = collen
        self.__initial_point = init_point
        super().__init__(self.__rowlen if self.__rowlen >= self.__collen else self.__collen, init_point)

    # enlist the each moves and update it for next possible matrix
    def _move_chessman(self, matrix_data: dict, moves: list, last_moved: list, points_list: list, bot_side: bool) -> list:
        temp_next_matrix_data = []
        for pos in moves:
            new_last_moved = copy.deepcopy(last_moved)
            new_last_moved.append(self._five_elements_to_one_integer(pos))
            
            new_matrix_data = copy.deepcopy(matrix_data)
            
            if bot_side:
                self.__perform_bot_move(new_matrix_data, pos)
            else:
                self.__perform_player_move(new_matrix_data, pos)

            new_point_list = copy.deepcopy(points_list)
            new_point_list.append(new_matrix_data["points"])

            temp_next_matrix_data.append(self._make_node(points=new_point_list, matrix_data=new_matrix_data, moved=new_last_moved))
        return temp_next_matrix_data

    # perform a single move for the bot on the chessboard and update the matrix data
    def __perform_bot_move(self, matrix_data: dict, move: list):
        old_row, old_col, new_row, new_col, change = move
        matrix = matrix_data["matrix"]

        # ---------------------------------------------------------
        # Capture player piece
        # ---------------------------------------------------------

        if (new_row, new_col) in matrix_data["player"]:
            captured_piece = matrix_data["player"].pop((new_row, new_col))
            # handle castling data of player for next
            if captured_piece == 10 and new_row == matrix_data["player_king"][0] and new_col in matrix_data["castling"]["player"]:
                matrix_data["castling"]["player"].remove(new_col)
            # handle the points
            if matrix_data["points"] == 0:
                matrix_data["points"] = self.__initial_point
            matrix_data["points"] = matrix_data["points"] + (captured_piece - 6)

        # ---------------------------------------------------------
        # Bot matrix update
        # ---------------------------------------------------------

        # handle bot king movement
        if matrix[old_row][old_col] == 6:
            # castling
            if abs(new_col - old_col) == 2:
                # left side castling
                if old_col > new_col:
                    matrix_data["bot"].pop((old_row, 0))
                    matrix_data["bot"][(old_row, old_col - 1)] = 4
                    matrix[old_row][old_col - 1] = 4
                    matrix[old_row][0] = 0
                # right side castling
                elif old_col < new_col:
                    matrix_data["bot"].pop((old_row, self.__collen - 1))
                    matrix_data["bot"][(old_row, old_col + 1)] = 4
                    matrix[old_row][old_col + 1] = 4
                    matrix[old_row][self.__collen - 1] = 0
            matrix_data["bot_king"] = (new_row, new_col)
            matrix_data["castling"]["bot"] = []
        # handle castling by rook
        elif matrix[old_row][old_col] == 4 and old_row == matrix_data["bot_king"][0] and old_col in matrix_data["castling"]["bot"]:
            matrix_data["castling"]["bot"].remove(old_col)
        
        # ---------------------------------------------------------
        # Move bot piece
        # ---------------------------------------------------------

        matrix_data["bot"].pop((old_row, old_col))
        if change is None:
            matrix_data["bot"][(new_row, new_col)] = matrix[old_row][old_col]
        else:
            matrix_data["bot"][(new_row, new_col)] = change

        # ---------------------------------------------------------
        # Update the matrix
        # ---------------------------------------------------------

        if change is None:
            matrix[new_row][new_col] = matrix[old_row][old_col]
            matrix[old_row][old_col] = 0
        else:
            matrix[new_row][new_col] = change
            matrix[old_row][old_col] = 0

    # perform a single move for the player on the chessboard and update the matrix data
    def __perform_player_move(self, matrix_data: dict, move: list):
        old_row, old_col, new_row, new_col, change = move
        matrix = matrix_data["matrix"]

        # ---------------------------------------------------------
        # Capture bot piece
        # ---------------------------------------------------------

        if (new_row, new_col) in matrix_data["bot"]:
            captured_piece = matrix_data["bot"].pop((new_row, new_col))
            # handle castling data of bot for next
            if captured_piece == 4 and new_row == matrix_data["bot_king"][0] and new_col in matrix_data["castling"]["bot"]:
                matrix_data["castling"]["bot"].remove(new_col)
            # handle the points
            if matrix_data["points"] == 0:
                matrix_data["points"] = self.__initial_point
            matrix_data["points"] = matrix_data["points"] - captured_piece

        # ---------------------------------------------------------
        # Player matrix update
        # ---------------------------------------------------------

        # handle player king movement
        if matrix[old_row][old_col] == 12:
            # castling
            if abs(new_col - old_col) == 2:
                # left side castling
                if old_col > new_col:
                    matrix_data["player"].pop((old_row, 0))
                    matrix_data["player"][(old_row, old_col - 1)] = 10
                    matrix[old_row][old_col - 1] = 10
                    matrix[old_row][0] = 0
                # right side castling
                elif old_col < new_col:
                    matrix_data["player"].pop((old_row, self.__collen - 1))
                    matrix_data["player"][(old_row, old_col + 1)] = 10
                    matrix[old_row][old_col + 1] = 10
                    matrix[old_row][self.__collen - 1] = 0
            matrix_data["player_king"] = (new_row, new_col)
            matrix_data["castling"]["player"] = []
        # handle castling by rook
        elif matrix[old_row][old_col] == 10 and old_row == matrix_data["player_king"][0] and old_col in matrix_data["castling"]["player"]:
            matrix_data["castling"]["player"].remove(old_col)
        
        # ---------------------------------------------------------
        # Move player piece
        # ---------------------------------------------------------

        matrix_data["player"].pop((old_row, old_col))
        if change is None:
            matrix_data["player"][(new_row, new_col)] = matrix[old_row][old_col]
        else:
            matrix_data["player"][(new_row, new_col)] = change

        # ---------------------------------------------------------
        # Update the matrix
        # ---------------------------------------------------------

        if change is None:
            matrix[new_row][new_col] = matrix[old_row][old_col]
            matrix[old_row][old_col] = 0
        else:
            matrix[new_row][new_col] = change
            matrix[old_row][old_col] = 0

class __Engine(__Calculate):
    def __init__(self, rowlen: int, collen: int, init_point: int, step: int):
        # how many steps bot will play to predict
        self.__steps = step
        self.__step_list = []

        # checkmate points
        self.__bot_checkmate_deduction = -(init_point)
        self.__player_checkmate_deduction = init_point + init_point + init_point
        
        # storage management
        self.__storage = MovesStorage()
        
        super().__init__(rowlen, collen, init_point)

    # engine run initial
    def _run(self, matrix_data: dict) -> tuple:
        # move the first move
        print("Step 1: Bot")
        data = self.__first_bot_move(matrix_data)
        self.__step_list = [False]
        self.__step_list.extend([True, False] * (self.__steps - 1))

        # keys of the storage
        key_list = []

        length_step = len(self.__step_list)

        # calculate the moves for the following steps
        for i in range(length_step):
            print(f"Step {i + 2}: {'Bot' if self.__step_list[i] else 'Player'}")
    
            # admin decision meta data start
            if i == length_step-1:
                self._start_setup_admin()

            # loading the data
            if i > 0:
                for key in key_list:
                    temp_data = self.__storage.load(key)
                    if temp_data:
                        data = self.__start_calc(self.__step_list[i], temp_data)
                        self.__storage.insert(key, data)
            else:
                data = self.__start_calc(self.__step_list[i], data)
                key_list = self._database_partition(False, data, self.__storage)
        
        # find the best move and next_moves
        best_move = self._get_best_move()
        next_moves = [int(friend) for item in key_list if "-" in item for user, friend in [item.split("-", 1)] if int(user) == best_move]

        return best_move, next_moves

    # engine run for the next steps
    def _next_run(self, file_name: str) -> tuple:
        if not self.__storage.exists(file_name):
            print("Key Donot match")
            pass

        data = self.__storage.load(file_name)
        if len(data) != 0:
            self.prev_points = data[1]["points_table"][1]
        else:
            return [], []
        self.__storage.clear()
        key_list = self._database_partition(True, data, self.__storage)

        length_step = len(self.__step_list)
        # calculate the moves for the following steps
        for i in range(length_step - 2, length_step):
            print(f"Step {i + 2}: {'Bot' if self.__step_list[i] else 'Player'}")

            # admin decision meta data start
            if i == length_step - 1:
                self._start_setup_admin()

            for key in key_list:
                temp_data = self.__storage.load(key)
                if temp_data:
                    data = self.__start_calc(self.__step_list[i], temp_data)
                    self.__storage.insert(key, data)

        # find the best move and next_moves
        best_move = self._get_best_move()
        next_moves = [int(friend) for item in key_list if "-" in item for user, friend in [item.split("-", 1)] if int(user) == best_move]
        
        return best_move, next_moves
    
    # this function first move bot
    def __first_bot_move(self, matrix_data: dict) -> list:
        moves = list(BotChessman(matrix_data))
        return self._move_chessman(matrix_data=matrix_data, moves=moves, last_moved=[], points_list=[], bot_side=True)
    
    # start the calculation for the possible matrix possible from each data
    def __start_calc(self, bot_side: bool, matrix_data: list) -> list:
        temp_tree = []
        for node in matrix_data:
            next_index = len(temp_tree)

            if node["stop"]:
                self._toggle_checkmate_point(node["moved"][0], node["points_table"], self.__step_list[len(node["moved"])-1], len(node["moved"]))
                temp_tree.append(node)
                continue
            else:
                matrix_data = node["matrix_data"]
                last_moves = node["moved"]
                point_list = node["points_table"]
                
                new_matrix_move_data = self.__each_matrix_data_calc(matrix_data=matrix_data, start=next_index, last_move=last_moves, points_list=point_list, bot_side=bot_side)
                
                if not new_matrix_move_data:
                    node["stop"] = True
                    if bot_side:
                        node["matrix_data"]["points"] = self.__bot_checkmate_deduction
                    else:
                        node["matrix_data"]["points"] = self.__player_checkmate_deduction
                    self._toggle_checkmate_point(node["moved"][0], node["points_table"], self.__step_list[len(node["moved"])-1], len(node["moved"]))
                    temp_tree.append(node)
                else:
                    temp_tree.extend(new_matrix_move_data)
        matrix_data = copy.deepcopy(temp_tree)
        return matrix_data

    # calculate the possible move by the coming side: BOT or PLAYER
    def __each_matrix_data_calc(self, matrix_data: dict, start: int, last_move: list, points_list: list, bot_side: bool) -> list:
        moves = list(BotChessman(matrix_data) if bot_side else PlayerChessman(matrix_data))
        if len(moves) == 0:
            return []
        else:
            return self._move_chessman(matrix_data=matrix_data, moves=moves, last_moved=last_move, points_list=points_list, bot_side=bot_side)

class Prediction(__Engine):
    def __init__(self, full=True, botLeftCastle=True, botRightCastle=True, playerLeftCastle=True, playerRightCastle=True):
        '''
        # Initializes the Prediction engine for chess move prediction.
        \n## Example usage:
        \n>>> obj = Prediction(\n\t\t\t\tfull=True,\n\t\t\t\tbotLeftCastle=True,\n\t\t\t\tbotRightCastle=False,\n\t\t\t\tplayerLeftCastle=False,\n\t\t\t\tplayerRightCastle=True\n\t\t\t)
        \n>>> initial_matrix = [[0, 0, 0, 6], [1, 0, 0, 0], [0, 7, 0, 0], [0, 0, 12, 0]]
        \n>>> obj.fit(initial_matrix)
        \n>>> best_move, next_options = obj.start()
        \n>>> pos_factor = obj.pos_factor
        \n>>> # print("Best move:", best_move)
        \n>>> # print("Next options:", [one_integer_to_five_elements(pos, pos_factor) for pos in list(next_options.keys())])
        \nParameters:
        \n- full (bool): If True, the engine will predict up to 10 steps ahead; if False, it will predict up to 3 steps ahead.
        \n- botLeftCastle (bool): Indicates if the bot can perform left-side castling.
        \n- botRightCastle (bool): Indicates if the bot can perform right-side castling.
        \n- playerLeftCastle (bool): Indicates if the player can perform left-side castling.
        \n- playerRightCastle (bool): Indicates if the player can perform right-side castling.
        '''
        self.__step = 10 if full else 3
        self.__bot_left_castle = botLeftCastle
        self.__bot_right_castle = botRightCastle
        self.__player_left_castle = playerLeftCastle
        self.__player_right_castle = playerRightCastle

    __current_matrix_data = {}
    __best_move = None

    pos_factor = 0
    '''This helps to make the four [old_row, old_col, new_row, new_col, change_piece] four elements in one integer
    \n>>> obj.pos_factor'''

    def fit(self, matrix:list[list[int]]):
        '''
        ### Prepares the engine with the initial chessboard state represented by a matrix.
        \nParameters:
        \n- matrix (list of list of int): A 2D list representing the chessboard, where each integer corresponds to a specific chess piece or an empty space.
        \nThe function initializes the internal state of the engine, including the positions of bot and
        '''
        rowlen = len(matrix)
        collen = len(matrix[0])
        self.pos_factor = rowlen if rowlen >= collen else collen

        # update the list matrix data
        temp_data = {}
        temp_data["points"] = 0
        temp_data["matrix"] = [row[:] for row in matrix]
        temp_data["bot"] = {}
        temp_data["player"] = {}
        temp_data["castling"] = {"bot": [], "player": []}

        # updating the meta data from the matrix
        for i in range(rowlen):
            for j in range(collen):
                if 0 < matrix[i][j] <= 6:
                    temp_data["bot"][(i, j)] = matrix[i][j]
                    # updating the bot king space
                    if matrix[i][j] == 6:
                        temp_data["bot_king"] = (i, j)
                    # update castling in bot
                    if matrix[i][j] == 4 and (j == 0 or j == collen - 1):
                        temp_data["castling"]["bot"].append((i, j))
                elif 7 <= matrix[i][j] <= 12:
                    temp_data["player"][(i, j)] = matrix[i][j]
                    # updating the player king space
                    if matrix[i][j] == 12:
                        temp_data["player_king"] = (i, j)
                    # update castling in player
                    if matrix[i][j] == 10 and (j == 0 or j == collen - 1):
                        temp_data["castling"]["player"].append((i, j))

        # filter out the castling rook positions only the columns
        temp_data["castling"]["bot"] = [rook[1] for rook in temp_data["castling"]["bot"] if rook[0] == temp_data["bot_king"][0] and abs(rook[1] - temp_data["bot_king"][1]) > 1 if (rook[1] == 0 and self.__bot_left_castle) or (rook[1] == collen - 1 and self.__bot_right_castle)]
        temp_data["castling"]["player"] = [rook[1] for rook in temp_data["castling"]["player"] if rook[0] == temp_data["player_king"][0] and abs(rook[1] - temp_data["player_king"][1]) > 1 if (rook[1] == 0 and self.__player_left_castle) or (rook[1] == collen - 1 and self.__player_right_castle)]

        initiate_point = (12 * len(temp_data["bot"])) if len(temp_data["bot"]) >= len(temp_data["player"]) else (12 * len(temp_data["player"]))
        self.__current_matrix_data = copy.deepcopy(temp_data)

        # fuel the engine
        super().__init__(rowlen=rowlen, collen=collen, init_point=initiate_point, step=self.__step)

    def start(self) -> tuple:
        '''
        # Starts the prediction engine.
        \n>>> best_move, next_partition = obj.start()
        \nReturns:
        \n- best_move (int): The best move for the bot, encoded as a single integer.
        \n- next_moves (dict): A dictionary containing the next possible moves and their corresponding matrix data, where keys are encoded moves and values are lists of matrix data.
        '''
        print("The engine is started")
        self.__best_move, next_moves = self._run(self.__current_matrix_data)
        return self.__best_move, next_moves

    def next(self, move: str) -> tuple:
        print("The enginge predict next")
        self.__best_move, next_moves = self._next_run(f"{self.__best_move}-{move}")
        return self.__best_move, next_moves
