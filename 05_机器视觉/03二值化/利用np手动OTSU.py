import numpy as np
import cv2


# ===================== 1. 读取图像 =====================
image = cv2.imread('./flower.png')

# ===================== 2. 转换为灰度图 =====================
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ===================== 3. 获取图像尺寸与像素总数 =====================
# NumPy 数组 gray 的 shape 属性返回它的维度信息。
# 对于灰度图：
#   gray.shape -> (rows, cols)
# 对于彩色图：
#   image.shape -> (rows, cols, channels)
rows, cols = gray.shape

# 图像的总像素个数 = 行数 * 列数
total_pixels = rows * cols


# ===================== 4. 统计灰度范围 =====================
# gray.min() 和 gray.max() 是 NumPy 数组的方法:
# - gray.min(): 返回数组中的最小值（这里是最小灰度值）。
# - gray.max(): 返回数组中的最大值（这里是最大灰度值）。
# 这两个值用于限定我们遍历阈值 t 的范围。
min_value = gray.min()
max_value = gray.max()


# ===================== 5. 计算整幅图像的平均灰度 =====================
# gray.mean() 返回数组所有元素的平均值（浮点数）。
# 在 Otsu 算法中：
#   u 表示整幅图像的平均灰度（全局均值）。
u = gray.mean()


# ===================== 6. 准备存储每个阈值对应的类间方差 =====================
# 使用 Python 内置的 dict（字典）来存储：
#   key（键）  ：阈值 t
#   value（值）：该阈值对应的类间方差 g
# 例如：variance_dict[120] = 12345.6
variance_dict = {}


# ===================== 7. 遍历所有可能的阈值 =====================
# range(start, stop) 生成一个整数序列，从 start 到 stop-1。
# 这里我们使用：
#   range(min_value + 1, max_value)
# 原因：
#   - 如果阈值 t 取到 min_value，那么灰度 <= t 的那一类几乎包含所有像素，另一类可能为空；
#   - 如果 t 取到 max_value，那么灰度 > t 的那一类可能为空；
#   - 因此通常避开两端极值，让两类都尽量有像素。
for t in range(min_value + 1, max_value):

    # ========== 7.1 利用布尔索引分割前景和背景 ==========
    # NumPy 数组可以通过布尔条件进行筛选：
    #   gray > t 会返回一个与 gray 同形状的布尔数组（True/False）。
    #   gray[gray > t] 则会返回所有满足条件的元素，组成一个一维数组。
    #
    # 在这里我们人为定义：
    #   foreground: 灰度值 > t 的像素（可以理解为“前景”或“亮的那一类”）。
    #   background: 灰度值 <= t 的像素（可以理解为“背景”或“暗的那一类”）。
    foreground = gray[gray > t]
    background = gray[gray <= t]

    # ========== 7.2 检查是否有某一类为空 ==========
    # len(array) 返回数组中元素的个数。
    # 如果某个类完全没有像素（如阈值设置得太极端），
    # 则该阈值没有意义，直接跳过。
    if len(foreground) == 0 or len(background) == 0:
        continue

    # ========== 7.3 计算每一类的像素数 ==========
    n0 = len(foreground)     # 类 0 像素数量
    n1 = len(background)     # 类 1 像素数量

    # ========== 7.4 计算类权重（类在整幅图中的占比） ==========
    # 在 Otsu 中：
    #   w0 = n0 / total_pixels
    #   w1 = n1 / total_pixels
    # 且 w0 + w1 = 1（因为两类刚好覆盖所有像素）。
    w0 = n0 / total_pixels
    w1 = n1 / total_pixels

    # ========== 7.5 计算每一类的平均灰度（类内均值） ==========
    # NumPy 数组的 mean() 方法会返回数组元素的平均值。
    # foreground.mean(): 前景像素的均值 u0。
    # background.mean(): 背景像素的均值 u1。
    u0 = foreground.mean()
    u1 = background.mean()

    # ========== 7.6 按 Otsu 公式计算类间方差 ==========
    # Otsu 类间方差公式的一种形式：
    #   g = w0 * (u0 - u)^2 + w1 * (u1 - u)^2
    #
    # 其中：
    #   u  是全局均值（在循环外已经求好）。
    #   u0 是类 0 均值。
    #   u1 是类 1 均值。
    #   w0, w1 是两类的权重。
    #
    # 直观理解：
    #   - 如果两类的平均灰度 u0 和 u1 与整体均值 u 差得很开，
    #     且两类权重都不太小，则 g 会很大；
    #   - 类间方差越大，说明这一阈值 t 越能把图像分成“差异明显”的两类。
    g = w0 * (u0 - u) ** 2 + w1 * (u1 - u) ** 2

    # ========== 7.7 将当前阈值与对应的类间方差存入字典 ==========
    # Python 字典赋值语法：
    #   字典名[键] = 值
    variance_dict[t] = g


# ===================== 8. 找到类间方差最大的阈值 =====================
# max(iterable, key=函数) 用于在可迭代对象中找到“某个评价指标最大”的元素。
# 这里：
#   - iterable 是 variance_dict，也就是字典的键集合（所有 t）。
#   - key=variance_dict.get 表示：
#         对每个键 t，用 variance_dict.get(t) 作为比较大小的依据。
# 效果相当于：
#   在所有阈值 t 中，找到使得 variance_dict[t] 最大的那个 t。
thresh = max(variance_dict, key=variance_dict.get)

# 打印最终得到的 Otsu 阈值
print("OTSU 阈值 =", thresh)


# ===================== 9. 使用最优阈值进行二值化 =====================
# 这里我们不用 OpenCV 自带的 cv2.threshold，而是用 NumPy 自己实现：
#
# np.where(condition, x, y) 的用法：
#   - condition 是一个布尔数组（与 gray 同形状的 True/False）。
#   - 返回的数组中：
#       对应位置若 condition 为 True，则取 x 对应位置的值；
#       否则取 y 对应位置的值。
#
# 在这里：
#   条件：gray > thresh
#   True  的位置：赋值 255（白色）。
#   False 的位置：赋值 0（黑色）。
# 结果：
#   得到一个与 gray 同形状的数组，元素为 0 或 255。
binary = np.where(gray > thresh, 255, 0)

# np.where 返回的数组默认 dtype 为 float64（视输入而定），
# 而图像在 OpenCV 中通常使用 uint8（0~255 的无符号 8 位整数）。
# 因此用 astype(np.uint8) 强制进行类型转换。
# astype(dtype) 是 NumPy 数组的方法，用于生成一个指定类型的新数组。
binary = binary.astype(np.uint8)


# ===================== 10. 显示二值化结果图 =====================
# cv2.imshow(winname, mat) 用于显示图像。
# - winname: 窗口名称（字符串）。
# - mat    : 要显示的图像数组（可以是灰度图或 BGR 彩色图）。
cv2.imshow("Binary (no resize)", binary)

# cv2.waitKey(delay) 用于等待键盘事件。
# - delay > 0: 等待指定毫秒数，如果期间有按键，则返回该键的 ASCII 值；
# - delay = 0: 无限期等待，直到用户按下任意键。
# 常用于“阻塞程序，直到用户按键后继续”。
cv2.waitKey(0)

# cv2.destroyAllWindows() 关闭所有由 OpenCV 创建的窗口。
# 如果只想关闭某一个窗口，可以使用 cv2.destroyWindow(winname)。
cv2.destroyAllWindows()
