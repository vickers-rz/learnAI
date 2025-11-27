import numpy as np
import cv2

def otsu_threshold(image):
    """
    OTSU算法实现 - 最大类间方差法
    原理：寻找一个最佳阈值，使得前景和背景之间的类间方差最大
    """
    # 1. 统计直方图 - 统计每个灰度级出现的次数
    # 统计图像中每个灰度级(0-255)的像素数量，形成直方图
    # flatten()将二维图像矩阵转换为一维数组
    # minlength=256确保输出数组长度为256，对应0-255个灰度级
    histogram = np.bincount(image.flatten(), minlength=256)
    total = image.size  # 获取图像总像素数，用于后续计算概率

    # 2. 计算每个灰度级的概率 p(i) = histogram(i) / total
    # prob[i] 表示灰度值为i的像素在整幅图像中出现的概率
    prob = histogram / total

    # 3. 计算累积概率 ω0(T) - 背景像素占总像素的比例
    # ω0(T) = Σ(p(i)) for i=0 to T
    # 表示灰度值从0到T的像素占总像素的比例（背景比例）
    omega = np.cumsum(prob)

    # 4. 计算累积均值 μ0(T) - 背景像素的平均灰度值
    # μ0(T) = Σ(i * p(i)) for i=0 to T
    # 表示背景区域的平均灰度值
    mu = np.cumsum(prob * np.arange(256))

    # 5. 计算整个图像的灰度平均值 μ
    # μ = Σ(i * p(i)) for i=0 to 255
    # 表示整幅图像的平均灰度值
    mu_total = mu[-1]

    # 6. 根据OTSU公式计算类间方差 σ²_b(T)
    # 类间方差公式推导：
    # 设前景比例 ω1(T) = 1 - ω0(T)
    # 设前景平均灰度 μ1(T) = (μ - ω0(T) * μ0(T)) / ω1(T)
    # 类间方差 σ²_b(T) = ω0(T) * ω1(T) * (μ0(T) - μ1(T))²
    # 经过数学变换可得：
    # σ²_b(T) = (μ * ω0(T) - μ0(T))² / (ω0(T) * (1 - ω0(T)))
    
    # 添加1e-6是为了防止分母为0的情况
    sigma_between = (mu_total * omega - mu)**2 / (omega * (1 - omega) + 1e-6)

    # 7. 找到使类间方差最大的阈值 T
    # 根据OTSU算法原理，最佳阈值就是使类间方差最大的那个值
    best_T = np.argmax(sigma_between)
    return best_T



# 读取彩色图像
img_color = cv2.imread("flower.png")  # 彩色图
# 转换为灰度图
img = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
T = otsu_threshold(img)
print("OTSU 阈值 =", T)

# 应用阈值
_, binary = cv2.threshold(img, T, 255, cv2.THRESH_BINARY)

# 创建可调整窗口显示结果
cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Grayscale Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Binary Image', cv2.WINDOW_NORMAL)

# 显示原图、灰度图和二值化结果
cv2.imshow("Original Image", img_color)
cv2.imshow("Grayscale Image", img)
cv2.imshow("Binary Image", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
