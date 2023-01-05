import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

level = 66
df = pd.read_excel("天堂w_練功.xlsx", sheet_name="level")
df = df.iloc[:, :4]
df = df.dropna(how="any")
df = df.drop('經驗值', axis=1)
df = df.groupby(['等級','地點']).agg({'錢': 'mean'}).reset_index()
print(df)

plt.figure(figsize=[8:6])
plt.bar(df['地點'], df['經驗值'])
plt.ytick(np.arange(10000, 200000, 2000))
plt.grid()

plt.title(level, "等妖精練功地點效率圖")