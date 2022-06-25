import matplotlib.pyplot as plt
# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
#准备绘制数据
x = ["Mon", "Tues", "Wed", "Thur", "Fri","Sat","Sun"]
y = [20, 40, 35, 55, 42, 80, 50]
y2 = [15, 18, 24, 30, 31, 25, 24]
#传入绘图参数
plt.plot(x, y, "g", linewidth=1,marker='D', markersize=5)  # "g"表示绿色，marksize设置'D'表示菱形
plt.plot(x, y2, 'b', linewidth=1,marker='*',markersize=10)
plt.title("天气温度",fontsize=16)  # 折线图标题并设置标题的字体大小为16
plt.xlabel("登录时间",fontsize=8)  #生成x轴标签
plt.ylabel("用户活跃度",fontsize=8)  #生成y轴标签
plt.tick_params(axis='both', labelsize=10) #设置横纵坐标轴的刻度标记的大小
#绘制图例
plt.legend(['广州','惠州',])
#展示图片
plt.show()