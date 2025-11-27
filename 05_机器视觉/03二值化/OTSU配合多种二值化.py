# 使用OTSU去计算合适的阈值，并且结合阈值法进行二值化

import cv2
import numpy as np

# 1.读取要二值化的彩色图
image_np = cv2.imread('./flower.png')

# 2. 进行灰度化
image_gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

# 使用不同的二值化方法结合OTSU
maxval = 255

# OTSU + THRESH_BINARY（标准二值化）
ret_binary, thresh_binary = cv2.threshold(image_gray, 0, maxval, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# OTSU + THRESH_BINARY_INV（反向二值化）
ret_binary_inv, thresh_binary_inv = cv2.threshold(image_gray, 0, maxval, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# OTSU + THRESH_TRUNC（截断阈值化）
ret_trunc, thresh_trunc = cv2.threshold(image_gray, 0, maxval, cv2.THRESH_TRUNC + cv2.THRESH_OTSU)

# OTSU + THRESH_TOZERO（阈值化到零）
ret_tozero, thresh_tozero = cv2.threshold(image_gray, 0, maxval, cv2.THRESH_TOZERO + cv2.THRESH_OTSU)

# OTSU + THRESH_TOZERO_INV（反向阈值化到零）
ret_tozero_inv, thresh_tozero_inv = cv2.threshold(image_gray, 0, maxval, cv2.THRESH_TOZERO_INV + cv2.THRESH_OTSU)

# 创建可调整大小的窗口
cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Gray Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('OTSU + BINARY', cv2.WINDOW_NORMAL)
cv2.namedWindow('OTSU + BINARY_INV', cv2.WINDOW_NORMAL)
cv2.namedWindow('OTSU + TRUNC', cv2.WINDOW_NORMAL)
cv2.namedWindow('OTSU + TOZERO', cv2.WINDOW_NORMAL)
cv2.namedWindow('OTSU + TOZERO_INV', cv2.WINDOW_NORMAL)

# 显示图像
cv2.imshow('Original Image', image_np)
cv2.imshow('Gray Image', image_gray)
cv2.imshow('OTSU + BINARY', thresh_binary)
cv2.imshow('OTSU + BINARY_INV', thresh_binary_inv)
cv2.imshow('OTSU + TRUNC', thresh_trunc)
cv2.imshow('OTSU + TOZERO', thresh_tozero)
cv2.imshow('OTSU + TOZERO_INV', thresh_tozero_inv)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 保存结果图像
cv2.imwrite('otsu_binary.png', thresh_binary)
cv2.imwrite('otsu_binary_inv.png', thresh_binary_inv)
cv2.imwrite('otsu_trunc.png', thresh_trunc)
cv2.imwrite('otsu_tozero.png', thresh_tozero)
cv2.imwrite('otsu_tozero_inv.png', thresh_tozero_inv)
