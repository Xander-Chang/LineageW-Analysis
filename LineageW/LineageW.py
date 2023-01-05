import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 資料引入
df = pd.read_excel("天堂w_練功.xlsx", sheet_name="66")
print(df,'\n')

# 資料清洗
df1 = df.iloc[:,0:4]
print(df1,'\n')
df2 = df1.dropna(how='any')
print(df2,'\n')


col_names = ['等級', '地點']
summeries = {'經驗值': 'mean', '錢': 'mean'}
df2 = df1.groupby(by=col_names).agg(summeries).reset_index()
#print(df2,'\n')



'''
level = df2["等級"]
spot = df2["地點"].astype(str)
ex = df2["經驗值"]
money = df2["錢"]


plt.figure(figsize=(16,8))
plt.plot(spot, ex)
plt.yticks(np.arange(0, 1, 0.1))


plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

plt.title("66等妖精練功地點效率圖")
plt.show()
'''

