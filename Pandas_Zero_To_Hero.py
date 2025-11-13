"""
Pandas零基础入门教程
====================

这份教程将带你从零开始学习Pandas，即使你没有任何编程经验。
我们将逐步介绍Pandas的核心概念和功能，并提供实际示例。

什么是Pandas？
-------------

Pandas是一个强大的Python数据分析库，它提供了高效的数据结构和数据分析工具，
特别适用于处理结构化数据（如表格数据）。Pandas是基于NumPy构建的，因此它也具备
很好的性能。

Pandas有两个主要的数据结构：
1. Series：一维数组，类似于带标签的数组
2. DataFrame：二维表格，类似于Excel中的表格或数据库中的表

本教程将首先介绍Series，然后是DataFrame。
"""

# 导入必要的库
import pandas as pd
import numpy as np

print("=== Pandas零基础入门教程 ===\\n")

print("第1部分：认识Pandas中的Series")
print("-------------------------")

print("1.1 什么是Series？")
print("Series是一种类似于一维数组的对象，由一组数据和相关的数据标签（即索引）组成。")
print("每一个Series都可以看作是由两个数组组成的：一个用来存储数据，另一个用来存储数据的标签。\\n")

# 创建一个最简单的Series
print("1.2 创建Series")
print("方法1：使用列表创建Series")

data_list = [10, 20, 30, 40, 50]
simple_series = pd.Series(data_list)
print("使用列表 [10, 20, 30, 40, 50] 创建的Series:")
print(simple_series)
print()

# 带自定义索引的Series
print("方法2：创建带自定义索引的Series")
custom_index = ['a', 'b', 'c', 'd', 'e']
indexed_series = pd.Series(data_list, index=custom_index)
print("使用相同数据但自定义索引 ['a', 'b', 'c', 'd', 'e'] 的Series:")
print(indexed_series)
print()

# 使用字典创建Series
print("方法3：使用字典创建Series")
data_dict = {'苹果': 5, '香蕉': 10, '橙子': 8}
dict_series = pd.Series(data_dict)
print("使用字典 {'苹果': 5, '香蕉': 10, '橙子': 8} 创建的Series:")
print(dict_series)
print()

print("第2部分：Series的基本属性")
print("----------------------")

print("我们来看看刚才创建的Series有哪些基本属性:")

print("2.1 查看Series的索引")
print("使用 .index 属性查看索引:")
print(dict_series.index)
print()

print("2.2 查看Series的值")
print("使用 .values 属性查看值:")
print(dict_series.values)
print()

print("2.3 查看Series的数据类型")
print("使用 .dtype 属性查看数据类型:")
print(dict_series.dtype)
print()

print("2.4 查看Series的长度")
print("使用 .size 属性查看Series包含多少个元素:")
print(dict_series.size)
print()

print("第3部分：访问Series中的数据")
print("------------------------")

print("3.1 通过位置访问数据")
print("使用索引号访问第一个元素:", dict_series[0])
print("使用切片访问前两个元素:")
print(dict_series[:2])
print()
"""
访问单个元素 vs 访问一个集合
•当你使用 dict_series[0]，你的目的是获取Series里一个具体的值。
    Pandas直接返回这个值本身（标量），所以 print就简单地把它打印出来。
•当你使用切片 dict_series[:2]，你的目的是获取Series的一个子集。
    Pandas会创建一个新的Series来存放这些数据，并保持其索引标签和数据类型信息。
    打印一个Series对象时，Pandas会将其格式化，让数据看起来更整齐（包含索引、值，并在最后注明dtype）
"""

print("3.2 通过标签访问数据")
print("使用标签名访问'苹果'的数量:", dict_series['苹果'])
print("访问多个标签的数据:")
print(dict_series[['苹果', '橙子']])
print()



print("第4部分：修改Series中的数据")
print("------------------------")

print("4.1 修改特定位置的数据")
print("修改前的Series:")
print(dict_series)
print()

dict_series['苹果'] = 7
print("将'苹果'的数量修改为7后:")
print(dict_series)
print()

print("第5部分：认识DataFrame")
print("-------------------")

print("DataFrame是Pandas中最重要的数据结构，它是一个表格型的数据结构，")
print("包含一组有序的列，每列可以是不同的值类型（数值、字符串、布尔值等）。")
print("可以把它想象成一个Excel表格或者SQL表。\\n")

# 创建DataFrame
print("5.1 创建DataFrame")
print("方法1：从字典创建DataFrame")

data = {
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 35],
    '城市': ['北京', '上海', '广州']
}

df = pd.DataFrame(data)
print("使用字典创建的DataFrame:")
print(df)
print()

print("方法2：指定列的顺序")
df_ordered = pd.DataFrame(data, columns=['姓名', '城市', '年龄'])
print("指定列顺序后的DataFrame:")
print(df_ordered)
print()

print("第6部分：DataFrame的基本操作")
print("--------------------------")

print("6.1 查看DataFrame的信息")
print("使用 .shape 查看形状(行数, 列数):")
print(df.shape)
print()

print("使用 .columns 查看列名:")
print(df.columns)
print()

print("使用 .dtypes 查看各列的数据类型:")
print(df.dtypes)
print()

print("6.2 访问DataFrame中的数据")
print("访问'姓名'列:")
print(df['姓名'])
print()

print("访问多列数据:")
print(df[['姓名', '年龄']])
print()

print("使用 .loc 通过标签访问行:")
print("访问第一行数据:")
print(df.loc[0])
print()

print("访问多行数据:")
print(df.loc[0:1])
print()

print("使用 .iloc 通过位置访问行:")
print("访问第一行数据:")
print(df.iloc[0])
print()

print("访问特定单元格:")
print("第一行'姓名'列的数据:", df.loc[0, '姓名'])
print()

print("第7部分：数据的增删改")
print("------------------")

print("7.1 添加新列")
df['薪资'] = [8000, 12000, 15000]
print("添加'薪资'列后的DataFrame:")
print(df)
print()

print("7.2 修改数据")
df.loc[1, '年龄'] = 31
print("将李四的年龄修改为31岁后:")
print(df)
print()

print("第8部分：DataFrame的高级操作")
print("--------------------------")

# 创建一个更复杂的DataFrame用于演示
print("8.1 数据筛选")
employee_data = {
    '姓名': ['张三', '李四', '王五', '赵六', '钱七'],
    '年龄': [25, 30, 35, 28, 32],
    '城市': ['北京', '上海', '广州', '深圳', '杭州'],
    '部门': ['技术部', '销售部', '技术部', '人事部', '财务部'],
    '薪资': [8000, 12000, 15000, 9000, 11000]
}

employee_df = pd.DataFrame(employee_data)
print("员工信息表:")
print(employee_df)
print()

print("筛选薪资大于10000的员工:")
high_salary = employee_df[employee_df['薪资'] > 10000]
print(high_salary)
print()

print("筛选技术部的员工:")
tech_employees = employee_df[employee_df['部门'] == '技术部']
print(tech_employees)
print()

print("使用多个条件筛选（年龄大于30且薪资大于10000）:")
multi_condition = employee_df[(employee_df['年龄'] > 30) & (employee_df['薪资'] > 10000)]
print(multi_condition)
print()

print("8.2 数据排序")
print("按薪资升序排列:")
salary_asc = employee_df.sort_values('薪资')
print(salary_asc)
print()

print("按薪资降序排列:")
salary_desc = employee_df.sort_values('薪资', ascending=False)
print(salary_desc)
print()

print("按多个列排序（先按部门，再按薪资）:")
multi_sort = employee_df.sort_values(['部门', '薪资'])
print(multi_sort)
print()

print("第9部分：处理缺失数据")
print("------------------")

# 创建包含缺失数据的DataFrame
print("9.1 创建包含缺失数据的DataFrame")
nan_data = {
    '姓名': ['张三', '李四', '王五', '赵六'],
    '年龄': [25, np.nan, 35, 28],  # np.nan 表示缺失值
    '城市': ['北京', '上海', None, '深圳'],  # None 也表示缺失值
    '薪资': [8000, 12000, 15000, np.nan]
}

nan_df = pd.DataFrame(nan_data)
print("包含缺失数据的DataFrame:")
print(nan_df)
print()

print("9.2 检查缺失数据")
print("使用 .isnull() 检查缺失值:")
print(nan_df.isnull())
print()

print("统计每列缺失值数量:")
print(nan_df.isnull().sum())
print()

print("9.3 处理缺失数据")
print("删除包含缺失值的行:")
drop_nan = nan_df.dropna()
print(drop_nan)
print()

print("用特定值填充缺失值:")
fill_value = nan_df.fillna({'年龄': 30, '薪资': 10000})
print(fill_value)
print()

print("用均值填充数值型列的缺失值:")
nan_df_filled = nan_df.copy()
nan_df_filled['年龄'].fillna(nan_df_filled['年龄'].mean(), inplace=True)
print("用年龄的平均值填充缺失的年龄:")
print(nan_df_filled)
print()

print("第10部分：数据统计和分组")
print("---------------------")

print("10.1 基本统计信息")
print("员工薪资的统计信息:")
print("平均薪资:", employee_df['薪资'].mean())
print("最高薪资:", employee_df['薪资'].max())
print("最低薪资:", employee_df['薪资'].min())
print("薪资中位数:", employee_df['薪资'].median())
print("薪资标准差:", employee_df['薪资'].std())
print()

print("整个DataFrame的统计摘要:")
print(employee_df.describe())
print()

print("10.2 数据分组")
print("按部门分组并计算各部门的平均薪资:")
grouped = employee_df.groupby('部门')['薪资'].mean()
print(grouped)
print()

print("按部门分组并查看各部门员工数量:")
dept_count = employee_df.groupby('部门').size()
print(dept_count)
print()

print("多重分组（按部门和城市分组）:")
# 添加城市列以演示多重分组
employee_df_extended = employee_df.copy()
employee_df_extended['城市'] = ['北京', '上海', '广州', '深圳', '杭州']
multi_group = employee_df_extended.groupby(['部门', '城市']).size()
print(multi_group)
print()

print("第11部分：数据的导入和导出")
print("-----------------------")

print("11.1 导出数据到CSV文件")
print("将员工数据保存为CSV文件:")
# 由于我们不能实际写入文件，这里只是演示代码
print("employee_df.to_csv('employees.csv', index=False)")
print("注意：在实际使用中，取消上面一行代码的注释即可保存文件")
print()

print("11.2 从CSV文件导入数据")
print("从CSV文件读取数据:")
print("# df_from_csv = pd.read_csv('employees.csv')")
print("注意：确保文件存在才能正常读取")
print()

print("第12部分：数据合并和连接")
print("---------------------")

print("12.1 使用concat()函数合并数据")
# 创建两个DataFrame用于演示合并
df1 = pd.DataFrame({
    '姓名': ['张三', '李四'],
    '年龄': [25, 30],
    '部门': ['技术部', '销售部']
})

df2 = pd.DataFrame({
    '姓名': ['王五', '赵六'],
    '年龄': [35, 28],
    '部门': ['人事部', '财务部']
})

print("第一个DataFrame:")
print(df1)
print()

print("第二个DataFrame:")
print(df2)
print()

# 垂直合并（按行）
print("垂直合并（按行）- 使用pd.concat():")
concat_vertical = pd.concat([df1, df2], ignore_index=True)
print(concat_vertical)
print()

# 水平合并（按列）
df3 = pd.DataFrame({
    '薪资': [8000, 12000],
})

df4 = pd.DataFrame({
    '奖金': [500, 800],
})

print("用于水平合并的DataFrame:")
print("df3:")
print(df3)
print("df4:")
print(df4)
print()

print("水平合并（按列）- 使用pd.concat(axis=1):")
concat_horizontal = pd.concat([df3, df4], axis=1)
print(concat_horizontal)
print()

print("12.2 使用merge()函数连接数据")
# 创建两个有关联的DataFrame
employees = pd.DataFrame({
    '员工ID': [1, 2, 3, 4],
    '姓名': ['张三', '李四', '王五', '赵六'],
    '部门ID': [101, 102, 101, 103]
})

departments = pd.DataFrame({
    '部门ID': [101, 102, 103],
    '部门名称': ['技术部', '销售部', '人事部']
})

print("员工信息表:")
print(employees)
print()

print("部门信息表:")
print(departments)
print()

print("基于部门ID连接两个表 - 使用pd.merge():")
merged_df = pd.merge(employees, departments, on='部门ID')
print(merged_df)
print()

print("不同类型的连接:")
print("左连接 (left join):")
left_join = pd.merge(employees, departments, on='部门ID', how='left')
print(left_join)
print()

print("右连接 (right join):")
right_join = pd.merge(employees, departments, on='部门ID', how='right')
print(right_join)
print()

print("外连接 (outer join):")
outer_join = pd.merge(employees, departments, on='部门ID', how='outer')
print(outer_join)
print()

print("内连接 (inner join) - 默认:")
inner_join = pd.merge(employees, departments, on='部门ID', how='inner')
print(inner_join)
print()

print("12.3 使用join()方法")
# 基于索引的连接
left_df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}, index=['x', 'y', 'z'])

right_df = pd.DataFrame({
    'C': [7, 8, 9],
    'D': [10, 11, 12]
}, index=['x', 'y', 'z'])

print("左表:")
print(left_df)
print()

print("右表:")
print(right_df)
print()

print("使用join()方法基于索引连接:")
joined_df = left_df.join(right_df)
print(joined_df)
print()

print("恭喜！你已经完成了Pandas的入门教程！")
print("这只是一个开始，Pandas还有更多强大的功能等待你去探索，比如：")
print("- 时间序列分析")
print("- 数据透视表")
print("- 数据可视化")
print("- 高级数据清洗技术")
print()

print("继续学习这些内容，你就能成为Pandas高手了！")