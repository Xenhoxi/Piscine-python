import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load a csv file"""
    try:
        csv = pd.read_csv(path)
        print(f"Loading dataset of dimensions {csv.shape}")
        return csv
    except FileNotFoundError as error:
        print(error)
    except IsADirectoryError as error:
        print(error)
