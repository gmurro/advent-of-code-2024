from collections import Counter
from pathlib import Path

from aoc.day_04.utils import (
    get_chain_of_chars,
    is_valid_move,
    is_valid_word,
    read_word_puzzle,
)
from aoc.utils import performance_meter

SEARCH_WORD = "MAS"


def grid_search_cross_word(
    grid: list[list[str]], search_word: str
) -> list[tuple[int, int]]:
    """
    Searches for a given word in a grid, considering all possible directions, and returns the positions where the word is found exactly twice, indicating a cross.

    Args:
        grid (list[list[str]]): The grid of characters to search in.
        search_word (str): The word to search for.

    Returns:
        list[tuple[int,int]]: A list of positions where the word is found exactly twice, indicating a cross.
    """
    valid_words = []

    all_moves = [
        (-1, -1),  # Top-left
        (-1, 1),  # Top-right
        (1, -1),  # Bottom-left
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

    # get index of the char in the middle of the cross
    cross_index = int(len(search_word) / 2)

    # filter out words that are not crossed
    cross_positions = []
    for start_position, move in valid_words:
        cross_move = (cross_index * move[0], cross_index * move[1])
        # Calculate the new position
        cross_x = start_position[0] + cross_move[0]
        cross_y = start_position[1] + cross_move[1]
        cross_positions.append((cross_x, cross_y))

    # Count the occurrences of each pair
    cross_positions_counts = Counter(cross_positions)

    # Find position that appear exactly twice, meaning they are exactly crossed words
    return [
        position for position, count in cross_positions_counts.items() if count == 2
    ]


@performance_meter
def get_puzzle_solution() -> int:
    DAILY_PUZZLE_DIR = Path(__file__).parent.parent
    input_path = str(DAILY_PUZZLE_DIR / "input.txt")

    word_puzzle = read_word_puzzle(input_path)
    valid_words = grid_search_cross_word(word_puzzle, SEARCH_WORD)
    return len(valid_words)


if __name__ == "__main__":
    solution = get_puzzle_solution()
    print(f"The number of times the word XMAS appear is: {solution}")
