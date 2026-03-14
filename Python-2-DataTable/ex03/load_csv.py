import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load a data set from a csv file,
    writes the dimensions of the dataset, displays it and returns it.\
    Print an error if an error occurs, and return None.
    Args:
        path (str): The path of the dataset (csv).
    Returns:
        pd.DataFrame: the dataset loaded, or None if an error has occurred.
    """
    try:
        ext = ".csv"
        find_ext = path.find(".csv")
        if find_ext == -1 or find_ext + len(ext) is not len(path):
            raise ValueError("format must be in '.csv'.")
        data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")
        print(data)
        return data
    except Exception as error:
        print(f"{type(error)} : {error}")
        return None
