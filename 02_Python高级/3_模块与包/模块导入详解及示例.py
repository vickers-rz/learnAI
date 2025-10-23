"""
Python模块导入详解及示例
"""

# 1. import 模块
# 特点：导入整个模块，使用时需要通过"模块名.对象名"访问
# 优点：命名空间清晰，避免命名冲突
# 缺点：每次使用都需要写模块前缀
import math
result = math.sqrt(16)
print(f"使用import导入模块: sqrt(16) = {result}")

# 2. import 模块 as 别名
# 特点：为模块指定简短别名
# 优点：减少代码长度，提高可读性
# import numpy as np
# 示例：np.array([1, 2, 3]) 创建数组

# 3. from 模块 import 子模块
# 特点：只导入指定的对象，直接使用无需前缀
# 优点：代码简洁，只导入需要的内容
from math import sqrt
result = sqrt(25)
print(f"使用from...import导入特定对象: sqrt(25) = {result}")

# 4. from 模块 import *
# 特点：导入模块中所有公开对象
# 限制：受__all__列表控制，只导入列表中指定的对象
# 缺点：容易造成命名冲突，降低代码可读性，不推荐在生产环境使用
from math import *
result = sin(pi/2)
print(f"使用from...import *导入所有对象: sin(π/2) = {result}")

# 5. from 模块 import 子模块 as 别名
# 特点：导入特定对象并重命名
# 优点：避免命名冲突，简化长名称
from datetime import datetime as dt
current_time = dt.now()
print(f"使用别名导入: 当前时间 {current_time}")

# __name__ 和 __main__ 的使用
# __name__ 是 Python 中的一个特殊变量，用于标识当前模块的名称
# __main__ 是 __name__ 变量的一个特殊值，表示当前模块是作为主程序直接运行的

def demo_function():
    """演示函数"""
    return "这是一个演示函数"

# 当模块被直接运行时执行以下代码块
if __name__ == '__main__':
    print("这是模块作为主程序直接运行时的输出")
    print(demo_function())
    
    # 展示各种导入方式的效果
    print("=" * 50)
    print("Python模块导入方式演示完成")