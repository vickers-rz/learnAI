"""
Collatz猜想（3n+1猜）规则如下：
从任意正整数 n开始，如果 n 是偶数，则下一个数是 n / 2；
如果 n是奇数，则下一个数是（3*n+1。
无论从哪个正整数开始，按此规则迭代，最终都会得到1。
编写一个 Python 脚本，接收用户输入的一个正整数n，
使用 while 循环打印出从 n开始到1的 Collatz序列，并计算序列的长度（步数）。
"""
n = int(input("请输入一个正整数："))
steps = 0
print(f"n的初始值为{n}")
while n != 1:
    if n % 2 == 0:
        n = n / 2
        print(n)
    else:
        n = 3 * n + 1
        print(n)
    steps += 1
print(f"Collatz 序列的长度是 {steps + 1} 步.")