import numpy as np
import matplotlib.pyplot as plt
# 从 scikit-learn 中导入 make_moons 函数，用于生成非线性可分的数据集
from sklearn.datasets import make_moons
# 从 scikit-learn 中导入 train_test_split 函数，用于划分训练集和测试集
from sklearn.model_selection import train_test_split
# 从 scikit-learn 中导入 StandardScaler 类，用于特征标准化
from sklearn.preprocessing import StandardScaler
# 从 scikit-learn 中导入 KNeighborsClassifier 类，即 KNN 分类器
from sklearn.neighbors import KNeighborsClassifier

"""
K近邻(KNN)算法简介:
KNN是一种基于实例的学习算法，属于懒惰学习(Lazy Learning)的范畴。其核心思想是：
给定一个样本，根据它最邻近的k个训练样本的类别来决定其类别。

KNN算法步骤:
1. 计算待分类样本与所有训练样本的距离
2. 选择距离最近的k个样本
3. 统计这k个样本中各类别的数量
4. 将待分类样本归为数量最多的那个类别

KNN特点:
- 简单易懂，易于实现
- 无需训练过程(懒惰学习)
- 对异常值不敏感
- 计算量大(每次预测都需要计算距离)
- 对特征缩放敏感，需进行标准化或归一化
"""

# --- 数据准备 ---

# 1. 造一个二维玩具数据集（两半月）
"""
make_moons函数说明:
该函数用于生成两个交织的半圆形状的数据集，常用于测试分类算法性能
参数解释:
- n_samples: 生成的样本总数
- noise: 添加到数据中的噪声量，使问题更具挑战性
- random_state: 随机种子，确保结果可重现
返回值:
- X: 特征矩阵，形状为(n_samples, n_features)
- y: 标签向量，形状为(n_samples,)
"""
# make_moons：创建两个交织在一起的“半月形”数据，是一个经典的非线性分类问题。
# n_samples=400：总共生成 400 个数据点。
# noise=0.25：增加 0.25 的随机噪声，让分类问题稍微有点难度。
# random_state=42：设定随机种子，确保每次运行生成的数据集都一样，方便重现结果。
X, y = make_moons(n_samples=400, noise=0.25, random_state=42)
# X 是特征 (features)，形状是 (400, 2)，即 400 个点，每个点有 2 个坐标 (x1, x2)。
# y 是标签 (labels)，形状是 (400,)，即每个点对应的类别 (0 或 1)。


# 2. 划分训练集 / 测试集
"""
train_test_split函数说明:
该函数用于将数据集划分为训练集和测试集
参数解释:
- X, y: 待划分的特征和标签
- test_size: 测试集所占比例
- random_state: 随机种子，确保结果可重现
返回值:
- X_train, X_test: 训练集和测试集的特征
- y_train, y_test: 训练集和测试集的标签
"""
# 这是 AI 建模的**必经之路**，避免模型“作弊”（死记硬背）。
# train_test_split：按比例分割数据。
# test_size=0.3：将 30% 的数据作为测试集 (Test Set)，用于评估模型性能。70% 作为训练集 (Train Set)。
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
# X_train / y_train：用于训练模型 (70% 数据)。
# X_test / y_test：用于评估模型 (30% 数据)。


# 3. 特征标准化（非常重要）
"""
StandardScaler标准化说明:
KNN算法对特征的尺度非常敏感，因为它是基于距离度量的算法。如果不同特征的量纲差异很大，
会导致某些特征在距离计算中起主导作用，影响分类效果。因此需要对特征进行标准化处理。

标准化公式: z = (x - μ) / σ
其中μ是均值，σ是标准差，标准化后数据均值为0，标准差为1
"""
# 专业术语：特征缩放 / 标准化 (Feature Scaling / Standardization)
# 作用：将每个特征（这里的 x1 和 x2）转换成均值为 0、标准差为 1 的数据。
# 为什么要标准化？因为 KNN 依赖于距离计算。如果 x1 的数值范围是 1 到 1000，而 x2 的数值范围是 1 到 10，那么 x1 对距离的影响就会被不成比例地放大。标准化可以消除这种量纲（单位）影响。
scaler = StandardScaler()
# fit_transform：在**训练集**上计算均值和标准差，并应用转换。
X_train_scaled = scaler.fit_transform(X_train)
# transform：使用**训练集**上计算得到的均值和标准差，对**测试集**进行转换（**不能用测试集的数据来计算均值和标准差**，否则会导致数据泄露）。
X_test_scaled = scaler.transform(X_test)


# --- KNN 模型构建与训练 ---

# 4. 建一个 KNN 分类器
k = 5    # **K 值**：即我们找“最近的 K 个邻居”中的 K。这是一个**超参数 (Hyperparameter)**，可以调整。
"""
KNeighborsClassifier参数说明:
- n_neighbors: 近邻数量k值，这是KNN算法的核心参数
- metric: 距离度量方式，这里使用闵可夫斯基距离
- p: 当metric='minkowski'时，p=2表示欧氏距离，p=1表示曼哈顿距离
"""
knn = KNeighborsClassifier(
    n_neighbors=k,              # 指定 K 为 5
    metric="minkowski",         # 指定距离度量方式为闵可夫斯基距离
    p=2                         # 当 p=2 时，闵可夫斯基距离即为欧氏距离（默认值）
)

# 5. 训练
"""
KNN的"训练"过程:
KNN算法实际上没有传统意义上的训练过程，只是存储了训练数据。
在sklearn中，fit方法的作用是保存训练数据，供后续预测时使用
"""
# 对于 KNN 来说，fit() 方法只是简单地**记住**了所有的训练数据及其标签。
knn.fit(X_train_scaled, y_train)

# 6. 在测试集上评估一下
"""
score方法说明:
计算分类准确率，即正确分类的样本数占总样本数的比例
对于KNN，预测过程包括:
1. 对每个测试样本，计算它与所有训练样本的距离
2. 找出距离最近的k个训练样本
3. 根据这k个邻居的类别进行投票决定测试样本的类别
"""
# score() 方法会用模型对 X_test_scaled 进行预测，然后和真实的 y_test 进行对比，返回**准确率 (Accuracy)**。
test_acc = knn.score(X_test_scaled, y_test)
print(f"Test accuracy (k={k}): {test_acc:.3f}")


# --- 决策边界可视化 ---

# 7. 画决策边界
#   先在平面上铺一个网格，每个格子点用模型预测一下类别
# 决策边界 (Decision Boundary)：在特征空间中，将不同类别区域分开的界限。
# 目标：画出模型认为类别 0 和类别 1 应该被分开的曲线。

# 为了画图，把训练集+测试集合并一下，方便确定网格的范围
X_all_scaled = np.vstack([X_train_scaled, X_test_scaled])

# 确定特征 1 (x1) 和特征 2 (x2) 的最大最小值，用于确定绘图区域
x1_min, x1_max = X_all_scaled[:, 0].min() - 0.5, X_all_scaled[:, 0].max() + 0.5
x2_min, x2_max = X_all_scaled[:, 1].min() - 0.5, X_all_scaled[:, 1].max() + 0.5

"""
np.meshgrid函数说明:
用于生成网格点坐标矩阵，构建一个规则的二维网格
np.linspace: 在指定范围内生成等间距的点
"""
# np.meshgrid：创建一个网格坐标矩阵。
# 我们在 (x1_min, x1_max) 和 (x2_min, x2_max) 之间均匀地取 300 个点，形成一个 300x300 的网格。
xx1, xx2 = np.meshgrid(
    np.linspace(x1_min, x1_max, 300),
    np.linspace(x2_min, x2_max, 300)
)

"""
网格点预测说明:
将网格点展平后输入模型进行预测，得到每个网格点的类别，用于绘制决策边界
np.c_: 按列连接数组
ravel(): 将数组展平为一维
reshape(): 重塑数组形状以匹配网格结构
"""
# np.c_：将网格坐标 xx1, xx2 展开 (ravel) 并按列堆叠起来，形成一个 (90000, 2) 的矩阵。
# 矩阵的每一行都是网格中的一个点 (x1, x2)。这些点就是我们要让模型预测的“虚拟新数据点”。
grid_points = np.c_[xx1.ravel(), xx2.ravel()]
# 使用 KNN 模型对网格中的所有点进行**预测**。
Z = knn.predict(grid_points)
# 将预测结果 Z 重新整形回 300x300 的网格形状，以便用作绘图的颜色数据。
Z = Z.reshape(xx1.shape)

# 8. 画图
plt.figure(figsize=(6, 5))

# 决策边界（背景）
# contourf：画出等高线填充图。它根据 Z 的值（0 或 1）来给背景区域填充颜色，alpha=0.3 是设置透明度。
# 两种颜色区域的交界线，就是 KNN 的**决策边界**。
plt.contourf(xx1, xx2, Z, alpha=0.3)

# 训练数据点
plt.scatter(
    X_train_scaled[:, 0], X_train_scaled[:, 1],
    c=y_train, edgecolor="k", s=40, label="train"
)

# 测试数据点（用不同标记显示）
plt.scatter(
    X_test_scaled[:, 0], X_test_scaled[:, 1],
    c=y_test, marker="^", edgecolor="k", s=50, label="test" # marker="^" 表示三角形标记
)

plt.title(f"KNN decision boundary (k={k})")
plt.xlabel("feature 1 (scaled)")
plt.ylabel("feature 2 (scaled)")
plt.legend()
plt.tight_layout()
plt.show()