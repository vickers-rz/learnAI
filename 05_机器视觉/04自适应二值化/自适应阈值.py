import cv2

# 读取彩色图像
img_color = cv2.imread("lena.png")
# 将彩色图像转换为灰度图像
img = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

# 对灰度图像进行高斯模糊处理，减少噪声影响，使阈值处理更稳定
blur = cv2.GaussianBlur(img, (5,5), 0)

# 1. 固定阈值
_, th1 = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)

# 2. Otsu
_, th2 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 3. 自适应阈值 (Adaptive Thresholding)
# 对于光照不均匀的图像，全局阈值处理效果不佳。自适应阈值法则根据像素周围一小块区域的亮暗程度来动态计算该像素的阈值。
# 这样，在图像的不同区域，我们就可以使用不同的阈值，从而获得更好的效果。

# cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)
# - src: 输入图像（必须是灰度图）。
# - maxValue: 当像素值超过阈值时，赋予的新像素值（通常是255）。
# - adaptiveMethod: 自适应阈值的计算方法。主要有两种：
#   - cv2.ADAPTIVE_THRESH_MEAN_C: 阈值是邻域块的平均值减去常数 C。
#       - 简单来说，就是计算像素点周围 (blockSize x blockSize) 区域内所有像素值的平均值，然后用这个平均值作为局部阈值。
#   - cv2.ADAPTIVE_THRESH_GAUSSIAN_C: 阈值是邻域块的高斯加权和减去常数 C。
#       - 与平均法不同，高斯方法给邻域中的像素赋予不同的权重，离中心点越近的像素权重越大。这通常能提供比平均法更好的结果。
# - thresholdType: 阈值类型，通常为 cv2.THRESH_BINARY 或 cv2.THRESH_BINARY_INV。
# - blockSize: 用于计算阈值的邻域大小。它必须是一个奇数 (e.g., 3, 5, 7, ...)。
# - C: 从计算出的平均值或加权平均值中减去的一个常数。它可以是正数、零或负数。这个值用于微调阈值。
'''
调整C的基本原则是：
增加C值(例如，从2增加到10):
	这会使得计算出的局部阈值变小(平均值-C的结果更小)。
	阈值变小，意味着像素值更容易超过阈值，从而导致更多的像素被判断为白色（前景）。
	当你发现图像中有很多本应是白色的细节丢失了，可以尝试增加C。
减小C值(例如，从2减小到-5):
	这会使得计算出的局部阈值变大(平均值-C的结果更大，因为减去一个负数等于加上一个正数)。
	阈值变大，意味着像素值更难超过阈值，从而导致更少的像素被判断为白色，更多的像素变成黑色（背景）。
	当你发现结果中存在很多不应有的噪点（小的白色斑点）时，可以尝试减小C。
总结与建议：
1.从一个小的正数开始：你的代码中C=2是一个很好的起点。
2.观察结果：
	如果结果图像太“碎”或者噪点太多，说明很多背景被误判为前景了，应该减小C(甚至可以设为负数)。
	如果结果图像丢失了太多你想要的线条或轮廓，说明很多前景被误判为背景了，应该增加C。
3.C是一个经验值：C的最佳值没有固定公式，它高度依赖于具体图像的光照条件、对比度以及你希望达成的最终效果。
  最好的方法就是多尝试几个不同的值，观察它们对结果的影响，然后选择最满意的一个。
'''
# 使用高斯加权平均法
th3 = cv2.adaptiveThreshold(blur, 255,
                            cv2.ADAPTIVE_THRESH_GAUSSIAN_C, # 阈值是邻域块像素值的高斯加权和，再减去常数C
                            cv2.THRESH_BINARY, 11, 2)

# 使用平均值法
th4 = cv2.adaptiveThreshold(blur, 255,
                            cv2.ADAPTIVE_THRESH_MEAN_C, # 阈值是邻域块像素值的平均值，再减去常数C
                            cv2.THRESH_BINARY, 11, 2)


# 创建可调整大小的窗口
cv2.namedWindow('Original Color', cv2.WINDOW_NORMAL)
cv2.namedWindow('Grayscale', cv2.WINDOW_NORMAL)
cv2.namedWindow('Gaussian', cv2.WINDOW_NORMAL)
cv2.namedWindow('Binary', cv2.WINDOW_NORMAL)
cv2.namedWindow('Otsu', cv2.WINDOW_NORMAL)
cv2.namedWindow('Adaptive Gaussian', cv2.WINDOW_NORMAL)
cv2.namedWindow('Adaptive Mean', cv2.WINDOW_NORMAL)

cv2.imshow("Original Color", img_color)
cv2.imshow("Grayscale", img)
cv2.imshow("Gaussian", blur)
cv2.imshow("Binary", th1)
cv2.imshow("Otsu", th2)
cv2.imshow("Adaptive Gaussian", th3)
cv2.imshow("Adaptive Mean", th4)
cv2.waitKey(0)
cv2.destroyAllWindows()
