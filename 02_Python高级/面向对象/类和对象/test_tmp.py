def give_yasuiqian(money):
    def child_buy(obj, m):
        nonlocal money
        if money > m:
            money -= m
            print('买', obj, '花了', m, '元, 剩余', money, '元')
        else:
            print("买", obj, '失败')
    return child_buy
cb = give_yasuiqian(1000)
cb('变形金刚', 200)
cb('漫画三国', 100)
cb('手机', 1300)