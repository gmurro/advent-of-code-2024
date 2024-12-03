import re
from pathlib import Path

from aoc.day_03.utils import (
    Do,
    Dont,
    Instruction,
    InstructionType,
    Multiplication,
    read_puzzle,
)
from aoc.utils import performance_meter


def extract_instructions(memory_puzzle: str) -> list[Instruction]:
    pattern_instr = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|don't\(\)|do\(\)")

    # Parse instructions
    instructions: list[Instruction] = []

    for match in pattern_instr.finditer(memory_puzzle):
        if match.group(0).split("(")[0] == InstructionType.MUL:
            x, y = int(match.group(1)), int(match.group(2))
            instructions.append(Multiplication(x=x, y=y))
        elif match.group(0).split("(")[0] == InstructionType.DO:
            instructions.append(Do())
        elif match.group(0).split("(")[0] == InstructionType.DONT:
            instructions.append(Dont())

    return instructions


def sum_instructions(instructions: list[Instruction]) -> int:
    is_mul_enabled = True
    sum_mul = 0
    for instr in instructions:
        if instr.instruction_type == InstructionType.DO:
            is_mul_enabled = True
        elif instr.instruction_type == InstructionType.DONT:
            is_mul_enabled = False
        elif instr.instruction_type == InstructionType.MUL and is_mul_enabled:
            sum_mul += instr.x * instr.y
    return sum_mul


@performance_meter
def get_puzzle_solution() -> int:
    DAILY_PUZZLE_DIR = Path(__file__).parent.parent
    input_path = str(DAILY_PUZZLE_DIR / "input.txt")

    memory_puzzle = read_puzzle(input_path)
    instructions = extract_instructions(memory_puzzle)
    return sum_instructions(instructions)


if __name__ == "__main__":
    solution = get_puzzle_solution()
    print(f"The sum of all of the results of the multiplications is: {solution}")
