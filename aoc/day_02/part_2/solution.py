import multiprocessing
from copy import deepcopy
from pathlib import Path

import numpy as np

from aoc.day_02.utils import read_reports


def check_report_is_safe_with_problem_dampener(original_report: list[int]) -> bool:
    for i in range(len(original_report)):
        report = deepcopy(original_report)
        report.pop(i)
        report_desc = sorted(report, reverse=True)
        report_asc = sorted(report, reverse=False)

        # check levels are either all increasing or all decreasing
        # and check two adjacent levels differ by at least one and at most three
        level_distances = [int(abs(distance)) for distance in np.diff(report)]
        if (min(level_distances) >= 1 and max(level_distances) <= 3) and (
            report in (report_desc, report_asc)
        ):
            return True
    return False


def get_number_safe_reports_with_problem_dampener(reports: list[list[int]]) -> int:
    # Create a Pool of worker processes
    with multiprocessing.Pool() as pool:
        # Apply check_report_is_safe to each report in parallel
        results = pool.map(check_report_is_safe_with_problem_dampener, reports)

    # Collect safe reports
    safe_reports = [report for report, is_safe in zip(reports, results) if is_safe]

    print(f"Safe reports are:\n - {'\n - '.join([str(r) for r in safe_reports])}")
    return len(safe_reports)


def get_puzzle_solution() -> int:
    DAILY_PUZZLE_DIR = Path(__file__).parent.parent
    input_path = str(DAILY_PUZZLE_DIR / "input.txt")

    # Read all reports
    reports = read_reports(input_path)
    return get_number_safe_reports_with_problem_dampener(reports)


if __name__ == "__main__":
    import time

    time.perf_counter()
    solution = get_puzzle_solution()
    print(f"Total number of safe reports is: {solution}")
