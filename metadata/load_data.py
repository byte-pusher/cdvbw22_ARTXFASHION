import pandas as pd
from path import data_path

df_input = pd.read_csv(data_path)
df_input = df_input.set_index('dateiname')





