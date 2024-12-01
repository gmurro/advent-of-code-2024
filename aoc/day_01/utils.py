import pandas as pd


def read_location_ids(file_path: str) -> pd.DataFrame:
    """
    Read puzzle as pandas Dataframe
    """
    return pd.read_csv(
        file_path,
        sep=r"\s+",
        header=None,
        names=["first_group_ids", "second_group_ids"],
    )
