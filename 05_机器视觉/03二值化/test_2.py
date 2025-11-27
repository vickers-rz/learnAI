import cv2

img = cv2.imread("flower.png", 0)
blur = cv2.GaussianBlur(img, (5,5), 0)

# 1. 固定阈值
_, th1 = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)

# 2. Otsu
_, th2 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 3. 自适应阈值
th3 = cv2.adaptiveThreshold(blur, 255,
                            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                            cv2.THRESH_BINARY, 11, 2)


# 创建可调整大小的窗口
cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.namedWindow('Gaussian', cv2.WINDOW_NORMAL)
cv2.namedWindow('Binary', cv2.WINDOW_NORMAL)
cv2.namedWindow('Otsu', cv2.WINDOW_NORMAL)
cv2.namedWindow('Adaptive', cv2.WINDOW_NORMAL)

cv2.imshow("Original", img)
cv2.imshow("Gaussian", blur)
cv2.imshow("Binary", th1)
cv2.imshow("Otsu", th2)
cv2.imshow("Adaptive", th3)
cv2.waitKey(0)
cv2.destroyAllWindows()
