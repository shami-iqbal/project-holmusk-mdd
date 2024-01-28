""" data analysis 
"""
import pandas as pd
def create_treatment_combination(row: pd.Series) -> str:
    """
    Create a treatment combination label based on the presence of treatments in a row.
    Args:   row (pd.Series): A Pandas Series representing a row of patient data with 
            treatment columns.
    Returns:
        str: A combination label representing the treatments present in the row.

    """
    treatment_names = {
        'trt_anx': 'anx',
        'trt_con': 'con',
        'trt_adt': 'adt',
        'trt_ssr': 'ssr',
        'trt_the': 'the',
        'trt_oth': 'oth'
    }

    combination = ('_'.join
                   (name for treatment,
                    name in treatment_names.
                    items() if row[treatment] == 1))
    return combination if combination else 'None'
