import matplotlib.pyplot as plt
import numpy as np
"""
直方图的绘图函数是plt.hist()
"""
plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

d=[6, 8, 6, 0, 0, 6, 9, 4, 2, 1,2,3,6,7,3,5]
plt.subplot(121)
plt.hist(x=d,bins=3,rwidth=2.8,color='#0504aa',alpha=0.7)  # alpha 是颜色深度 rwidth 条形宽度，bins条形箱的数目
plt.grid(axis='y', alpha=0.4)  # alpha 网格颜色深度
plt.xlabel('number')
plt.ylabel('count')
plt.title('样本分区间统计')

plt.subplot(122)
plt.hist(x=d,bins=[0,4,6,9],color='#0504aa',alpha=0.7)
plt.grid(axis='y', alpha=0.4)  # alpha 网格颜色深度
plt.xlabel('number')
plt.ylabel('count')
plt.title('样本分区间统计')
plt.show()