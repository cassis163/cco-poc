import pandas as pd
from os import getcwd
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv(getcwd() + '/data/winequality-red.csv')
regressor = RandomForestRegressor(n_estimators=2000)

target = 'quality'
features = [item for item in df.columns.values if item != target]

def run():
    regressor.fit(
        df[features],
        df[target]
    )