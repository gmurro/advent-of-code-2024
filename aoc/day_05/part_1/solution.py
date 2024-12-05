from pathlib import Path

from aoc.day_05.utils import process_print_puzzle, read_print_puzzle
from aoc.utils import performance_meter


def check_update_correctly_ordered(
    page_update: list[int], ordering_rules: dict[int, list[int]]
) -> bool:
    """
    Checks if the given list of pages (page_update) is ordered correctly according to the specified ordering rules.

    The ordering_rules are defined such that for each key `b`, the list of values `[a]` indicates that `a` must appear before `b` in the update list.

    Args:
        page_update (list[int]): The list of page numbers to be updated.
        ordering_rules (dict[int, list[int]]): A dictionary where keys are page numbers and values are lists of page numbers that must appear before the key.

    Returns:
        bool: True if the update list respects all ordering rules, False otherwise.
    """
    seen = set()
    for page in page_update:
        if page in ordering_rules:
            dependencies = ordering_rules[page]
            for dependency in dependencies:
                if (dependency not in seen) and (dependency in page_update):
                    return False
        seen.add(page)
    return True


def get_middle_page_update(page_update: list[int]):
    return page_update[int(len(page_update) / 2)]


def get_correctly_ordered_updates(
    pages_updates: list[list[int]], ordering_rules: dict[int, list[int]]
):
    return [
        page_update
        for page_update in pages_updates
        if check_update_correctly_ordered(page_update, ordering_rules)
    ]


@performance_meter
def get_puzzle_solution() -> int:
    DAILY_PUZZLE_DIR = Path(__file__).parent.parent
    input_path = str(DAILY_PUZZLE_DIR / "input.txt")

    print_puzzle = read_print_puzzle(input_path)
    ordering_rules, pages_updates = process_print_puzzle(print_puzzle)
    correctly_ordered_updates = get_correctly_ordered_updates(
        pages_updates, ordering_rules
    )

    return sum(
        [
            get_middle_page_update(page_update)
            for page_update in correctly_ordered_updates
        ]
    )


if __name__ == "__main__":
    solution = get_puzzle_solution()
    print(
        f"The sum of middle page number from those correctly-ordered updates is: {solution}"
    )
