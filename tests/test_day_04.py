from textwrap import dedent

import pytest

from aoc.day_04.part_1.solution import grid_search_word
from aoc.day_04.part_2.solution import grid_search_cross_word


@pytest.fixture
def word_puzzle() -> list[list[str]]:
    """
    Fixture that returns a sample word puzzle.

    Returns:
        list[list[str]]: Sample word puzzle.
    """
    puzzle = dedent(
        """MMMSXXMASM
        MSAMXMSMSA
        AMXSXMAAMM
        MSAMASMSMX
        XMASAMXAMM
        XXAMMXXAMA
        SMSMSASXSS
        SAXAMASAAA
        MAMMMXMMMM
        MXMXAXMASX
        """
    )

    lines = puzzle.splitlines()
    return [list(line.strip()) for line in lines]


def test_word_puzzle(word_puzzle):
    print(word_puzzle)
    print("".join(word_puzzle[0]))
    assert len(word_puzzle) == 10
    assert len(word_puzzle[0]) == 10


def test_grid_search_word(word_puzzle):
    search_word = "XMAS"
    assert len(grid_search_word(word_puzzle, search_word)) == 18


def test_grid_search_cross_word(word_puzzle):
    search_word = "MAS"
    assert len(grid_search_cross_word(word_puzzle, search_word)) == 9
