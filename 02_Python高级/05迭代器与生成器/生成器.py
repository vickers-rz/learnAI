# # 定义生成器函数
# def count_up_to(max):
#     count = 1
#     while count <= max:
#         yield count
#         count += 1
#         # return count
#
# res = count_up_to(5)
# # print(res)
#
# # 使用生成器函数
# for number in res:
#     print(number)
#
# for num in res:
#     print(num)



# my_list = [1, 2, 3, 4, 5]
# mylist_iterator = my_list.__iter__()
# for i in mylist_iterator:
#     print(i)
#
# for i in mylist_iterator:
#     print(i)








# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# # 打印前10个斐波那契数
# fib = fibonacci()
# for _ in fib:
#     print(_)



# ls = list(range(10000000001))
# for i in ls:
#     print(i)



def make_num():
    start = 1
    while True:
        yield start
        start += 1

num_gen = make_num()
for i in num_gen:
    print(i)




