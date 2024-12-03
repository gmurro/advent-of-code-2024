import pytest

from aoc.day_03.part_1.solution import (
    extract_multiplications,
    sum_multiplications,
)
from aoc.day_03.part_2.solution import (
    extract_instructions,
    sum_instructions,
)
from aoc.day_03.utils import Do, Dont, Multiplication


@pytest.fixture
def memory_puzzle_mul() -> str:
    """
    Fixture that returns a sample memory puzzle.

    Returns:
        str: Sample memory puzzle.
    """
    return "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"


@pytest.fixture
def memory_puzzle_instr() -> str:
    """
    Fixture that returns a sample memory puzzle with additional instructions.

    Returns:
        str: Sample memory puzzle with additional instructions.
    """
    return "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def test_extract_multiplications(memory_puzzle_mul):
    expected_multiplications = [
        Multiplication(x=2, y=4),
        Multiplication(x=5, y=5),
        Multiplication(x=11, y=8),
        Multiplication(x=8, y=5),
    ]
    assert extract_multiplications(memory_puzzle_mul) == expected_multiplications


def test_sum_multiplications():
    multiplications = [
        Multiplication(x=2, y=4),
        Multiplication(x=5, y=5),
        Multiplication(x=11, y=8),
        Multiplication(x=8, y=5),
    ]
    assert sum_multiplications(multiplications) == 161


def test_extract_instructions(memory_puzzle_instr):
    expected_instructions = [
        Multiplication(x=2, y=4),
        Dont(),
        Multiplication(x=5, y=5),
        Multiplication(x=11, y=8),
        Do(),
        Multiplication(x=8, y=5),
    ]
    assert extract_instructions(memory_puzzle_instr) == expected_instructions


def test_sum_instructions():
    instructions = [
        Multiplication(x=2, y=4),
        Dont(),
        Multiplication(x=5, y=5),
        Multiplication(x=11, y=8),
        Do(),
        Multiplication(x=8, y=5),
    ]
    assert sum_instructions(instructions) == 48
