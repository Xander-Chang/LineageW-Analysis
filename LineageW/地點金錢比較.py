import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_excel("天堂w_練功.xlsx", sheet_name="66")
df = df.iloc[:, :4]
df = df.dropna(how="any")
df = df.drop('經驗值', axis=1)
df = df.groupby(['等級','地點']).agg({'錢': 'mean'}).reset_index()
df = df.sort_values('錢', ascending=False)
print(df)


plt.figure(figsize=[10,8])
plt.bar(df['地點'], df['錢'], alpha=0.7, label='經驗值')

plt.xlabel('地點')
plt.xticks(rotation=45)                               # rotation 旋轉字體

plt.ylabel('金錢數量')
plt.ylim(0, 700000)
plt.yticks(np.arange(0, 720000, 20000))

plt.grid()
plt.legend(loc='best')

plt.title("66 等妖精練功地點效率圖")
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
plt.show()

