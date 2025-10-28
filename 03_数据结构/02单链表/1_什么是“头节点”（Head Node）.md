### 🧩 一、什么是“头节点”（Head Node）

在链表中：

- 每个节点（Node）都保存两样东西：
  1. `data`：节点的数据内容
  2. `next`：指向下一个节点的“引用”或“指针”

而**整个链表的入口**就是第一个节点的引用，也就是 **`head`（头节点）**。

举个例子👇：

```
head → [data: 5 | next →] → [data: 8 | next →] → [data: 12 | next → None]
```

- `head` 指向第一个节点（值 5）
- 然后每个节点通过 `next` 连接到下一个
- 最后一个节点的 `next` 是 `None`，表示链表结束

------

### 🧠 二、为什么 `head = None` 表示空链表？

- 在 Python 中，`None` 是一个特殊的值，表示“没有东西”。

- 当 `head` 是 `None` 时，意思就是：

  > 链表没有第一个节点，自然也没有其他节点。

换句话说：

> 如果连“入口”都没有，就没有办法访问任何节点 → 整个链表为空。

------

### 💡 类比理解（生活化）

想象链表是一串风筝：

- 第一个风筝绑在你的手上（这就是 `head`）
- 每个风筝线连接下一个（这就是 `next`）
- 如果你手上没有风筝（`head = None`）
   👉 那就说明天上没有任何风筝，这串“链”是空的。

------

### 🧾 小实验（Python 验证）

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None  # 初始化时为空链表

ll = LinkedList()
print(ll.head)           # 输出 None
print(ll.head is None)   # True → 确认这是空链表
```

输出：

```
None
True
```

此时，链表里没有节点，`head` 没指向任何 Node —— 所以它是空链表。

------

### ✅ 小结

| 判断条件           | 含义     | 说明           |
| ------------------ | -------- | -------------- |
| `head is None`     | 空链表   | 没有任何节点   |
| `head is not None` | 非空链表 | 至少有一个节点 |