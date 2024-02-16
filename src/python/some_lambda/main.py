import pandas as pd


def lambda_handler(event, context):
    print(pd.DataFrame({'a': [1,2,3]}))
