import csv
from matplotlib import pyplot as plt
from datetime import datetime

# 从文件中获取日期、最高气温和最低气温
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    # csv.reader() 将文件内容解析为一个可迭代的对象，每次迭代返回一行数据，该行数据以列表的形式表示
    # 返回一个迭代器（iterator），这个迭代器可以在 for 循环中使用，逐行读取 CSV 文件的内容
    header_row = next(reader)
    # second_row = next(reader)
    # print(second_row)
    # 调用 next(reader) 后，reader 的状态会改变，它的内部指针会向下移动到下一行。
    # 这意味着在之后的迭代中，你将从文件的第二行开始读取数据。

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # dates = [datetime.strptime(row[0], "%Y-%m-%d") for row in reader]
    # highs = [int(row[1]) for row in reader]
    # 不可以实现。这两行中都使用了reader，但在第一次读取reader后，指针会移动到文件的末尾，
    # 这意味着在第二次尝试读取reader时，将不会再有任何数据可供读取。必须在同一个循环里进行
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)  # list.append()的返回值是None，不可以用于赋值
            lows.append(low)
        # try:
        #     current_date = datetime.strptime(row[0], "%Y-%m-%d")
        #     high = int(row[1])
        #     low = int(row[3])
        #     # 将这三行直接放在 try 块中
        #     dates.append(current_date)
        #     highs.append(high)
        #     lows.append(low)
        # except ValueError:
        #     print(current_date, 'missing data')
# 功能上等价：不使用 else 和使用 else 在功能上可以是等价的，效果相同，都是处理异常。
# 逻辑上的区别：使用 else 明确表示后续代码在没有异常的情况下才会执行，帮助代码逻辑更加清晰，尤其在处理复杂逻辑时，else 块可以让代码更具可读性。

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6)) # 设置绘图窗口的尺寸
plt.plot(dates, highs, c='red', alpha=0.5) # matplotlib可自动识别datetime格式
plt.plot(dates, lows, c='blue', alpha=0.5) # 实参alpha指定颜色的透明度,0表示完全透明
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# 设置图形的格式
title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate() # 调用了fig.autofmt_xdate()来绘制斜的日期标签，以免它们彼此重叠。
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16) # which 参数能够更精确地控制图表中的刻度线设置

plt.show()