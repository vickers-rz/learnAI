import numpy as np
import matplotlib.pyplot as plt

"""
Matplotlib绘制正弦和余弦曲线示例

该脚本演示了如何使用numpy生成数据点，使用matplotlib绘制正弦和余弦函数曲线。
matplotlib.pyplot是matplotlib的子库，提供了类似MATLAB的绘图接口。
"""
# 使用numpy.linspace生成从0到3π之间的1000个均匀分布的数据点
# linspace比arange更精确，因为它确保生成的点数是固定的
# x轴数据：从0到3π，共1000个点，这样可以保证曲线平滑
x = np.linspace(0, 3 * np.pi, 1000)

# 计算每个x值对应的余弦和正弦值
# y_cos存储余弦函数值，y_sin存储正弦函数值
# numpy的cos和sin函数可以对整个数组进行运算，这是向量化操作的优势
y_cos = np.cos(x)  # 余弦函数值
y_sin = np.sin(x)  # 正弦函数值

# 使用Matplotlib绘制余弦曲线
# plt.plot()是matplotlib中最重要的绘图函数之一，用于创建线图
# 参数说明：
#   x, y_cos: x轴和y轴的数据
#   '-': 线型样式，'-'表示实线
#   label: 图例标签，用于标识这条曲线
#   linewidth: 线条宽度
#   color: 线条颜色
#   alpha: 透明度，取值范围0-1，1表示完全不透明
plt.plot(x, y_cos, '-',
         label='Cosine Wave',  # 图例标签
         linewidth=1,  # 线宽
         color='blue',  # 线的颜色
         # marker='o',  # 标记样式
         # markersize=5,  # 标记的大小
         # markeredgecolor='black',  # 标记边缘的颜色
         # markeredgewidth=1,  # 标记边缘的宽度
         # markerfacecolor='none',  # 标记内部的颜色
         alpha=1 # 透明度
         )

# 绘制正弦曲线，使用虚线样式
# '--'表示虚线线型
plt.plot(x, y_sin, '--',
         label='Sine Wave',  # 图例标签
         linewidth=1,  # 线宽
         color='red',  # 线的颜色
         # marker='o',  # 标记样式
         # markersize=5,  # 标记的大小
         # markeredgecolor='black',  # 标记边缘的颜色
         # markeredgewidth=1,  # 标记边缘的宽度
         # markerfacecolor='none',  # 标记内部的颜色
         alpha=1 # 透明度
         )



# 显示图例，自动根据plot函数中的label参数创建图例
# 图例会显示每条曲线的标签及其对应的颜色和线型
plt.legend()

# 显示图形窗口，这是matplotlib绘图的最后一步
# show()函数会阻塞程序执行，直到关闭图形窗口
# 它会将当前图形缓冲区的内容渲染到屏幕上
plt.show()
