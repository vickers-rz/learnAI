import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
形态学变换简明教程
=================

本教程将介绍形态学变换的基本概念和应用，
重点展示不同核对腐蚀和膨胀操作的影响。
"""

# 1. 创建示例图像
# 创建一个黑色背景图像
image = np.zeros((100, 100), dtype=np.uint8)

# 添加一些形状用于演示
cv2.rectangle(image, (10, 10), (40, 40), 255, -1)  # 白色矩形
cv2.circle(image, (70, 25), 15, 255, -1)           # 白色圆形

# 添加一些噪声点
cv2.circle(image, (20, 60), 2, 255, -1)            # 小噪声点
cv2.circle(image, (40, 70), 1, 255, -1)            # 更小的噪声点

print("原始图像已创建")

# 2. 定义不同的结构元素（核）
"""
核的类型：
1. 矩形核 (MORPH_RECT) - 各方向作用均匀且强烈
2. 椭圆核 (MORPH_ELLIPSE) - 接近自然物体形状，作用柔和
3. 十字核 (MORPH_CROSS) - 主要在水平和垂直方向起作用
"""

# 创建不同形状的核
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))      # 矩形核
ellipse_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)) # 椭圆核
cross_kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))     # 十字核

# 3. 执行基本形态学操作

# 腐蚀操作 - 使白色区域缩小，可以去除小的噪声点
eroded_rect = cv2.erode(image, rect_kernel, iterations=1)
eroded_ellipse = cv2.erode(image, ellipse_kernel, iterations=1)
eroded_cross = cv2.erode(image, cross_kernel, iterations=1)

# 膨胀操作 - 使白色区域扩大，可以填补小的空洞
dilated_rect = cv2.dilate(image, rect_kernel, iterations=1)
dilated_ellipse = cv2.dilate(image, ellipse_kernel, iterations=1)
dilated_cross = cv2.dilate(image, cross_kernel, iterations=1)

# 4. 组合操作

# 开运算 = 先腐蚀后膨胀 - 去除小的噪声点
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, ellipse_kernel)

# 闭运算 = 先膨胀后腐蚀 - 填补小的空洞
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, ellipse_kernel)

# 5. 可视化结果
plt.figure(figsize=(12, 8))

# 显示原始图像和不同核的腐蚀效果
plt.subplot(3, 4, 1)
plt.imshow(image, cmap='gray')
plt.title('原始图像')
plt.axis('off')

plt.subplot(3, 4, 2)
plt.imshow(eroded_rect, cmap='gray')
plt.title('矩形核腐蚀')
plt.axis('off')

plt.subplot(3, 4, 3)
plt.imshow(eroded_ellipse, cmap='gray')
plt.title('椭圆核腐蚀')
plt.axis('off')

plt.subplot(3, 4, 4)
plt.imshow(eroded_cross, cmap='gray')
plt.title('十字核腐蚀')
plt.axis('off')

# 显示原始图像和不同核的膨胀效果
plt.subplot(3, 4, 5)
plt.imshow(image, cmap='gray')
plt.title('原始图像')
plt.axis('off')

plt.subplot(3, 4, 6)
plt.imshow(dilated_rect, cmap='gray')
plt.title('矩形核膨胀')
plt.axis('off')

plt.subplot(3, 4, 7)
plt.imshow(dilated_ellipse, cmap='gray')
plt.title('椭圆核膨胀')
plt.axis('off')

plt.subplot(3, 4, 8)
plt.imshow(dilated_cross, cmap='gray')
plt.title('十字核膨胀')
plt.axis('off')

# 显示组合操作效果
plt.subplot(3, 4, 9)
plt.imshow(image, cmap='gray')
plt.title('原始图像')
plt.axis('off')

plt.subplot(3, 4, 10)
plt.imshow(opening, cmap='gray')
plt.title('开运算(去噪)')
plt.axis('off')

plt.subplot(3, 4, 11)
plt.imshow(closing, cmap='gray')
plt.title('闭运算(填补)')
plt.axis('off')

# 显示核的形状
plt.subplot(3, 4, 12)
plt.imshow(ellipse_kernel, cmap='gray')
plt.title('椭圆核形状')
plt.axis('off')

plt.tight_layout()
plt.show()
