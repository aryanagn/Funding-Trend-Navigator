import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd


def load_and_process(path_csv):
    
    df1 = (
         pd.read_csv( path_csv)
        .drop(['category','currency','country', 'pledged', 'goal', 'usd pledged'], axis=1)
        .rename(columns={'main_category': 'category', 'usd_pledged_real': 'pledged', 'usd_goal_real': 'goal'})
    )
    df2 = (
        df1.loc[df1['state'].isin(
            ['successful', 'failed'])]
    )
  
    return df2
