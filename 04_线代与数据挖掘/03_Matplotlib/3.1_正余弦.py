import numpy as np
import matplotlib.pyplot as plt

# 计算曲线上的点的x和y坐标
x = np.arange(0, 3 * np.pi, 0.1)  # 起点、终点，步长
"""
linspace与arange函数的区别：最后一个参数是生成的点的个数。
linspace更方便、更常用。
"""
# x = np.linspace(0, 3 * np.pi, 1000)
y = np.sin(x)
#y = np.cos(x)
# 使用Matplotlib绘制点，并添加fmt和kwargs属性
plt.plot(x, y, '-',      # plot会自适应缩放轴的标度
         label='Cosine Wave',  # 图例标签
         linewidth=2,  # 线宽
         color='blue',  # 线的颜色
         marker='o',  # 标记样式
         markersize=5,  # 标记的大小
         markeredgecolor='black',  # 标记边缘的颜色
         markeredgewidth=1,  # 标记边缘的宽度
         markerfacecolor='none',  # 标记内部的颜色
         alpha=0.5 # 透明度
         )

# 显示图例
plt.legend()

# 显示图形
plt.show()
# print("hello world") # 直到关闭图像框，才会打印出来。
"""
会弹出一个图像框。
此函数的block参数默认为True，会阻滞程序的结束，
直到手动关闭图像框。
如果是`False`，则所有图形窗口都显示出来并立即返回。
所以，一般都会用的默认的true,并且都是放到代码末尾。
"""
# plt.show(block= False)
# print("hello world")
