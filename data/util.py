import pandas as pd


def get_data(PATH):
    df = pd.read_csv(PATH)
    df = df.query("type == 'conventional' and region == 'Albany'")
    df = df.assign(Date=lambda data: pd.to_datetime(data["Date"], format="%Y-%m-%d"))
    df = df.sort_values(by="Date")
    print(df.head())
    return df

