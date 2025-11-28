import cv2
import numpy as np

# 读取图像
img = cv2.imread("lena.png")
# 如果没有lena.png，创建一个示例图像
if img is None:
    # 创建一个示例图像
    img = np.zeros((200, 200, 3), dtype=np.uint8)
    # 添加一些图形元素以便观察边缘填充效果
    cv2.rectangle(img, (50, 50), (150, 150), (255, 255, 255), -1)
    cv2.circle(img, (100, 100), 30, (0, 0, 255), -1)
    cv2.line(img, (0, 0), (200, 200), (0, 255, 0), 5)

# 设置边界大小
top, bottom, left, right = 50, 50, 50, 50

# 使用不同的边界填充方式
# BORDER_REPLICATE: 复制边缘像素
# 应用场景：适用于希望边界保持与原图边缘一致性的场合，如某些滤波操作
# 效果：边缘像素向外重复扩展，形成"平铺"效果
replicate = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_REPLICATE)

# BORDER_REFLECT: 镜像反射
# 应用场景：适用于希望减少边缘突兀感的场合，使边界过渡更自然，常用于卷积操作
# 效果：以边缘为轴进行镜像反射，边缘呈现对称分布
reflect = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_REFLECT)

# BORDER_REFLECT_101: 镜像反射(另一种方式)
# 应用场景：与BORDER_REFLECT类似，但镜像时不复制边缘像素，适用于需要更自然过渡的场合
# 效果：类似于BORDER_REFLECT，但不包括最边缘的像素
reflect_101 = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_REFLECT_101)

# BORDER_CONSTANT: 常数填充(用红色)
# 应用场景：适用于需要突出显示原图边界或添加装饰性边框的场合
# 效果：用指定颜色填充边界，形成明显的分界线
constant = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[0, 0, 255])

# 创建可调整大小的窗口
cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.namedWindow('BORDER_REPLICATE', cv2.WINDOW_NORMAL)
cv2.namedWindow('BORDER_REFLECT', cv2.WINDOW_NORMAL)
cv2.namedWindow('BORDER_REFLECT_101', cv2.WINDOW_NORMAL)
cv2.namedWindow('BORDER_CONSTANT', cv2.WINDOW_NORMAL)

# 显示图像
cv2.imshow("Original", img)
cv2.imshow("BORDER_REPLICATE", replicate)
cv2.imshow("BORDER_REFLECT", reflect)
cv2.imshow("BORDER_REFLECT_101", reflect_101)
cv2.imshow("BORDER_CONSTANT", constant)

cv2.waitKey(0)
cv2.destroyAllWindows()
