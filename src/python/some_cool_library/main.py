from typing import Dict

import pandas as pd


def generate_df():
    return pd.DataFrame({"x": [1, 2, 3, 4], "y": [4, 5, 6, 7]})


def get_dict_len(input_dict: Dict):
    return len(input_dict)
