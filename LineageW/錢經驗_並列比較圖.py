import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('天堂w_練功.xlsx', sheet_name='66')
df = df.iloc[:,0:4].dropna(how='any')
df = df.groupby(['等級','地點']).agg({'經驗值':'mean', '錢':'mean'}).reset_index()
df = df.sort_values(by=['經驗值','錢'], ascending=False)
print(df)

x1 = [x+0.25 for x in range(len(df['地點']))]
x2 = [x-0.25 for x in range(len(df['地點']))]
plt.bar(x1, df['經驗值'])
plt.bar(x2, df['錢'])

plt.xticks(x for x in range(df[['地點']]))


plt.title("66 等錢/經驗_並列比較圖")
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
plt.show()



