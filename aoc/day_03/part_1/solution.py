import re
from pathlib import Path

from aoc.day_03.utils import Multiplication, read_puzzle
from aoc.utils import performance_meter


def extract_multiplications(memory_puzzle: str) -> list[Multiplication]:
    pattern_mul = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    matches_mul = pattern_mul.findall(memory_puzzle)

    return [Multiplication(x=int(match[0]), y=int(match[1])) for match in matches_mul]


def sum_multiplications(multiplications: list[Multiplication]) -> int:
    return sum([mul.x * mul.y for mul in multiplications])


@performance_meter
def get_puzzle_solution() -> int:
    DAILY_PUZZLE_DIR = Path(__file__).parent.parent
    input_path = str(DAILY_PUZZLE_DIR / "input.txt")

    memory_puzzle = read_puzzle(input_path)
    multiplications = extract_multiplications(memory_puzzle)
    return sum_multiplications(multiplications)


if __name__ == "__main__":
    solution = get_puzzle_solution()
    print(f"The sum of all of the results of the multiplications is: {solution}")
