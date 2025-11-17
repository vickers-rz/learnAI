import cv2
import numpy as np
import matplotlib.pyplot as plt

# 创建一个空白的 700x700 彩色图像
image = np.zeros((700, 700, 3), dtype=np.uint8)

# 绘制黑色边框，每个 100x100 像素的块周围
block_size = 100
for i in range(0, 700, block_size):
    for j in range(0, 700, block_size):
        top_left = (j, i)
        bottom_right = (j + block_size - 1, i + block_size - 1)

        # 将特定位置的块用绿色填充
        if ((i // block_size == 1 or i // block_size == 5) and j // block_size in [2, 3, 4]) or (
                (j // block_size == 1 or j // block_size == 5) and i // block_size in [2, 3, 4]):
            cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), -1)  # 使用 -1 填充矩形为绿色
        cv2.rectangle(image, top_left, bottom_right, (255, 255, 255), 2)  # 绘制其他块的白色边框

# 将 BGR 通道顺序转换为 RGB 顺序，用于 Matplotlib 显示
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 在 Jupyter Notebook 中显示原始图像
plt.imshow(image_rgb)
plt.title('Original Image')
plt.axis('off')  # 不显示坐标轴
plt.show()

# 拆分彩色通道
b, g, r = cv2.split(image)

# 创建空白图像，用于每个通道
blue_channel = np.zeros((700, 700, 3), dtype=np.uint8)
green_channel = np.zeros((700, 700, 3), dtype=np.uint8)
red_channel = np.zeros((700, 700, 3), dtype=np.uint8)

# 分配颜色通道数据
blue_channel[:, :, 0] = b
green_channel[:, :, 1] = g
red_channel[:, :, 2] = r

# 将 BGR 通道顺序转换为 RGB 顺序，用于 Matplotlib 显示
blue_channel_rgb = cv2.cvtColor(blue_channel, cv2.COLOR_BGR2RGB)
green_channel_rgb = cv2.cvtColor(green_channel, cv2.COLOR_BGR2RGB)
red_channel_rgb = cv2.cvtColor(red_channel, cv2.COLOR_BGR2RGB)

# 在 Jupyter Notebook 中显示拆分的颜色通道
plt.subplot(131)
plt.imshow(blue_channel_rgb)
plt.title('Blue Channel')
plt.axis('off')

plt.subplot(132)
plt.imshow(green_channel_rgb)
plt.title('Green Channel')
plt.axis('off')

plt.subplot(133)
plt.imshow(red_channel_rgb)
plt.title('Red Channel')
plt.axis('off')

plt.tight_layout()
plt.show()
