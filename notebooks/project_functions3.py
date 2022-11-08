import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

def load_and_process(path_csv):
    
    df1 = (
         pd.read_csv(path_csv)
        .drop(['currency','country', 'usd pledged', 'pledged', 'ID', 'name','deadline', 'launched', 'backers'], axis=1)
        .rename(columns={'category': 'Type (Subcategory)', 'usd_pledged_real': 'deadline_pledge', 'usd_goal_real': 'initial_pledge'})
        .reindex(['Type (Subcategory)','main_category','goal','state','deadline_pledge','initial_pledge'], axis=1)
    )
    df2 = (
        df1.loc[df1['state'].isin(
            ['successful', 'failed'])]
    )
  
    return df2