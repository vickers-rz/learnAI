import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier

# ==========================================
# 第一阶段：准备工作
# ==========================================

# 1. 载入数据
# X 是特征 (长宽数据), y 是标签 (花的品种)
iris = load_iris()
X = iris.data
y = iris.target

# 2. 划分“训练集”和“独立测试集”
# 注意：这个 X_test 是我们留到最后真正的“期末考试”，选 K 值的时候绝对不能看它！
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=4, test_size=0.25)

# ==========================================
# 第二阶段：循环评估 (寻找最佳 K)
# ==========================================

# 我们想尝试从 k=1 到 k=30 的效果
k_range = range(1, 31)
k_scores = []  # 用来记录每个 k 值对应的平均分数

print("开始寻找最佳 K 值...")

for k in k_range:
    # 1. 建立当前的 KNN 模型 (假设邻居数为 k)
    knn = KNeighborsClassifier(n_neighbors=k)

    # 2. 核心步骤：交叉验证 (Cross Validation)
    # cv=5 表示 5 折交叉验证 (5-Fold)
    # scoring='accuracy' 表示我们要看准确率
    # 这行代码自动完成了：切分数据 -> 训练 -> 验证 -> 算分 -> 算平均
    scores = cross_val_score(knn, X_train, y_train, cv=5, scoring='accuracy')

    # 3. 记录平均分
    k_scores.append(scores.mean())
    # print(f"当 k={k} 时，5折交叉验证的平均准确率为: {scores.mean():.4f}")

# ==========================================
# 第三阶段：可视化与决策
# ==========================================

# 绘制 K 值与准确率的关系图
plt.figure(figsize=(10, 6))
plt.plot(k_range, k_scores, marker='o')  # 画出折线图
plt.xlabel('Value of K for KNN')  # X轴：K值
plt.ylabel('Cross-Validated Accuracy')  # Y轴：准确率
plt.title('Finding the Best K Value')
plt.grid(True)
plt.show()

# 找出分数最高的那个 K
best_score = max(k_scores)
best_k = k_range[k_scores.index(best_score)]

print(f"结论：在交叉验证中表现最好的 K 值是 {best_k}，准确率为 {best_score:.4f}")

# ==========================================
# 第四阶段：最终模型的应用
# ==========================================

# 使用最佳 K 值，在“整个训练数据”上重新训练
final_knn = KNeighborsClassifier(n_neighbors=best_k)
final_knn.fit(X_train, y_train)

# 真正的“期末考试”：在从未见过的测试集上评估
final_accuracy = final_knn.score(X_test, y_test)
print(f"最终模型(k={best_k})在独立测试集上的准确率: {final_accuracy:.4f}")