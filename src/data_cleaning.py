""" data cleaning
"""
from typing import List
import pandas as pd

def clean_columns(df: pd.DataFrame,
                  columns: List[str]) -> pd.DataFrame:
    """
    Cleans columns in a dataframe by converting values to 0 or 1.
    Args:
    df (pd.DataFrame): The pandas df containing the columns to be cleaned.
    columns (List[str]): list of column names in the df to be cleaned.
    Returns:
    pd.DataFrame: The DataFrame with the specified columns cleaned.
    """
    for col in columns:
        df[col] = df[col].apply(lambda x: 1 if x == 'Yes' or x == 1 else 0)
    return df
