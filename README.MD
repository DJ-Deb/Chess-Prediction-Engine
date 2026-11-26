# Chess Move Prediction Engine

A Python-based chess move prediction engine that evaluates possible board states, explores future moves, and selects a move for the bot using a set of prioritisation rules.

The engine accepts a chessboard represented as a 2D integer matrix. It returns the bot's selected move and the available follow-up moves.

> **Note:** This project provides a move-prediction engine and a matrix-based interface. The supplied code does not include a graphical chessboard or a complete user interface.

## Features

- Represents the board using a 2D Python list.
- Supports separate numeric identifiers for bot and player pieces.
- Generates and evaluates possible moves through `BotChessman` and `PlayerChessman`.
- Predicts multiple plies ahead.
- Selects a move using capture priority, min/max point evaluation, checkmate-related criteria, and next-move evaluation.
- Handles castling state and pawn promotion in the engine's move representation.
- Encodes a move as a single integer for compact storage.
- Uses `MovesStorage` to store and retrieve calculated move branches.

## Project modules

The example and prediction engine expect these modules to be available in the same project (or importable Python package):

```text
your-project/
├── prediction.py        # Prediction engine and move encoding/decoding
├── chessman.py          # BotChessman and PlayerChessman move generation
├── storageProcessing.py # MovesStorage persistence implementation
└── main.py              # Example program that runs the engine
```

The `chessman.py` and `storageProcessing.py` implementations are required dependencies; their internal behaviour and installation requirements are not specified here.

## Requirements

- Python 3.10 or later is recommended for the `match` statement used in the example.
- The `chessman.py` and `storageProcessing.py` modules described above.
- Any dependencies required by those modules.

No third-party package installation command can be specified from the supplied code alone. Add the project's actual dependencies to `requirements.txt` if applicable.

## Board representation

The board is a rectangular 2D list. Each cell contains `0` for an empty square or a piece identifier.

| Piece | Bot ID | Player ID |
|---|---:|---:|
| Pawn | `1` | `7` |
| Knight | `2` | `8` |
| Bishop | `3` | `9` |
| Rook | `4` | `10` |
| Queen | `5` | `11` |
| King | `6` | `12` |
| Empty square | `0` | `0` |

For example:

```python
matrix = [
    [4, 0, 0, 6],
    [1, 0, 0, 0],
    [0, 7, 0, 0],
    [10, 0, 0, 12]
]
```

The sample board is a 4 × 4 matrix. The engine derives its position factor from the larger of the row and column counts.

## Quick start

Create a `main.py` file:

```python
import copy
from pprint import pprint

from prediction import Prediction, one_integer_to_five_elements

matrix = [
    [4, 0, 0, 6],
    [1, 0, 0, 0],
    [0, 7, 0, 0],
    [10, 0, 0, 12]
]

print("Initial matrix:")
pprint(matrix)

# full=False: shorter prediction depth.
# Castling flags control whether each side may castle on that side.
engine = Prediction(
    full=False,
    botLeftCastle=True,
    botRightCastle=True,
    playerLeftCastle=True,
    playerRightCastle=True
)

# Prepare the engine. Pass a copy if the original matrix must be preserved.
engine.fit(copy.deepcopy(matrix))

# The position factor is used to decode integer moves.
pos_factor = engine.pos_factor

# Ask the bot for its first move.
best_move, next_moves = engine.start()

print("Best move (encoded):", best_move)

old_row, old_col, new_row, new_col, change_piece = (
    one_integer_to_five_elements(best_move, pos_factor)
)

# Apply the bot's move to the local display matrix.
matrix[new_row][new_col] = (
    matrix[old_row][old_col] if change_piece is None else change_piece
)
matrix[old_row][old_col] = 0

print("Board after bot move:")
pprint(matrix)

print("Next options (encoded):", next_moves)
print(
    "Next options (decoded):",
    [one_integer_to_five_elements(move, pos_factor) for move in next_moves]
)
```

Run it with:

```bash
python main.py
```

## Playing subsequent moves

After the bot's first move, provide the player's move to `engine.next()`.

The move supplied to `next()` must be the encoded integer format returned by the move encoder / move-generation flow. The following example shows the interaction pattern:

```python
# `player_move` is an encoded integer representing the player's move.
old_row, old_col, new_row, new_col, change_piece = (
    one_integer_to_five_elements(player_move, pos_factor)
)

# Update the local board used by this example.
matrix[new_row][new_col] = (
    matrix[old_row][old_col] if change_piece is None else change_piece
)
matrix[old_row][old_col] = 0

# Ask the engine to calculate the bot's response.
best_move, next_moves = engine.next(str(player_move))

# Decode and apply the bot's response.
old_row, old_col, new_row, new_col, change_piece = (
    one_integer_to_five_elements(best_move, pos_factor)
)
matrix[new_row][new_col] = (
    matrix[old_row][old_col] if change_piece is None else change_piece
)
matrix[old_row][old_col] = 0
```

The example updates the visible matrix manually. The engine also maintains its own internal board and move-tree state. Keep the external board and the sequence of moves supplied to the engine in sync.

## Prediction depth

The `full` constructor option controls the configured prediction depth:

| Option | Configured steps |
|---|---:|
| `full=True` | 10 |
| `full=False` | 3 |

A larger search depth can require substantially more computation and storage because the number of possible board states can grow quickly.

## Move encoding

The engine represents a move as five values:

```python
[old_row, old_col, new_row, new_col, change_piece]
```

- `old_row`, `old_col`: starting square.
- `new_row`, `new_col`: destination square.
- `change_piece`: promoted piece identifier, or `None` when the moving piece keeps its identifier.

The move is packed into an integer. The lower three bits contain the promotion/change-piece code; the remaining bits contain the encoded coordinates.

Decode an engine move with:

```python
move_data = one_integer_to_five_elements(encoded_move, pos_factor)
print(move_data)
```

The decoder's promotion mapping is:

| Code | Decoded piece ID |
|---:|---:|
| `0` | `None` |
| `1` | `2` |
| `2` | `5` |
| `3` | `8` |
| `4` | `9` |
| `5` | `10` |
| `6` | `11` |

## Move-selection overview

The engine's move-selection code applies the following criteria in sequence:

1. Gives priority to an immediate bot checkmate.
2. Applies its capture-priority filtering.
3. Compares the maximum and minimum point outcomes.
4. Considers the closest checkmate-step information.
5. Compares the next-move point value.
6. Uses checkmate-count difference as a final tie-break criterion.

These are the selection rules implemented in the supplied engine; they should not be interpreted as a claim of complete tournament-level chess strategy or full chess-rules compliance.

## Castling options

Castling availability is configured when creating the engine:

```python
engine = Prediction(
    full=False,
    botLeftCastle=True,
    botRightCastle=False,
    playerLeftCastle=True,
    playerRightCastle=False
)
```

The four flags independently configure left- and right-side castling eligibility for the bot and player. The supplied implementation derives eligible rook positions from the initial matrix and these flags.

## Important integration notes

- The board must contain the expected piece IDs, including one king for each side, because the setup code records each king's position.
- The example applies moves to its own `matrix`; it does not automatically update that variable when the engine calculates a move.
- Pass player moves to `next()` using the encoded integer representation expected by the engine.
- `one_integer_to_five_elements()` requires the same `pos_factor` obtained from the fitted engine.
- The engine uses `MovesStorage` internally. Review that module's storage path, persistence behaviour, and cleanup strategy before running large searches or deploying it.
- Validate player moves before passing them to the engine if moves can come from an untrusted client or user interface.
- The supplied code does not establish support for every official chess rule or every board size. Test the rules and board configurations required by your application.

## Current scope

This README documents the interfaces and behaviour visible in the supplied prediction-engine code. It does not assume details that are not included for the move-generation and storage modules.

## License

Add your chosen open-source license before publishing this repository. Until a license is added, do not assume that others have permission to reuse, modify, or distribute the code.
