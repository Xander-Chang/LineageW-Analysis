import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 資料引入
df = pd.read_excel("天堂w_練功.xlsx", sheet_name="62")
print(df)

# 資料清洗
df1 = df.dropna(how='all').iloc[:,0:4]
print(df1)




level = df1["等級"]
spot = df1["地點"].astype(str)
ex = df1["經驗值"]
money = df1["錢"]







plt.figure(figsize=(16,8))
plt.plot(spot, ex)
plt.yticks(np.arange(0, 1, 0.1))


plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

plt.title("62等妖精練功地點效率圖")
plt.show()
