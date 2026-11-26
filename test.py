from prediction import Prediction, one_integer_to_five_elements
import copy
from pprint import pprint

print("prediction file is started")

matrix = [
    [4, 0, 0, 6],
    [1, 0, 0, 0],
    [0, 7, 0, 0],
    [10, 0, 0, 12]
]

print("Initial matrix")
pprint(matrix)

obj = Prediction(full=False, botLeftCastle=True, botRightCastle=True, playerLeftCastle=True, playerRightCastle=True)

obj.fit(copy.deepcopy(matrix))

pos_factor = obj.pos_factor
print(pos_factor)

# played by the bot
best_move, next_moves = obj.start()
print("Best move:", best_move)
old_row, old_col, new_row, new_col, change_piece = one_integer_to_five_elements(best_move, pos_factor)
matrix[new_row][new_col] = matrix[old_row][old_col] if change_piece == None else change_piece
matrix[old_row][old_col] = 0
pprint(matrix)
print("Next options:", end="\t")
print(next_moves)
pprint([one_integer_to_five_elements(moves, pos_factor) for moves in next_moves])

while True:
    choice = input("Want to continue(y/n)?").capitalize()
    match choice:
        case "Y":
            move = input("Enter the next move:")
            # played by the player
            old_row, old_col, new_row, new_col, change_piece = one_integer_to_five_elements(int(move), pos_factor)
            matrix[new_row][new_col] = matrix[old_row][old_col] if change_piece == None else change_piece
            matrix[old_row][old_col] = 0
            pprint(matrix)

            # played by the bot
            best_move, next_moves = obj.next(move)
            print("Best move:", best_move)
            old_row, old_col, new_row, new_col, change_piece = one_integer_to_five_elements(best_move, pos_factor)
            matrix[new_row][new_col] = matrix[old_row][old_col] if change_piece == None else change_piece
            matrix[old_row][old_col] = 0
            pprint(matrix)
            print("Next options:", end="\t")
            print(next_moves)
            pprint([one_integer_to_five_elements(moves, pos_factor) for moves in next_moves])
        case "N":
            break
        case _:
            break

