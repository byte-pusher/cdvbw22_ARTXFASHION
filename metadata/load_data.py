import pandas as pd

df_input = pd.read_csv('metadata/metadata.csv')
df_input = df_input.set_index('dateiname')





