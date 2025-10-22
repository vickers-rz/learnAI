class BankAccount:
    total_amount = 0  # 类属性

    def __init__(self, name, init_money):
        self.name = name
        BankAccount.total_amount += init_money
        # self.total_amount += init_money  # ❌ 错误：创建了一个实例属性 total_amount

# 创建两个账户
a1 = BankAccount("Alice", 100)
print("a1.total_amount:", a1.total_amount)
print("BankAccount.total_amount:", BankAccount.total_amount)

a2 = BankAccount("Bob", 200)
print("a2.total_amount:", a2.total_amount)
print("BankAccount.total_amount:", BankAccount.total_amount)
a2.total_amount = 999   # 在实例上新建一个同名属性！
print("a2.total_amount:", a2.total_amount)
print("BankAccount.total_amount:", BankAccount.total_amount)


