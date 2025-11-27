from skimage import data
import matplotlib.pyplot as plt

# 使用其他可用图像，如 coins, astronaut, camera 等
image = data.astronaut()  # 或 data.coins(), data.camera()
image2 = data.coins()  # 或 data.coins(), data.camera()
image3 = data.camera()  # 或 data.coins(), data.camera()

plt.imshow(image)
plt.axis('off')
plt.show()
plt.imshow(image2)
plt.axis('off')
plt.show()
plt.imshow(image3)
plt.axis('off')
plt.show()
