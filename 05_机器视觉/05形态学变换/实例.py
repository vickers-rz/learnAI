import cv2
import numpy as np
import matplotlib.pyplot as plt

# =======================================================================================
# 知识点 1: 什么是形态学变换 (Morphological Transformations)？
#
# 形态学是图像处理中的一个分支，主要用于分析和处理图像中的几何形状。
# 这类操作通过在图像上移动一个称为"核"或"结构元素"的小块来修改图像的形状特征。
#
# - 主要对象: 通常是二值化图像（黑白图像），但也可以应用于灰度图像。
# - 核心思想: 通过探查图像中的像素与其邻域像素的关系，来改变像素的值。
# - 主要用途:
#   1. 图像去噪 (例如去除小的白色噪点或黑色孔洞)。
#   2. 分割独立的图像元素或连接相邻的元素。
#   3. 寻找图像中明显的边界或轮廓。
#   4. 提取图像的骨架。
# =======================================================================================


# --- 1. 创建一个更适合展示形态学变换的测试图像 ---
# 创建一个黑色背景图像
image = np.zeros((200, 200), dtype=np.uint8)

# 添加一些白色形状来展示形态学变换效果
cv2.rectangle(image, (20, 20), (60, 60), 255, -1)  # 白色矩形
cv2.circle(image, (100, 50), 20, 255, -1)      # 白色圆形
cv2.ellipse(image, (150, 50), (25, 15), 0, 0, 360, 255, -1) # 白色椭圆

# 添加一些细小的噪声点和线条来展示去噪效果
cv2.rectangle(image, (30, 80), (32, 150), 255, -1)  # 细长条
cv2.rectangle(image, (50, 100), (70, 102), 255, -1) # 细长条
cv2.circle(image, (90, 120), 3, 255, -1)          # 小噪声点
cv2.circle(image, (110, 140), 2, 255, -1)         # 小噪声点

# 添加一些相互靠近的形状来展示连接效果
cv2.circle(image, (150, 100), 10, 255, -1)
cv2.circle(image, (170, 100), 10, 255, -1)

print("已创建用于演示形态学变换的测试图像")

# --- 2. 定义核/结构元素 (Kernel) ---
# =======================================================================================
# 知识点 2: 什么是核 (Kernel) / 结构元素 (Structuring Element)？
#
# 核是形态学操作的核心，它是一个小的二值矩阵（或称为"形状"），在输入图像上滑动，以确定每个像素的输出值。
# 核的形状和大小直接影响变换的结果。
#
# cv2.getStructuringElement(shape, ksize) 用于创建核。
# - shape: 核的形状。
#   - cv2.MORPH_RECT:    矩形核。 [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
#   - cv2.MORPH_ELLIPSE: 椭圆形核。在处理自然物体时效果通常更好。 [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
#   - cv2.MORPH_CROSS:   十字形核。 [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
# - ksize: 核的大小，例如 (3, 3), (5, 5)。大小越大，影响范围越广，效果越"剧烈"。
#
# 不同核的形状和大小选择：
# 1. 矩形核 (MORPH_RECT):
#    - 特点：各方向作用均匀，效果强烈
#    - 适用场景：需要在各个方向上同等程度地进行形态学操作时
#    - 示例：一般的膨胀、腐蚀操作
#
# 2. 椭圆核 (MORPH_ELLIPSE):
#    - 特点：接近自然物体的形状，各方向作用相对均匀但柔和
#    - 适用场景：处理自然图像，需要保持物体形状相对完整时
#    - 示例：去噪、平滑处理
#
# 3. 十字核 (MORPH_CROSS):
#    - 特点：主要沿水平和垂直方向作用
#    - 适用场景：需要保留对角线特征或只在特定方向进行操作时
#    - 示例：细化线条、提取骨架、特定方向的形态学操作
#
# 核大小选择原则：
# - 小核 (如 3x3): 作用轻微，适合精细处理
# - 中等核 (如 5x5): 平衡效果和性能，最常用
# - 大核 (如 7x7 或更大): 作用强烈，适合明显形态变化但可能丢失细节
# =======================================================================================
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)) # 使用 5x5 的椭圆核，效果会更明显

# --- 2.1 创建多种不同类型的核进行对比 ---
# 创建不同形状和大小的核以展示它们的效果差异
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))      # 矩形核
ellipse_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)) # 椭圆核
cross_kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))     # 十字核

# 创建不同大小的核
small_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))   # 小核
large_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))   # 大核

print("已创建多种不同类型的核用于演示")
print("矩形核形状:")
print(rect_kernel)
print("\n椭圆核形状:")
print(ellipse_kernel)
print("\n十字核形状:")
print(cross_kernel)

# --- 3. 执行各种形态学变换操作 ---

# 腐蚀 (Erosion)
# 原理: 用核扫描图像，只有当核覆盖的区域内所有像素都是白色时，中心像素才保持白色，否则变为黑色。
# 效果: "侵蚀"或"细化"白色区域的边界。
# 应用: 去除小的白色噪声点（"盐"噪声），分离两个连接在一起的物体。
eroded_image = cv2.erode(image, kernel, iterations=1)

# 使用不同核进行腐蚀的对比
eroded_rect = cv2.erode(image, rect_kernel, iterations=1)      # 矩形核腐蚀
eroded_cross = cv2.erode(image, cross_kernel, iterations=1)    # 十字核腐蚀
eroded_small = cv2.erode(image, small_kernel, iterations=1)    # 小核腐蚀
eroded_large = cv2.erode(image, large_kernel, iterations=1)    # 大核腐蚀

# 膨胀 (Dilation)
# 原理: 用核扫描图像，只要核覆盖的区域内有一个像素是白色，中心像素就变为白色。
# 效果: "扩张"或"增粗"白色区域的边界。
# 应用: 填充物体内的小黑洞（"胡椒"噪声），连接两个邻近但断开的物体。
dilated_image = cv2.dilate(image, kernel, iterations=1)

# 使用不同核进行膨胀的对比
dilated_rect = cv2.dilate(image, rect_kernel, iterations=1)    # 矩形核膨胀
dilated_cross = cv2.dilate(image, cross_kernel, iterations=1)  # 十字核膨胀
dilated_small = cv2.dilate(image, small_kernel, iterations=1)  # 小核膨胀
dilated_large = cv2.dilate(image, large_kernel, iterations=1)  # 大核膨胀

# 开运算 (Opening)
# 原理: 先进行腐蚀，再进行膨胀 (Erosion -> Dilation)。
# 效果: "打开"物体间的缝隙。
# 应用: 有效去除小的白色噪点（盐噪声），同时基本保持原始物体的大小不变。
opened_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# 使用不同核进行开运算的对比
opened_rect = cv2.morphologyEx(image, cv2.MORPH_OPEN, rect_kernel)    # 矩形核开运算
opened_cross = cv2.morphologyEx(image, cv2.MORPH_OPEN, cross_kernel)  # 十字核开运算
opened_small = cv2.morphologyEx(image, cv2.MORPH_OPEN, small_kernel)  # 小核开运算
opened_large = cv2.morphologyEx(image, cv2.MORPH_OPEN, large_kernel)  # 大核开运算

# 闭运算 (Closing)
# 原理: 先进行膨胀，再进行腐蚀 (Dilation -> Erosion)。
# 效果: "关闭"物体内部的孔洞。
# 应用: 有效填充物体内部的小黑洞（胡椒噪声），同时基本保持原始物体的大小不变。
closed_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# 使用不同核进行闭运算的对比
closed_rect = cv2.morphologyEx(image, cv2.MORPH_CLOSE, rect_kernel)   # 矩形核闭运算
closed_cross = cv2.morphologyEx(image, cv2.MORPH_CLOSE, cross_kernel) # 十字核闭运算
closed_small = cv2.morphologyEx(image, cv2.MORPH_CLOSE, small_kernel) # 小核闭运算
closed_large = cv2.morphologyEx(image, cv2.MORPH_CLOSE, large_kernel) # 大核闭运算

# 形态学梯度 (Gradient)
# 原理: 图像的膨胀结果减去腐蚀结果 (Dilation - Erosion)。
# 效果: 得到物体的轮廓。
# 应用: 提取物体的边缘。
gradient_image = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

# =======================================================================================
# 知识点 3: 顶帽和黑帽变换 (Top Hat & Black Hat)
# 这两种变换用于发现比邻域更亮或更暗的细节。
# =======================================================================================

# 顶帽 (Top Hat)
# 原理: 原始图像减去其开运算结果 (Original - Opening)。
# 效果: 突出显示那些比周围区域亮的、并且被开运算去除掉的小斑点或细节。
# 应用: 在不均匀光照下，校正背景，突出明亮的小物体。
tophat_image = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

# 使用不同核进行顶帽变换的对比
tophat_rect = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, rect_kernel)   # 矩形核顶帽变换
tophat_cross = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, cross_kernel)  # 十字核顶帽变换
tophat_small = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, small_kernel) # 小核顶帽变换
tophat_large = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, large_kernel) # 大核顶帽变换

# 黑帽 (Black Hat)
# 原理: 图像的闭运算结果减去原始图像 (Closing - Original)。
# 效果: 突出显示那些比周围区域暗的、并且被闭运算填充掉的小孔洞或细节。
# 应用: 突出显示暗色的小物体或图像中的黑色缺陷。
blackhat_image = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

# 使用不同核进行黑帽变换的对比
blackhat_rect = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, rect_kernel)   # 矩形核黑帽变换
blackhat_cross = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, cross_kernel)  # 十字核黑帽变换
blackhat_small = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, small_kernel) # 小核黑帽变换
blackhat_large = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, large_kernel) # 大核黑帽变换

# --- 4. 使用matplotlib显示结果 ---
# 创建一个图形窗口来显示原始图像和不同核的腐蚀、膨胀结果

# 显示原始图像和基本形态学操作结果
plt.figure(figsize=(12, 8))

# 第一行：原始图像和基本形态学操作
plt.subplot(2, 4, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 4, 2)
plt.imshow(eroded_image, cmap='gray')
plt.title('Erosion (Ellipse 5x5)')
plt.axis('off')

plt.subplot(2, 4, 3)
plt.imshow(dilated_image, cmap='gray')
plt.title('Dilation (Ellipse 5x5)')
plt.axis('off')

plt.subplot(2, 4, 4)
plt.imshow(opened_image, cmap='gray')
plt.title('Opening (Ellipse 5x5)')
plt.axis('off')

plt.subplot(2, 4, 5)
plt.imshow(closed_image, cmap='gray')
plt.title('Closing (Ellipse 5x5)')
plt.axis('off')

plt.subplot(2, 4, 6)
plt.imshow(gradient_image, cmap='gray')
plt.title('Gradient (Ellipse 5x5)')
plt.axis('off')

plt.subplot(2, 4, 7)
plt.imshow(tophat_image, cmap='gray')
plt.title('Top Hat (Ellipse 5x5)')
plt.axis('off')

plt.subplot(2, 4, 8)
plt.imshow(blackhat_image, cmap='gray')
plt.title('Black Hat (Ellipse 5x5)')
plt.axis('off')

plt.tight_layout()
plt.show()

# 创建一个新的图形窗口来显示不同核对腐蚀和膨胀的影响
plt.figure(figsize=(15, 10))

# 腐蚀操作对比
plt.subplot(3, 5, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(3, 5, 2)
plt.imshow(eroded_rect, cmap='gray')
plt.title('Erosion (Rect 5x5)')
plt.axis('off')

plt.subplot(3, 5, 3)
plt.imshow(eroded_cross, cmap='gray')
plt.title('Erosion (Cross 5x5)')
plt.axis('off')

plt.subplot(3, 5, 4)
plt.imshow(eroded_small, cmap='gray')
plt.title('Erosion (Ellipse 3x3)')
plt.axis('off')

plt.subplot(3, 5, 5)
plt.imshow(eroded_large, cmap='gray')
plt.title('Erosion (Ellipse 7x7)')
plt.axis('off')

# 膨胀操作对比
plt.subplot(3, 5, 6)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(3, 5, 7)
plt.imshow(dilated_rect, cmap='gray')
plt.title('Dilation (Rect 5x5)')
plt.axis('off')

plt.subplot(3, 5, 8)
plt.imshow(dilated_cross, cmap='gray')
plt.title('Dilation (Cross 5x5)')
plt.axis('off')

plt.subplot(3, 5, 9)
plt.imshow(dilated_small, cmap='gray')
plt.title('Dilation (Ellipse 3x3)')
plt.axis('off')

plt.subplot(3, 5, 10)
plt.imshow(dilated_large, cmap='gray')
plt.title('Dilation (Ellipse 7x7)')
plt.axis('off')

# 核的形状可视化
plt.subplot(3, 5, 11)
plt.imshow(rect_kernel, cmap='gray')
plt.title('Rect Kernel (5x5)')
plt.axis('off')

plt.subplot(3, 5, 12)
plt.imshow(cross_kernel, cmap='gray')
plt.title('Cross Kernel (5x5)')
plt.axis('off')

plt.subplot(3, 5, 13)
plt.imshow(small_kernel, cmap='gray')
plt.title('Ellipse Kernel (3x3)')
plt.axis('off')

plt.subplot(3, 5, 14)
plt.imshow(large_kernel, cmap='gray')
plt.title('Ellipse Kernel (7x7)')
plt.axis('off')

plt.subplot(3, 5, 15)
plt.imshow(ellipse_kernel, cmap='gray')
plt.title('Ellipse Kernel (5x5)')
plt.axis('off')

plt.tight_layout()
plt.show()

# 等待按键并关闭所有 OpenCV 窗口
cv2.waitKey(0)
cv2.destroyAllWindows()