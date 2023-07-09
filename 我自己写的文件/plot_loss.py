import matplotlib.pyplot as plt

x = [6, 24, 48, 72]
y1 = [87, 174, 225, 254]
y2 = [24, 97, 202, 225]
plt.title('扩散速度')  # 折线图标题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
plt.xlabel('时间')  # x轴标题
plt.ylabel('差值')  # y轴标题
plt.plot(x, y1)  # 绘制折线图，添加数据点，设置点的大小
plt.plot(x, y2)

# for a, b in zip(x, y1):
#     plt.text(a, b, b, ha='center', va='bottom', fontsize=10)  # 设置数据标签位置及大小
# for a, b in zip(x, y2):
#     plt.text(a, b, b, ha='center', va='bottom', fontsize=10)


plt.legend(['方案一', '方案二'])  # 设置折线名称

plt.show()  # 显示折线图

