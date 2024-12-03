import multiprocessing
from pathlib import Path

import numpy as np

from aoc.day_02.utils import read_reports


def check_report_is_safe(report: list[int]) -> bool:
    report_desc = sorted(report, reverse=True)
    report_asc = sorted(report, reverse=False)

    # check levels are either all increasing or all decreasing
    if report != report_desc and report != report_asc:
        return False

    # check two adjacent levels differ by at least one and at most three
    level_distances = [int(abs(distance)) for distance in np.diff(report)]
    return min(level_distances) >= 1 and max(level_distances) <= 3


def get_number_safe_reports(reports: list[list[int]]) -> int:
    # Create a Pool of worker processes
    with multiprocessing.Pool() as pool:
        # Apply check_report_is_safe to each report in parallel
        results = pool.map(check_report_is_safe, reports)

    # Collect safe reports
    safe_reports = [report for report, is_safe in zip(reports, results) if is_safe]

    print(f"Safe reports are:{'\n - '.join([str(r) for r in safe_reports])}")
    return len(safe_reports)


def get_puzzle_solution() -> int:
    DAILY_PUZZLE_DIR = Path(__file__).parent.parent
    input_path = str(DAILY_PUZZLE_DIR / "input.txt")

    # Read all reports
    reports = read_reports(input_path)
    return get_number_safe_reports(reports)


if __name__ == "__main__":
    solution = get_puzzle_solution()
    print(f"Total number of safe reports is: {solution}")
