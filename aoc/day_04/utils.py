def read_word_puzzle(file_path: str) -> list:
    """
    Read puzzle as a matrix of characters
    """
    with open(file_path) as file:
        multiline_content = file.read()

    lines = multiline_content.splitlines()
    return [list(line.strip()) for line in lines]


def is_valid_word(chars: list[str], search_word: str) -> bool:
    return "".join(chars) == search_word


def is_valid_move(
    position: tuple[int, int], move: tuple[int, int], rows: int, cols: int
) -> bool:
    """
    Check if a move is valid within the grid boundaries.

    Args:
        position (tuple[int, int]): Current position (row, column).
        move (tuple[int, int]): Move offset (row offset, column offset).
        rows (int): Number of rows in the grid.
        cols (int): Number of columns in the grid.

    Returns:
        bool: True if the move is valid, False otherwise.
    """
    new_x = position[0] + move[0]
    new_y = position[1] + move[1]
    return 0 <= new_x < rows and 0 <= new_y < cols


def get_chain_of_chars(
    start_position: tuple[int, int],
    move: tuple[int, int],
    len_word: int,
    grid: list[list[str]],
) -> list[str]:
    """
    Extract a sequence of characters from the grid starting from a given position in a specified direction.

    Args:
        start_position (tuple[int, int]): Starting position (row, column) in the grid.
        move (tuple[int, int]): Direction to move (row offset, column offset).
        len_word (int): Length of the word to extract.
        grid (list[list[str]]): The grid of characters.

    Returns:
        list[str]: List of characters forming the sequence.
    """
    chars = []
    rows = len(grid)
    cols = len(grid[0] if len(grid) else 0)
    x, y = start_position
    dx, dy = move

    for i in range(len_word):
        next_move = (i * dx, i * dy)

        # Check if the new position is within the grid boundaries
        if is_valid_move(start_position, next_move, rows, cols):
            # Calculate the new position
            new_x = x + next_move[0]
            new_y = y + next_move[1]
            chars.append(grid[new_x][new_y])
        else:
            # If the position is out of bounds, break the loop
            break

    return chars
