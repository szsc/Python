import matplotlib.pyplot as plt
import numpy as np
"""
条形图/柱状图的绘制函数plt.bar()相关参数：
# params
# x: 条形图x轴
# height：条形图的高度
# width：条形图的宽度 默认是0.8
# bottom：条形底部的y坐标值 默认是0
# align：center / edge 条形图是否以x轴坐标为中心点或者是以x轴坐标为边缘
"""
# 以下两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
#figsize=(width, height)，默认单位：inches，定义了 figure 的尺寸大小(图像的物理尺寸)；
#dpi(dots per inches)表示图像的分辨率，即每英寸距离上的点数(像素数)
fig=plt.figure(figsize=(12,12),dpi=150)

#添加第一幅子图(第一行第一列)
ax1=fig.add_subplot(121)
#设置第一幅子图的标题
ax1.set_title("购买饮用水情况的调查结果")
# 输入统计数据
drinks = ('碳酸饮料', '绿茶', '矿泉水', '果汁', '其他')
buy_number_male = [6, 7, 6, 1, 2]
buy_number_female = [9, 4, 4, 5, 6]
#设置绘图参数
bar_width=0.3  #柱状图默认宽度是0.8
index_male = np.arange(len(drinks)) # 男生条形图的横坐标
index_female = index_male + bar_width # 女生条形图的横坐标
# 使用bar函数绘制条形图
plt.bar(index_male, height=buy_number_male, width=0.3, color='b', label='男性')
plt.bar(index_female, height=buy_number_female, width=0.3, color='r', label='女性')
plt.legend() # 显示图例
plt.xlabel('饮料类型',fontsize=12) #横坐标轴标题
# 设置横坐标轴刻度的位置为index_male+bar_width/2，设置横坐标轴刻度值为 drinks元组里的各种饮料
plt.xticks(index_male + bar_width/2,drinks)
# 纵坐标轴标题
plt.ylabel('购买量',fontsize=12)
#保存图片
plt.savefig("../tempPic/test.jpg")

#添加第二幅子图(第一行第二列)
ax2=fig.add_subplot(122)
ax2.set_title("大气污染物浓度柱状图")
plt.bar(['SO2','NO2','O3'],height=[10,8,9],width=0.3,color=['y','g','b'])
plt.xlabel('污染物类型')
plt.ylabel('大气污染物浓度均值(微克每立方米)')
plt.show() #展示条形图/柱状图
