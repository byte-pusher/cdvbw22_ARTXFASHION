import pandas as pd

df = pd.read_csv('metadata/metadata.csv')
df = df.set_index('dateiname')
