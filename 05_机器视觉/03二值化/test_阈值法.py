# 阈值法就是通过设置一个阈值，将灰度图中的每一个像素值与该阈值进行比较，
# 小于等于阈值的像素就被设置为0（黑），大于阈值的像素就被设置为maxval。
# 阈值法是最简单的二值化方法，但是它只能将灰度图二值化，不能将彩色图二值化。

import cv2
# 使用opencv的imread方法去读取一张图
image_np = cv2.imread('./flower.png')
# 使用opencv的函数 cvtColor去灰度化彩色图
image_gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
# 使用opencv的接口函数去二值化灰度图
'''
cv2.threshold 函数用于图像二值化处理
语法: cv2.threshold(src, thresh, maxval, type)
参数说明:
src: 输入图像（通常为灰度图）
thresh: 阈值，用于比较的临界值
maxval: 最大值，当像素值超过阈值时赋予的值
type: 阈值类型，常用的有:
  cv2.THRESH_BINARY:     大于阈值的部分设为maxval，小于部分设为0
  cv2.THRESH_BINARY_INV: 大于阈值的部分设为0，小于部分设为maxval
  cv2.THRESH_TRUNC:      大于阈值的部分设为thresh，小于部分保留原值
  cv2.THRESH_TOZERO:     大于阈值的部分保留原值，小于部分设为0
  cv2.THRESH_TOZERO_INV: 大于阈值的部分设为0，小于部分保留原值
返回值: (ret, dst) 其中ret是实际使用的阈值，dst是二值化后的图像
# 其中，ret存放的是二值化所用的阈值，如果我们使用阈值法等方法时，ret没有任何作用
# 当我们使用OTSU去计算最合适的阈值时，ret就有用了
"""
即使 Otsu 会返回一个自动计算的阈值，但你当前代码中并没有使用它。
所以仍然使用 _ 来丢弃：（_只是占位符，表示“我不关心这个值”）

_, th2 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

"""
# image_thresh里存放的是二值化的图(本质上是与image_gray大小相同的单通道数组)
'''
ret, image_thresh = cv2.threshold(image_gray, 150, 255, cv2.THRESH_BINARY)
# 使用opencv的函数  imshow去显示结果
cv2.imshow('image_thresh', image_thresh)
# 使用waitKey()去固定窗口
cv2.waitKey(0)
