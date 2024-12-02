import pytest

from aoc.day_02.part_1.solution import check_report_is_safe, get_number_safe_reports
from aoc.day_02.part_2.solution import (
    check_report_is_safe_with_problem_dampener,
    get_number_safe_reports_with_problem_dampener,
)


@pytest.fixture
def reports() -> list[list[int]]:
    """
    Fixture that returns a sample list of reports.

    Returns:
        list[list[int]]: Sample list of reports.
    """
    return [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]


def test_check_report_safe(reports):
    assert check_report_is_safe(reports[0]) is True


def test_check_report_unsafe(reports):
    assert check_report_is_safe(reports[1]) is False


def test_get_number_safe_reports(reports):
    assert get_number_safe_reports(reports) == 2


def test_check_report_safe_with_problem_dampener(reports):
    assert check_report_is_safe_with_problem_dampener(reports[4]) is True


def test_check_report_unsafe_with_problem_dampener(reports):
    assert check_report_is_safe_with_problem_dampener(reports[1]) is False


def test_get_number_safe_reports_with_problem_dampener(reports):
    assert get_number_safe_reports_with_problem_dampener(reports) == 4
