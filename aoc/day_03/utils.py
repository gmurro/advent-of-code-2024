from enum import Enum, unique

from pydantic import BaseModel, Field


def read_puzzle(file_path: str) -> str:
    """
    Read puzzle as a string
    """
    with open(file_path) as file:
        return file.read()


@unique
class InstructionType(str, Enum):
    """
    An enumeration of instructions type
    """

    DO: str = "do"
    DONT: str = "don't"
    MUL: str = "mul"

    def __str__(self) -> str:
        return self.value


class Instruction(BaseModel):
    instruction_type: InstructionType = Field(
        ..., description="Type of the instruction"
    )


class Do(Instruction):
    instruction_type: InstructionType = Field(
        default=InstructionType.DO, validate_default=True
    )


class Dont(Instruction):
    instruction_type: InstructionType = Field(
        default=InstructionType.DONT, validate_default=True
    )


class Multiplication(Instruction):
    instruction_type: InstructionType = Field(
        default=InstructionType.MUL, validate_default=True
    )
    x: int = Field(description="The first integer to be multiplied")
    y: int = Field(description="The second integer to be multiplied")
