import pandas as pd

def load_and_process(path):
    df = pd.read_csv(path)
    df = df[df["state"] != "undefined"]
    df = df[df["country"] != 'N,0"']
    df = df.drop(["usd pledged", "pledged", "goal"], axis=1)
    return df