import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('天堂w_練功.xlsx', sheet_name='66')
df = df.iloc[:,0:4].dropna(how='any')
df = df.groupby(['等級','地點']).agg({'經驗值':'mean', '錢':'mean'}).reset_index()
df = df.sort_values(by=['經驗值','錢'], ascending=False)
print(df)



plt.figure(figsize=(12,8))
plt.suptitle("66 等錢/經驗_並列比較圖", fontsize=24)                # 大標題

plt.subplot(211)
plt.title("練功地點比較圖", fontsize=16, loc='left')
plt.plot(df['地點'], df['經驗值'], label='經驗值', color='#a59922')
plt.xlabel('地點')
plt.ylabel('經驗趴數')
plt.ylim(0,1.2)
plt.yticks(np.arange(0, 1.2, 0.1))
plt.legend(loc='best', )


plt.subplot(212)
plt.title("地點金錢比較圖", fontsize=16, loc='left')
plt.plot(df['地點'], df['錢'], label='錢', ls='-.')
plt.xlabel('地點')
plt.ylabel('金錢數量')
plt.ylim(0, 400000)
plt.yticks(np.arange(20000, 400000, 20000))
plt.legend(loc='best')

# print(list(df['地點']))                  # df 轉乘 list
# print(df['地點'].tolist())


plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
plt.show()
# plt.savefig()



