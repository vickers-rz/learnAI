# 导入必须的库
from sklearn.neighbors import KNeighborsClassifier # 导入KNN分类器模型
import numpy as np
import matplotlib.pyplot as plt

# --- 数据准备 ---

# 1、定义数据集
# 这里我们不使用文件或自动生成的方式，而是手动定义三组二维数据点。
# 每一组代表一个不同的类别。
point1 = [[7.7, 6.1], [3.1, 5.9], [8.6, 8.8], [9.5, 7.3], [3.9, 7.4], [5.0, 5.3], [1.0, 7.3]]
point2 = [[0.2, 2.2], [4.5, 4.1], [0.5, 1.1], [2.7, 3.0], [4.7, 0.2], [2.9, 3.3], [7.3, 7.9]]
point3 = [[9.2, 0.7], [9.2, 2.1], [7.3, 4.5], [8.9, 2.9], [9.5, 3.7], [7.7, 3.7], [9.4, 2.4]]

# 点集特征的合并
# np.concatenate：将多个数组（这里是 point1, point2, point3）沿指定轴连接起来。
# axis=0：表示垂直方向（按行）连接，最终形成一个包含所有数据点的特征矩阵。
np_train_data = np.concatenate((point1, point2, point3), axis=0)
# np_train_data 的形状将是 (21, 2)，代表 21 个数据点，每个点有 2 个特征。

# 根据输入的数据创建标签
# 我们为每个类别手动创建标签：point1 对应标签 0，point2 对应标签 1，point3 对应标签 2。
# [0] * len(point1) 会生成一个包含 7 个 0 的列表，以此类推。
# np.array() 将列表转换为 NumPy 数组。
np_train_label = np.array([0] * len(point1) + [1] * len(point2) + [2] * len(point3))
# np_train_label 的形状是 (21,)，与 np_train_data 中的每个点一一对应。


# --- KNN 模型构建与训练 ---

# 2、构建KNN算法：实例化KNN算法，KNN训练
# 初始化K近邻分类器
# KNeighborsClassifier(1)：创建一个 KNN 分类器实例。
# 参数 1 代表 K 值 (n_neighbors=1)，即每个点的分类由它最近的 1 个邻居决定。
knn_clf = KNeighborsClassifier(1)

# 训练
# 对于 KNN 来说，fit() 方法非常简单，它只是将训练数据 (np_train_data) 和对应的标签 (np_train_label) “记住”并存储起来。
knn_clf.fit(np_train_data, np_train_label)


# --- 决策边界可视化 ---

# 3、设定未知点，设定坐标点网络
# 定义绘图区域的边界 [x_min, x_max, y_min, y_max]
axis = [0, 10, 0, 10]

# 生成坐标点网络，用于绘制决策边界
# np.linspace(start, stop, num)：在指定的间隔内返回均匀间隔的数字。
# np.meshgrid()：从坐标向量返回坐标矩阵，简单说就是创建一个覆盖整个绘图区域的网格。
x0, x1 = np.meshgrid(
    np.linspace(axis[0], axis[1], 100),  # 在 x 轴 (0到10) 上均匀生成 100 个点
    np.linspace(axis[2], axis[3], 100)  # 在 y 轴 (0到10) 上均匀生成 100 个点
)
# x0 和 x1 都是 100x100 的矩阵，分别存储了网格中每个点的 x 和 y 坐标。

# np.c_[]：将网格坐标 x0, x1 展开 (ravel) 并按列堆叠起来，形成一个 (10000, 2) 的矩阵。
# 矩阵的每一行都是网格中的一个点 (x, y)，这些点就是我们要让模型预测的“虚拟新数据点”。
axis_xy = np.c_[x0.ravel(), x1.ravel()]

# 4、KNN的预测与绘制决策边界
# 使用训练好的 KNN 模型对网格中的所有点进行**预测**。
y_predict = knn_clf.predict(axis_xy)
# y_predict 现在是一个包含 10000 个预测标签 (0, 1, 或 2) 的一维数组。

# 将预测结果 y_predict 重新整形回 100x100 的网格形状，以便用作绘图的颜色或等高线数据。
y_predict = y_predict.reshape(x0.shape)

# 等高线的绘制
# plt.contour()：绘制等高线。在这里，它会画出不同预测类别区域之间的分界线，即**决策边界**。
plt.contour(x0, x1, y_predict)

# 使用散点图绘制原始的训练数据点
# np_train_label == 0 会返回一个布尔数组，用于选择所有标签为 0 的数据点。
# np_train_data[..., 0] 选择这些点的 x 坐标，np_train_data[..., 1] 选择 y 坐标。
plt.scatter(np_train_data[np_train_label == 0, 0], np_train_data[np_train_label == 0, 1], marker="^") # 类别0用三角形表示
plt.scatter(np_train_data[np_train_label == 1, 0], np_train_data[np_train_label == 1, 1], marker="*") # 类别1用星号表示
plt.scatter(np_train_data[np_train_label == 2, 0], np_train_data[np_train_label == 2, 1], marker="s") # 类别2用正方形表示

# 显示最终的图形
plt.show()
