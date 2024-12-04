from pathlib import Path

from aoc.day_04.utils import (
    get_chain_of_chars,
    is_valid_move,
    is_valid_word,
    read_word_puzzle,
)
from aoc.utils import performance_meter

SEARCH_WORD = "XMAS"


def grid_search_word(
    grid: list[list[str]], search_word: str
) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    valid_words = []

    all_moves = [
        (-1, -1),  # Top-left
        (-1, 0),  # Top
        (-1, 1),  # Top-right
        (0, -1),  # Left
        (0, 1),  # Right
        (1, -1),  # Bottom-left
        (1, 0),  # Bottom
        (1, 1),  # Bottom-right
    ]

    n = len(grid)
    m = len(grid[0] if len(grid) else 0)

    for i in range(n):
        for j in range(m):
            current_char = grid[i][j]

            # check if it is our starting point
            if current_char == search_word[0]:
                allowed_moves = [
                    move for move in all_moves if is_valid_move((i, j), (move), n, m)
                ]
                for move in allowed_moves:
                    chars = get_chain_of_chars((i, j), move, len(search_word), grid)
                    if is_valid_word(chars, search_word):
                        valid_words += [((i, j), move)]
    return valid_words


@performance_meter
def get_puzzle_solution() -> int:
    DAILY_PUZZLE_DIR = Path(__file__).parent.parent
    input_path = str(DAILY_PUZZLE_DIR / "input.txt")

    word_puzzle = read_word_puzzle(input_path)
    valid_words = grid_search_word(word_puzzle, SEARCH_WORD)
    return len(valid_words)


if __name__ == "__main__":
    solution = get_puzzle_solution()
    print(f"The number of times the word XMAS appear is: {solution}")
