import numpy as np
def shape_test():
    array_one = np.array([[1,2,3],[4,5,6]])
    print('array_one 原数组维度：',array_one.shape)
    print('array_one 原数组内容：',array_one)
    array_one.shape = (3,2)
    print('array_one 转变数组维度大小之后的数组维度：',array_one.shape)
    print('array_one 转变数组维度大小之后的数组内容：',array_one)

shape_test()