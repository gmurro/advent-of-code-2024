from pathlib import Path

import pandas as pd

from aoc.day_01.utils import read_location_ids


def get_total_distance_between_lists(df: pd.DataFrame) -> int:
    """
    Calculate the total absolute distance between the sorted values of two list of location ids.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the two list of location ids created by the two groups of Senior Historians.

    Returns:
    int: The sum of the absolute differences between the sorted values of the two columns.
    """
    # Sort the values in each column
    sorted_first = df["first_group_ids"].sort_values(ignore_index=True)
    sorted_second = df["second_group_ids"].sort_values(ignore_index=True)

    # Calculate the absolute difference between each pair of sorted values
    absolute_differences = abs(sorted_first - sorted_second)

    # Sum the absolute differences
    return int(absolute_differences.sum())


def get_puzzle_solution() -> int:
    DAILY_PUZZLE_DIR = Path(__file__).parent.parent
    input_path = str(DAILY_PUZZLE_DIR / "input.txt")
    location_ids_df = read_location_ids(input_path)
    return get_total_distance_between_lists(location_ids_df)


if __name__ == "__main__":
    solution = get_puzzle_solution()
    print(
        f"Total distance between the lists created by the two groups of Senior Historians: {solution}"
    )
