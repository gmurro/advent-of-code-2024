import pandas as pd
import pytest

from aoc.day_01.part_1.solution import get_total_distance_between_lists
from aoc.day_01.part_2.solution import get_similarity_score


@pytest.fixture
def location_ids_df():
    """
    Fixture that returns a sample DataFrame with the given values.

    Returns:
        pd.DataFrame: A DataFrame with columns 'first_group_ids' and 'second_group_ids'.
    """
    data = {
        "first_group_ids": [3, 4, 2, 1, 3, 3],
        "second_group_ids": [4, 3, 5, 3, 9, 3],
    }
    return pd.DataFrame(data)


def test_get_total_distance_between_lists(location_ids_df):
    assert get_total_distance_between_lists(location_ids_df) == 11


def test_get_similarity_score(location_ids_df):
    assert get_similarity_score(location_ids_df) == 31
