"""
1. 找出只在 group_a 中出现的水果。
2. 找出同时在 group_a 和 group_b 中出现，但不在 group_c 中出现的水果。
3. 找出所有只在一个组中出现的水果（A独有 或 B独有 或 C独有）。
"""
group_a = ['apple', 'banana', 'orange', 'grape']
group_b = ['banana', 'grape', 'watermelon']
group_c = ['orange', 'peach']

# 转成集合
set_a = set(group_a)
set_b = set(group_b)
set_c = set(group_c)

# a - b
print(set_a - set_b - set_c)

# (a & b) - c
print(set_a & set_b - set_c)

# a ^ b ^ c
print(set_a ^ set_b ^ set_c)


list1 = [1, 2, 3, 4, 5, 5]
list2 = [4, 5, 6, 7, 8, 5]

set1 = set(list1)
set2 = set(list2)

print(set1 & set2)