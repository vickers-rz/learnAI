
# 使用Numpy库来创建三维数组
import numpy as np

# 创建一个700*700的三维数组（彩色图）
# dtype=np.uint8 表示无符号整数 0-255
image = np.zeros((700, 700, 3), dtype=np.uint8)
