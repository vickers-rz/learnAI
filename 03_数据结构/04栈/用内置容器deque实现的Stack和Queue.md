## (一)、**栈**（Stack）的构建
在 **Python** 中，确实可以使用 **`list`**（列表） 来构建 **栈**（Stack），但这只是最直接的一种方式。我们来系统地看看常见的几种实现方式👇

### ✅ 1. 使用 Python 内置的 `list`

最简单、最常见的实现。

```python
stack = []
stack.append(10)   # 入栈
stack.append(20)
print(stack.pop()) # 出栈 -> 20
```

**特点：**

- `append()` 和 `pop()` 操作都在列表末尾进行，效率高（O(1)）。
- **缺点**：列表在频繁扩容时可能有轻微性能损耗。

------

### ✅ 2. 使用 `collections.deque`

推荐的高效实现方式。

```python
from collections import deque

stack = deque()
stack.append(10)
stack.append(20)
print(stack.pop())  # 出栈 -> 20
```

**优点：**

- 双端队列（deque）在两端插入、删除操作的时间复杂度都是 O(1)。
- 比 `list` 更适合频繁进出栈操作。

------

### ✅ 3. 使用自定义类 + 链表节点结构

模拟底层数据结构，实现更清晰的逻辑。

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if not self.top:
            raise IndexError("Stack is empty")
        value = self.top.value
        self.top = self.top.next
        return value
```

**优点：**

- 更贴近底层数据结构原理。
- 不依赖 Python 容器。

------



## (二)、 **队列（Queue）** 的构建

在 **Python** 里实现 **队列（Queue）**，最推荐、最常用、最高效的方式就是用 **`collections.deque`**。

------

### 🧩 一、为什么 `deque` 适合实现队列

`deque` 的名字就是 **“double-ended queue（双端队列）”**，
 它支持在**两端 O(1) 时间插入和删除**，这正好符合队列的操作特性：

- **入队（enqueue）**：从右端（尾部）插入
- **出队（dequeue）**：从左端（头部）删除

```python
from collections import deque

queue = deque()

# 入队
queue.append('A')
queue.append('B')
queue.append('C')

# 出队
print(queue.popleft())  # 输出: A
print(queue)            # deque(['B', 'C'])
```

✅ 时间复杂度：

- `append()` 和 `popleft()` 都是 **O(1)**。
- 而如果用 `list.pop(0)` 实现出队，是 **O(n)**（因为所有元素要前移），效率很低。

------

### 🧱 二、对比一下常见队列实现方式

| 实现方式            | 出队复杂度 | 线程安全 | 备注                     |
| ------------------- | ---------- | -------- | ------------------------ |
| `list`              | ❌ O(n)     | ❌        | 删除第一个元素慢         |
| `collections.deque` | ✅ O(1)     | ❌        | 推荐用于普通队列         |
| `queue.Queue`       | ✅ O(1)     | ✅        | 线程安全，用于多线程任务 |
| `asyncio.Queue`     | ✅ O(1)     | ✅        | 异步任务队列（协程）     |

------

### 🧩 三、几种典型使用方式

#### 1️⃣ 普通队列（单线程）

```python
from collections import deque

queue = deque()
queue.append('task1')
queue.append('task2')
print(queue.popleft())  # task1
```

------

#### 2️⃣ 双端队列（可从两端操作）

```python
from collections import deque

dq = deque()
dq.append('right')
dq.appendleft('left')
print(dq.pop())       # right
print(dq.popleft())   # left
```

------

#### 3️⃣ 线程安全队列（多线程环境）

```python
import queue

q = queue.Queue()
q.put('task1')
q.put('task2')
print(q.get())   # task1
```

> `queue.Queue()` 底层其实也用链表实现，只是加了锁，保证线程安全。

------

### 🧠 四、总结

| 场景                | 推荐结构            | 说明                                |
| ------------------- | ------------------- | ----------------------------------- |
| 普通队列            | `collections.deque` | 简单、高效                          |
| 线程安全队列        | `queue.Queue`       | 内置锁机制                          |
| 异步任务队列        | `asyncio.Queue`     | 协程环境使用                        |
| 双端操作（栈+队列） | `collections.deque` | 同时支持 `append`、`pop`、`popleft` |

------

👉 **结论：**

> 是的，Python 的队列最常用的实现方式就是 `deque`，
>  它简单、高效、灵活，是“面试常问 + 实战常用”的核心结构。

------