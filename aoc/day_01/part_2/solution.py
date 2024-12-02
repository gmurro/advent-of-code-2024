from pathlib import Path

import pandas as pd

from aoc.day_01.utils import read_location_ids


def get_similarity_score(df: pd.DataFrame) -> int:
    """
    Calculate the total similarity score by adding up each number in the left list after multiplying it
    by the number of times that number appears in the right list.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the two list of location ids created by the two groups of Senior Historians.

    Returns:
    int: The similarity score.
    """
    return sum(
        location_id * df["second_group_ids"].value_counts().get(location_id, 0)
        for location_id in df["first_group_ids"]
    )


def get_puzzle_solution() -> int:
    DAILY_PUZZLE_DIR = Path(__file__).parent.parent
    input_path = str(DAILY_PUZZLE_DIR / "input.txt")
    location_ids_df = read_location_ids(input_path)
    return get_similarity_score(location_ids_df)


if __name__ == "__main__":
    solution = get_puzzle_solution()
    print(
        f"Similarity score between the lists created by the two groups of Senior Historians:\n{solution}"
    )
