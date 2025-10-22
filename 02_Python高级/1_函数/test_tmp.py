def test3(x, y, m, n):
    print(x, y, m, n)

kwargs = {'a': 1, 'b': 2}
test3(*[kwargs['a'], kwargs['b']], m=3, n=4)

print(kwargs.get('c', '不存在'))




