from textwrap import dedent

import pytest

from aoc.day_05.part_1.solution import (
    get_correctly_ordered_updates,
    get_middle_page_update,
)
from aoc.day_05.part_2.solution import (
    fix_incorrectly_ordered_update,
    get_incorrectly_ordered_updates,
)
from aoc.day_05.utils import process_print_puzzle


@pytest.fixture
def print_puzzle() -> str:
    """
    Fixture that returns a sample puzzle.

    Returns:
        list[list[str]]: Sample puzzle.
    """
    puzzle = dedent(
        """47|53
        97|13
        97|61
        97|47
        75|29
        61|13
        75|53
        29|13
        97|29
        53|29
        61|53
        97|53
        61|29
        47|13
        75|47
        97|75
        47|61
        75|61
        47|29
        75|13
        53|13

        75,47,61,53,29
        97,61,53,29,13
        75,29,13
        75,97,47,61,53
        61,13,29
        97,13,75,29,47
        """
    )
    return puzzle


def test_process_print_puzzle(print_puzzle):
    ordering_rules, page_num_updates = process_print_puzzle(print_puzzle)
    print(ordering_rules)
    print(page_num_updates)
    assert len(ordering_rules) == 6
    assert len(page_num_updates) == 6


def test_get_correctly_ordered_updates(print_puzzle):
    ordering_rules, pages_updates = process_print_puzzle(print_puzzle)
    correctly_ordered_updates = get_correctly_ordered_updates(
        pages_updates, ordering_rules
    )

    assert len(correctly_ordered_updates) == 3


def test_get_puzzle_solution_part_1(print_puzzle):
    ordering_rules, pages_updates = process_print_puzzle(print_puzzle)
    correctly_ordered_updates = get_correctly_ordered_updates(
        pages_updates, ordering_rules
    )

    assert (
        sum(
            [
                get_middle_page_update(page_update)
                for page_update in correctly_ordered_updates
            ]
        )
        == 143
    )


def test_get_puzzle_solution_part_2(print_puzzle):
    ordering_rules, pages_updates = process_print_puzzle(print_puzzle)
    incorrectly_ordered_updates = get_incorrectly_ordered_updates(
        pages_updates, ordering_rules
    )
    fixed_incorrectly_ordered_updates = [
        fix_incorrectly_ordered_update(incorrect_update, ordering_rules)
        for incorrect_update in incorrectly_ordered_updates
    ]

    assert (
        sum(
            [
                get_middle_page_update(page_update)
                for page_update in fixed_incorrectly_ordered_updates
            ]
        )
        == 123
    )
