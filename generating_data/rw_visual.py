import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步
# while True:

# 创建一个RandomWalk实例，并将其包含的点都绘制出来
rw = RandomWalk(50000)
rw.fill_walk()

# 设置绘图窗口的尺寸
plt.figure(dpi=128, figsize=(10, 6))
point_numbers = list(range(rw.num_points)) # rang 返回可迭代对象，list将其转换为列表
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Greens,
            edgecolor='none', s=2)
plt.plot(rw.x_values, rw.y_values, linewidth=1)
# 突出起点和终点
plt.scatter(0, 0, c='green', edgecolors='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
            s=100)
# 隐藏坐标轴
# plt.axes().get_xaxis().set_visible(False)
# plt.axes().get_yaxis().set_visible(False)
# 多次调用了 plt.axes()，这可能会导致问题，因为每次调用 plt.axes() 都会创建新的坐标轴或者切换到不同的轴，
# 而不是对当前的轴进行操作。可以通过使用 plt.gca() (get current axes) 来获取当前的坐标轴，确保对当前图形的轴进行操作
# 正确隐藏坐标轴
plt.gca().get_xaxis().set_visible(False)
plt.gca().get_yaxis().set_visible(False)

plt.show()

    # keep_running = input("Make another walk? (y/n): ")
    # if keep_running == 'n':
    #     break