from collections import deque
from pathlib import Path

from aoc.day_05.part_1.solution import (
    check_update_correctly_ordered,
    get_middle_page_update,
)
from aoc.day_05.utils import process_print_puzzle, read_print_puzzle
from aoc.utils import performance_meter


def get_incorrectly_ordered_updates(
    pages_updates: list[list[int]], ordering_rules: dict[int, list[int]]
):
    return [
        page_update
        for page_update in pages_updates
        if not check_update_correctly_ordered(page_update, ordering_rules)
    ]


# def fix_incorrectly_ordered_update(incorrect_update: list[int], ordering_rules: dict[int, list[int]]) -> list[int]:
#    fixed_incorrect_update = []
#    for page in incorrect_update:
#        if page in ordering_rules:
#            dependencies = ordering_rules[page]
#            for dependency in dependencies:
#                if (dependency not in fixed_incorrect_update) and (dependency in incorrect_update):
#                    fixed_incorrect_update.append(dependency)
#        fixed_incorrect_update.append(page)
#    return fixed_incorrect_update


def fix_incorrectly_ordered_update(  # noqa: C901
    incorrect_update: list[int], ordering_rules: dict[int, list[int]]
) -> list[int]:
    """
    Fixes an incorrectly ordered list of page numbers according to the specified ordering rules.

    Args:
        incorrect_update (list[int]): The incorrectly ordered list of page numbers.
        ordering_rules (dict[int, list[int]]): A dictionary where keys are page numbers and values are lists of page numbers that must come before the key.

    Returns:
        list[int]: The correctly ordered list of page numbers.
    """
    # Create a set of pages in the update list
    update_set = set(incorrect_update)

    # Build the adjacency list for dependencies within the update list
    adjacency = {page: [] for page in incorrect_update}
    for page in incorrect_update:
        if page in ordering_rules:
            for dependency in ordering_rules[page]:
                if dependency in update_set:
                    adjacency[dependency].append(page)

    # Build in-degree count for each node in the update list
    in_degree = {page: 0 for page in incorrect_update}
    for dependency in adjacency:
        for page in adjacency[dependency]:
            in_degree[page] += 1

    # Initialize queue with nodes that have in-degree 0
    queue = deque([page for page in incorrect_update if in_degree[page] == 0])

    # Initialize the topological order list
    topological_order = []

    # Perform Kahn's algorithm
    while queue:
        page = queue.popleft()
        topological_order.append(page)
        for neighbor in adjacency[page]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check if all pages are in the topological order
    if len(topological_order) == len(incorrect_update):
        return topological_order
    else:
        # There is a cycle; return an empty list
        return []


@performance_meter
def get_puzzle_solution() -> int:
    DAILY_PUZZLE_DIR = Path(__file__).parent.parent
    input_path = str(DAILY_PUZZLE_DIR / "input.txt")

    print_puzzle = read_print_puzzle(input_path)
    ordering_rules, pages_updates = process_print_puzzle(print_puzzle)
    incorrectly_ordered_updates = get_incorrectly_ordered_updates(
        pages_updates, ordering_rules
    )

    fixed_incorrectly_ordered_updates = [
        fix_incorrectly_ordered_update(incorrect_update, ordering_rules)
        for incorrect_update in incorrectly_ordered_updates
    ]

    return sum(
        [
            get_middle_page_update(page_update)
            for page_update in fixed_incorrectly_ordered_updates
        ]
    )


if __name__ == "__main__":
    solution = get_puzzle_solution()
    print(
        f"The sum of middle page number from those correctly-ordered updates is: {solution}"
    )
