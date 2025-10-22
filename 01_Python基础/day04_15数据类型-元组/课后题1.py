"""
**11.**
给定一个包含元组的列表
items = [('apple', 2.5), ('banana', 1.8), ('orange', 3.0), ('grape', 2.8)]
其中每个元组代表（商品名称, 价格）。
编写一个 Python 脚本，根据元组中的价格（第二个元素）对这个列表进行升序排序，并打印排序后的列表。
"""
"""
items = [('apple', 2.5), ('banana', 1.8), ('orange', 3.0), ('grape', 2.8)]
price_max = items[0][1]
for i in range(len(items)):
    price = items[i][1]
    if price_max < price:
        price_max = price
        print(f"{price_max}")
"""
'''
items = [('apple', 2.5), ('banana', 1.8), ('orange', 3.0), ('grape', 2.8)]
price_max = items[0][1]
sorted_items = []
for i in range(len(items)):
    price = items[i][1]
    if price_max < price:
        price_max = price
        sorted_items.append(items[i])
print(sorted_items)
'''

items = [('apple', 2.5), ('banana', 1.8), ('orange', 3.0), ('grape', 2.8)]
# 定义一个函数来取出价格
def get_price(item):
    return item[1]

# 用 sorted，不改变原列表
sorted_items = sorted(items, key=get_price)

print(sorted_items)

items = [('apple', 2.5), ('banana', 1.8), ('orange', 3.0), ('grape', 2.8)]

# 使用冒泡排序
for i in range(len(items) - 1):          # 外层循环控制轮数
    for j in range(len(items) - 1 - i):  # 内层循环比较相邻两个元素
        if items[j][1] > items[j + 1][1]:  # 如果前一个价格比后一个大，就交换
            temp = items[j]
            items[j] = items[j + 1]
            items[j + 1] = temp

print(items)

