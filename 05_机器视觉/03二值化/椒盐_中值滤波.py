import cv2
import numpy as np

img = cv2.imread("flower.png", 0)

# 添加椒盐噪声
def add_salt_pepper_noise(image, salt_prob=0.01, pepper_prob=0.01):
    noisy_image = np.copy(image)
    # 添加盐噪声（白色点）
    num_salt = np.ceil(salt_prob * image.size * 0.5)
    coords = [np.random.randint(0, i-1, int(num_salt)) for i in image.shape]
    noisy_image[coords[0], coords[1]] = 255
    
    # 添加胡椒噪声（黑色点）
    num_pepper = np.ceil(pepper_prob * image.size * 0.5)
    coords = [np.random.randint(0, i-1, int(num_pepper)) for i in image.shape]
    noisy_image[coords[0], coords[1]] = 0
    
    return noisy_image

noisy_img = add_salt_pepper_noise(img, 0.01, 0.01)

# 使用中值滤波处理椒盐噪声
median_blur = cv2.medianBlur(noisy_img, 5)

# 1. 固定阈值
_, th1 = cv2.threshold(median_blur, 127, 255, cv2.THRESH_BINARY)

# 2. Otsu
_, th2 = cv2.threshold(median_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 3. 自适应阈值
th3 = cv2.adaptiveThreshold(median_blur, 255,
                            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                            cv2.THRESH_BINARY, 11, 2)


# 创建可调整大小的窗口
cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.namedWindow('Noisy Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Median Filter', cv2.WINDOW_NORMAL)
cv2.namedWindow('Binary', cv2.WINDOW_NORMAL)
cv2.namedWindow('Otsu', cv2.WINDOW_NORMAL)
cv2.namedWindow('Adaptive', cv2.WINDOW_NORMAL)

cv2.imshow("Original", img)
cv2.imshow("Noisy Image", noisy_img)
cv2.imshow("Median Filter", median_blur)
cv2.imshow("Binary", th1)
cv2.imshow("Otsu", th2)
cv2.imshow("Adaptive", th3)
cv2.waitKey(0)
cv2.destroyAllWindows()
