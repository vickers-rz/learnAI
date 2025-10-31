"""
线性查找算法 (Linear Search)
==========================

线性查找算法在 Python 中可以使用以下哪种语句实现？

一、线性查找（Linear Search）的原理
----------------------------------

线性查找就是从头到尾依次扫描序列，
直到找到目标元素或遍历完所有元素为止。

其本质是顺序遍历，没有固定的实现方式限制。
在 Python 中，可以用多种语法结构实现。

二、实现方式
------------

1. 使用 for 循环 (最常见的实现方式)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

>>> def linear_search(lst, target):
...     for i in range(len(lst)):
...         if lst[i] == target:
...             return i
...     return -1

2. 使用 while 循环
~~~~~~~~~~~~~~~~~

>>> def linear_search(lst, target):
...     i = 0
...     while i < len(lst):
...         if lst[i] == target:
...             return i
...         i += 1
...     return -1

3. 使用递归函数
~~~~~~~~~~~~~~

>>> def linear_search_recursive(lst, target, index=0):
...     if index == len(lst):
...         return -1
...     if lst[index] == target:
...         return index
...     return linear_search_recursive(lst, target, index + 1)

三、结论
--------
线性查找既可以用 for 循环、也可以用 while 循环，甚至递归函数实现。

"""