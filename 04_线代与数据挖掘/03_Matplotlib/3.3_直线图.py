import numpy as np
import matplotlib.pyplot as plt

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 五个点的x和y坐标
x = np.array([0, 10, 7, 12, 1])        # 五个点的x坐标
y = np.array([0, 5, 6, 7, 8])  # 对应的y坐标
'''
数组长度匹配：x 数组和 y 数组必须具有相同的长度，每个 x[i] 对应一个 y[i] 坐标点
此示例代码中 x 数组有5个元素，y 数组也有5个元素，这是正确的匹配
绘图原理：plt.plot() 函数会将 x 和 y 数组中对应位置的元素组合作为坐标点进行绘制
'''
# 使用Matplotlib绘制折线图
plt.plot(x, y, '-',
         label='Line between five points',  # 图例标签
         linewidth=2,  # 线宽
         color='red',  # 线的颜色
         marker='o',  # 标记样式
         markersize=10,  # 标记的大小
         markeredgecolor='black',  # 标记边缘的颜色
         markeredgewidth=2,  # 标记边缘的宽度
         markerfacecolor='blue',  # 标记内部的颜色
         alpha=1.0  # 透明度
         )

# 显示图例
"""
plt.legend() 的作用是：
显示图例：在图表中显示图例（legend），用于标识不同数据系列的含义
自动识别标签：会自动收集在 plt.plot() 等绘图函数中通过 label 参数设置的标签文本
提供图例说明：帮助读者理解图表中不同线条、点或数据系列代表的含义
在此段代码中：
在 plt.plot() 函数中设置了 label='Line between five points'
调用 plt.legend() 后，会在图表上显示这个标签，通常出现在图表的角落
用户可以通过图例清楚地知道这条红线代表的是"Line between five points"
如果没有调用 plt.legend()，即使在绘图时设置了 label 参数，图例也不会显示在图表中。
"""
plt.legend()

# 显示第一个图形（折线图）
plt.show()

# 创建第二个图形显示直线
"""
使用 plt.figure() 创建新的图形窗口
创建第二个图的原因：
1. 演示如何在不同的图形窗口中显示不同的图表
2. 展示更简单的数据绘制方式，直接使用列表而不是先定义数组
3. 对比不同的绘图效果：第一个图使用了复杂的参数设置，第二个图使用默认参数
4. 展示递增数据的直线图形，x轴坐标默认为[0,1,2,3,4]，y轴为传入的值[1,2,3,4,5]
   由于y值是递增的，所以形成一条上升的直线
"""
plt.figure()  # 创建一个新的图形窗口，与之前的图形窗口独立
# 绘制直线图
plt.plot([1, 2, 3, 4, 5], marker='o', linestyle='-')  # 绘制点(0,1),(1,2),(2,3),(3,4),(4,5)并用线连接
plt.title('直线图')  # 设置图形标题

# 显示第二个图形
plt.show()