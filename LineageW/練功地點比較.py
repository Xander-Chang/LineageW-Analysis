import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 資料引入

df = pd.read_excel("天堂w_練功.xlsx", sheet_name="66")
# print('原本的樣子:\n', df,'\n')

# 資料清洗
df1 = df.iloc[:,0:4]
# print('iloc 取前面5個 col:\n', df1,'\n')
# df3 = df1.dropna(how='all')      
# print('dropna 空格的資料\n', df3,'\n')
df2 = df1.dropna(how='any')
# print('dropna 空格的資料\n', df2,'\n')


col_names = ['等級', '地點']
summeries = {'經驗值': 'mean', '錢': 'mean'}
df3 = df2.groupby(by=col_names).agg(summeries).reset_index()
# print('groupby排序/計算後:\n', df3,'\n')

df4 = df3.sort_values('經驗值', ascending=False)
print(df4)


# 製圖

level = df4["等級"]
spot = df4["地點"].astype(str)
ex = df4["經驗值"]
money = df4["錢"]


plt.figure(figsize=(12,10))
plt.bar(spot, ex, alpha=0.75, color='g', label='經驗值')

plt.xlabel('地點')
plt.xticks(rotation=60) 

plt.ylabel('經驗趴數')
plt.ylim(0,1.2)
plt.yticks(np.arange(0, 1.2, 0.05))

plt.grid()
plt.legend(loc='best')



plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

plt.title("66等妖精練功地點效率圖")
plt.show()

#上標籤 未解決 用text 但似乎有series 資料型態有問題

