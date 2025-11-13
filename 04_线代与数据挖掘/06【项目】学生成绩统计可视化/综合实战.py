import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
写一个Numpy、matplotlib、Pandas的综合实战案例：
使用Pandas读取准备好的学生成绩表，计算每个学生的最终成绩，
最终成绩是平时成绩的百分之三十加上考试成绩的百分之七十，判断是否及格（60），
并将最终成绩和及格率填到表格里，并保存，然后使用Matplotlib进行显示最终成绩和及格率。
"""

# 读取学生成绩表
df = pd.read_csv('student_scores.csv')

# 计算每个学生的最终成绩（平时成绩30% + 考试成绩70%）
df['最终成绩'] = df['平时成绩'] * 0.3 + df['考试成绩'] * 0.7

# 判断是否及格（>=60）
df['是否及格'] = df['最终成绩'] >= 60

# 计算及格率
pass_rate = df['是否及格'].sum() / len(df)

# 打印结果
print("学生成绩表:")
print(df)
print(f"\n及格率: {pass_rate:.2%}")

# 保存到CSV文件
df.to_csv('student_results.csv', index=False, encoding='utf-8-sig')
print("\n已保存到 student_results.csv")

# 保存到Excel文件
df.to_excel('student_results.xlsx', index=False)
print("已保存到 student_results.xlsx")

# 使用Matplotlib显示最终成绩和及格率
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

# 创建图形和子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# 子图1: 显示每个学生的最终成绩
colors = ['green' if passed else 'red' for passed in df['是否及格']]
bars = ax1.bar(df['姓名'], df['最终成绩'], color=colors)
ax1.set_title('学生成绩分布')
ax1.set_xlabel('学生姓名')
ax1.set_ylabel('最终成绩')
ax1.tick_params(axis='x', rotation=45)

# 在柱状图上添加数值标签
for bar, score in zip(bars, df['最终成绩']):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
             f'{score:.1f}', ha='center', va='bottom')

# 子图2: 显示及格率和不及格率
labels = ['及格', '不及格']
sizes = [pass_rate, 1 - pass_rate]
colors_pie = ['lightgreen', 'lightcoral']
ax2.pie(sizes, labels=labels, colors=colors_pie, autopct='%1.1f%%', startangle=90)
ax2.set_title('及格率分布')

plt.tight_layout()
plt.show()