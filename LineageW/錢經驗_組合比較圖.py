import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# 資料清洗
df = pd.read_excel('天堂w_練功.xlsx', sheet_name='66')
df = df.iloc[:,0:4].dropna(how='any')
df = df.groupby(['等級','地點']).agg({'經驗值':'mean', '錢':'mean'}).reset_index()
df = df.sort_values(by=['經驗值','錢'], ascending=False)
print(df)



# 畫布
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)

# 練功地點Bar
ax1 = ax.bar(df['地點'], df['經驗值'], label='經驗值', alpha=0.8)
plt.xlabel('地點')
plt.xticks(rotation=70)
plt.ylabel('經驗趴數')
plt.ylim(0,1.2)
plt.yticks(np.arange(0, 1.3, 0.1))
plt.grid()



# 金錢Line
ax2 = ax.twinx()
ax2 = plt.plot(df['地點'],df['錢'],label='錢', color='#a59922',alpha=0.5)
plt.ylabel('金錢數量')
plt.ylim(0, 700000)
plt.yticks(np.arange(50000, 720000, 50000))


# legend_tags = [ax1, ax2]
# ax.legend(legend_tags, [legend_tags for legend_tag in legend_tags])    # 圖表標示無法解決, 同時表示 ax1、ax2


plt.suptitle('錢、經驗_組合比較圖', fontsize=28)
# plt.subplot_tool
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
plt.show()
# plt.savefig(dpi= )










