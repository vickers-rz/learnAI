"""

1️⃣ **内建模块（built-in modules）**
2️⃣ **标准库模块（standard library modules）**
3️⃣ **第三方模块（third-party modules）**

我们来一步步拆解👇

---

## 🧩 一、内建模块（built-in modules）

* ✅ **Python 解释器在启动时就已经加载（编译）进内存的模块**
* 🧠 **不需要 `import` 也能直接用**（有些甚至是直接可用的函数、类型）
* 📦 它们是 Python 解释器“核心的一部分”

📘 **例子：**

```python
len([1,2,3])
print()
type(5)
```

这里的 `len`、`print`、`type` 都来自于内建模块（实际上是来自 `builtins` 模块）。

👉 你甚至可以看到：

```python
import builtins
dir(builtins)
```

会列出所有 Python 自带的内建函数。

---

## 📚 二、标准库模块（standard library）

* ✅ **随 Python 一起安装**，但**不是自动加载**；
* ❗️**使用前需要 `import`**；
* 📦 你不需要 `pip install`；
* 它们被打包在你的 Python 安装目录下（通常在 `Lib/` 文件夹中）。

📘 **例子：**

```python
import math
import os
import datetime
import json
import re
```

这些模块是“官方内置随 Python 一起发布的标准模块”，所以使用它们时：

* 不需要 pip；
* 但需要手动 `import`。

---

## 🧱 三、第三方模块（third-party modules）

* 🚀 **不是 Python 自带的**
* 🧩 需要通过 `pip install` 下载和安装
* 一般存放在 `site-packages` 目录

📘 **例子：**

```bash
pip install requests numpy pandas
```

然后在代码中：

```python
import requests
import numpy as np
```

---

## ✅ 四、对比总结表

| 类型                      | 是否随 Python 自带 | 是否需要 import   | 是否需要 pip 安装 | 例子                                      |
| ----------------------- | ------------- | ------------- | ----------- | --------------------------------------- |
| 内建模块（built-in）          | ✅ 是           | ❌ 不一定（很多直接可用） | ❌ 不需要       | `print`, `len`, `type`, `builtins`      |
| 标准库模块（standard library） | ✅ 是           | ✅ 需要          | ❌ 不需要       | `math`, `os`, `sys`, `json`, `datetime` |
| 第三方模块（third-party）      | ❌ 否           | ✅ 需要          | ✅ 需要        | `requests`, `numpy`, `pandas`           |

---

## 💡 小技巧：快速判断模块类型

可以在 Python 交互模式下用：

```python
import sys
import math
import requests

print(sys.builtin_module_names)  # 所有内建模块名称
```

如果一个模块在这个列表里，它是 built-in；
如果不是，但不用 pip 就能 import —— 它属于标准库；
如果必须 pip 安装，那就是第三方。

---

 __name__，是模块的内置变量
__doc__，表示模块的文档字符串
 __file__，表示模块文件路径
在 Python 中，如果你想查看模块的内置变量、函数、类等名称，可以使用内置函数 dir()

"""