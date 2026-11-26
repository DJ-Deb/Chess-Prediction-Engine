
from prediction import Prediction, one_integer_to_five_elements
import copy


# ============================================================
# CONFIGURATION
# ============================================================

matrix = [
    [4, 0, 0, 6],
    [1, 0, 0, 0],
    [0, 7, 0, 0],
    [10, 0, 0, 12]
]

PIECES = {
    0: "·",
    1: "♙",
    2: "♘",
    3: "♗",
    4: "♖",
    5: "♕",
    6: "♔",
    7: "♙",
    8: "♘",
    9: "♗",
    10: "♖",
    11: "♕",
    12: "♔"
}


# ============================================================
# TERMINAL COLORS
# ============================================================

RESET = "\033[0m"
BOLD = "\033[1m"

CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
GRAY = "\033[90m"


# ============================================================
# TERMINAL UI
# ============================================================

def line(char="─", width=58):
    print(f"{GRAY}{char * width}{RESET}")


def header():
    print()
    line("═")

    print(
        f"{BOLD}{CYAN}"
        "              CHESS PREDICTION ENGINE"
        f"{RESET}"
    )

    print(
        f"{GRAY}"
        "                   MOVE ANALYSIS"
        f"{RESET}"
    )

    line("═")


def section(title):
    print()
    print(f"{BOLD}{CYAN}  {title}{RESET}")
    line()


def success(message):
    print(f"{GREEN}  ✓ {message}{RESET}")


def error(message):
    print(f"{RED}  ✗ {message}{RESET}")


# ============================================================
# BOARD DISPLAY
# ============================================================

def display_board(board):

    size = len(board)

    print()
    print("       " + "    ".join(str(i) for i in range(size)))
    print("     ┌" + "─────┬" * (size - 1) + "─────┐")

    for row_index, row in enumerate(board):

        cells = []

        for value in row:

            piece = PIECES.get(value, "?")

            if 1 <= value <= 6:
                color = "\033[91m"

            elif 7 <= value <= 12:
                color = "\033[92m"

            else:
                color = "\033[90m"

            cells.append(
                f"  {color}\033[1m{piece}\033[0m  "
            )

        print(
            f"  {row_index}  │"
            + "│".join(cells)
            + "│"
        )

        if row_index != size - 1:
            print(
                "     ├"
                + "─────┼" * (size - 1)
                + "─────┤"
            )

    print("     └" + "─────┴" * (size - 1) + "─────┘")

    print(
        "\n  \033[91m● Bot (1-6)\033[0m"
        "     \033[92m● Player (7-12)\033[0m"
    )


# ============================================================
# MOVE VALIDATION
# ============================================================

def validate_move(move, next_moves):

    """
    Validate the submitted move ID against available moves.

    Returns:
        int: Validated move ID.

    Raises:
        ValueError: If move ID is invalid.
    """

    try:
        move = int(move)

    except (ValueError, TypeError):
        raise ValueError("Move ID must be an integer.")

    if not next_moves:
        raise ValueError("No available moves.")

    valid_moves = {int(item) for item in next_moves}

    if move not in valid_moves:
        raise ValueError(
            f"Invalid Move ID: {move}. "
            "Choose an ID from the available moves."
        )

    return move


# ============================================================
# MOVE DECODING
# ============================================================

def decode_move(move, pos_factor):

    old_row, old_col, new_row, new_col, change_piece = (
        one_integer_to_five_elements(move, pos_factor)
    )

    return (
        old_row,
        old_col,
        new_row,
        new_col,
        change_piece
    )


# ============================================================
# BOARD UPDATE
# ============================================================

def update_board(board, move, pos_factor):

    (
        old_row,
        old_col,
        new_row,
        new_col,
        change_piece
    ) = decode_move(move, pos_factor)

    size = len(board)

    # Validate coordinates
    coordinates = [
        old_row,
        old_col,
        new_row,
        new_col
    ]

    if not all(
        isinstance(value, int)
        for value in coordinates
    ):
        raise ValueError("Decoded coordinates must be integers.")

    if not (
        0 <= old_row < size
        and 0 <= old_col < size
        and 0 <= new_row < size
        and 0 <= new_col < size
    ):
        raise ValueError(
            f"Move coordinates out of bounds: "
            f"{(old_row, old_col)} -> {(new_row, new_col)}"
        )

    # Validate source position
    if board[old_row][old_col] == 0:
        raise ValueError(
            f"No piece exists at {(old_row, old_col)}."
        )

    piece = (
        board[old_row][old_col]
        if change_piece is None
        else change_piece
    )

    # Apply move
    board[new_row][new_col] = piece
    board[old_row][old_col] = 0

    return (
        old_row,
        old_col,
        new_row,
        new_col,
        change_piece
    )


# ============================================================
# MOVE FORMATTING
# ============================================================

def format_move(move, pos_factor):

    (
        old_row,
        old_col,
        new_row,
        new_col,
        change_piece
    ) = decode_move(move, pos_factor)

    result = (
        f"({old_row}, {old_col}) → "
        f"({new_row}, {new_col})"
    )

    if change_piece is not None:

        result += (
            f" | Promotion: "
            f"{PIECES.get(change_piece, change_piece)}"
        )

    return result


# ============================================================
# PREDICTION DISPLAY
# ============================================================

def display_best_move(move, pos_factor, player):

    color = GREEN if player == "BOT" else YELLOW

    section(f"{player} MOVE")

    print(
        f"  {color}{BOLD}"
        f"{format_move(move, pos_factor)}"
        f"{RESET}"
    )

    print(f"  {GRAY}[ID: {move}]{RESET}")


def display_next_moves(next_moves, pos_factor):

    section(f"AVAILABLE NEXT MOVES ({len(next_moves)})")

    if not next_moves:
        print(f"  {GRAY}No available next moves.{RESET}")
        return

    for index, move in enumerate(next_moves, start=1):

        print(
            f"  {YELLOW}{index:02d}.{RESET} "
            f"{format_move(move, pos_factor)} "
            f"{GRAY}[ID: {move}]{RESET}"
        )


# ============================================================
# MOVE HISTORY
# ============================================================

def display_history(history):

    section("MOVE HISTORY")

    if not history:
        print(f"  {GRAY}No moves played yet.{RESET}")
        return

    for index, (player, move) in enumerate(history, start=1):

        color = GREEN if player == "BOT" else YELLOW

        print(
            f"  {index:02d}. "
            f"{color}{player:<8}{RESET} "
            f"{move}"
        )


# ============================================================
# PLAYER INPUT
# ============================================================

def get_player_move(next_moves, pos_factor):

    while True:

        raw_move = input(
            f"\n  {CYAN}Enter move ID: {RESET}"
        ).strip()

        if not raw_move:
            error("Move ID cannot be empty.")
            continue

        try:

            move = validate_move(
                raw_move,
                next_moves
            )

            # Return only a valid move
            return move

        except ValueError as exc:

            error(str(exc))

            print(
                f"  {GRAY}Please select one of "
                f"the currently available move IDs.{RESET}"
            )


# ============================================================
# MAIN APPLICATION
# ============================================================

def main():

    global matrix

    header()

    # --------------------------------------------------------
    # INITIALIZE PREDICTION ENGINE
    # --------------------------------------------------------

    section("INITIALIZING ENGINE")

    print(f"  {YELLOW}Loading prediction model...{RESET}")

    obj = Prediction(
        full=False,
        botLeftCastle=True,
        botRightCastle=True,
        playerLeftCastle=True,
        playerRightCastle=True
    )

    obj.fit(copy.deepcopy(matrix))

    pos_factor = obj.pos_factor

    success("Prediction engine initialized")

    # --------------------------------------------------------
    # SESSION VARIABLES
    # --------------------------------------------------------

    history = []
    turn = 1

    # --------------------------------------------------------
    # INITIAL BOARD
    # --------------------------------------------------------

    section("INITIAL BOARD")

    display_board(matrix)

    # --------------------------------------------------------
    # BOT FIRST MOVE
    # --------------------------------------------------------

    best_move, next_moves = obj.start()

    update_board(
        matrix,
        best_move,
        pos_factor
    )

    history.append((
        "BOT",
        format_move(best_move, pos_factor)
    ))

    display_best_move(
        best_move,
        pos_factor,
        "BOT"
    )

    success("Bot move applied")

    display_board(matrix)

    display_next_moves(
        next_moves,
        pos_factor
    )

    # --------------------------------------------------------
    # GAME LOOP
    # --------------------------------------------------------

    while True:

        line("═")

        print(f"\n  {BOLD}TURN {turn}{RESET}")

        print(f"""
   {GREEN}Y{RESET}  - Continue
   {RED}N{RESET}  - Exit
""")

        choice = input(
            f"  {CYAN}Your choice: {RESET}"
        ).strip().upper()

        if choice == "N":
            break

        if choice != "Y":

            error("Invalid choice. Enter Y or N.")
            continue

        # ----------------------------------------------------
        # CHECK AVAILABLE MOVES
        # ----------------------------------------------------

        if not next_moves:

            error("No available moves. Game over.")
            break

        # ----------------------------------------------------
        # PLAYER MOVE
        # ----------------------------------------------------

        section("PLAYER MOVE")

        move = get_player_move(
            next_moves,
            pos_factor
        )

        try:

            # Prepare a temporary board first
            temp_matrix = copy.deepcopy(matrix)

            update_board(
                temp_matrix,
                move,
                pos_factor
            )

            # Get bot prediction before committing the move
            best_move, updated_next_moves = obj.next(move)

            # Commit player's move
            matrix = temp_matrix

            history.append((
                "PLAYER",
                format_move(move, pos_factor)
            ))

            success("Player move applied")

            display_board(matrix)

            # ------------------------------------------------
            # BOT MOVE
            # ------------------------------------------------

            update_board(
                matrix,
                best_move,
                pos_factor
            )

            history.append((
                "BOT",
                format_move(best_move, pos_factor)
            ))

            display_best_move(
                best_move,
                pos_factor,
                "BOT"
            )

            success("Bot move applied")

            display_board(matrix)

            # ------------------------------------------------
            # UPDATE AVAILABLE MOVES
            # ------------------------------------------------

            next_moves = updated_next_moves

            display_next_moves(
                next_moves,
                pos_factor
            )

            turn += 1

        except (ValueError, TypeError, IndexError) as exc:

            error(f"Move processing failed: {exc}")
            break

        except Exception as exc:

            error(f"Prediction engine error: {exc}")
            break

    # --------------------------------------------------------
    # SESSION SUMMARY
    # --------------------------------------------------------

    section("SESSION SUMMARY")

    print(f"  Total turns   : {turn}")
    print(f"  Total moves   : {len(history)}")

    display_history(history)

    # --------------------------------------------------------
    # FINAL BOARD
    # --------------------------------------------------------

    section("FINAL BOARD")

    display_board(matrix)

    print()

    success("Prediction engine stopped")

    line("═")


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:

        print(
            f"\n\n{YELLOW}"
            "Application interrupted by user."
            f"{RESET}"
        )

    except Exception as exc:

        error(f"Application failed: {exc}")
