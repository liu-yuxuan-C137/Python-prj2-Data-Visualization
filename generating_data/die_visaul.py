from die import Die
import pygal

# 创建一个D6
die_1 = Die()
die_2 = Die()
# 掷几次骰子，并将结果存储在一个列表中
# results = []
# for roll_num in range(1000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)
# 使用列表解析生成results
results = [die_1.roll() + die_2.roll() for value in range(1000)]
print(results)

# 分析结果

# frequencies = []
# for value in range(2, die_1.num_sides + die_2.num_sides + 1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

# my count
# frequencies = []
# frequency = 0
# for value in range(1, die.num_sides+1): # 注：range从0计数
#     for result in results:
#         if result == value:
#             frequency = frequency + 1
#     frequencies.append(frequency)
#     frequency = 0
# print(frequencies)

# 使用列表解析生成 frequencies
frequencies = [results.count(value) for value in range(2, die_1.num_sides + die_2.num_sides + 1)]
print(frequencies)
# verify
print(sum(frequencies))

# 对结果进行可视化
# 一个Bar类图表的实例化，并非函数
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times."
# list_lables = list(range(2, die_1.num_sides + die_2.num_sides + 1))
# hist.x_labels = list_lables
# 使用列表解析生成x_lables
hist.x_labels = [value for value in range(2, die_1.num_sides + die_2.num_sides +1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

# 将一系列值添加到图表中
hist.add('D6 + D6', frequencies)
# 将这个图表渲染为一个SVG文件
hist.render_to_file('die_visual.svg')

