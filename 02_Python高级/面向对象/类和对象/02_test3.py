# ============================================================
# 主题：类中“属性”和“方法”的类别与设计动机
# 场景：什么时候用“类属性/类方法/静态方法”，什么时候用“实例属性/实例方法”
# 设计动机（核心思想）：
#   1) 当一个数据“被所有实例共享”且“与某个具体对象无关”时 → 用类属性（绑定在类上）
#   2) 当一个数据“属于某个具体对象”且“每个对象不同”时   → 用实例属性（绑定在self上）
#   3) 当一个行为“需要访问实例数据”                     → 用实例方法（第一个参数self）
#   4) 当一个行为“只需要访问或修改类级别数据”             → 用类方法（第一个参数cls）
#   5) 当一个行为“既不访问实例也不访问类数据”             → 用静态方法（无self/cls）
# 底层逻辑（绑定）：
#   - 实例方法：由实例调用时，解释器会把该实例自动作为self传入（方法绑定到实例）
#   - 类方法：由类/实例调用时，解释器会把该类自动作为cls传入（方法绑定到类）
#   - 静态方法：不自动传self/cls，本质是“放在类命名空间里的普通函数”
#   - 属性查找顺序：实例.__dict__ → 类.__dict__ → 父类.__dict__（MRO）
# ============================================================


# ------------------------------------------------------------
# 一、类属性（class attribute）
#   定义在类体中、与self无关，所有实例共享一份。
#   设计原因：当数据对所有实例都相同（或需要统计/聚合所有实例的信息）时，避免重复存放。
# ------------------------------------------------------------

class Circle:
    # PI作为类属性，因为所有圆的π都是同一个常量：共享即可、无需拷贝到每个对象
    PI = 3.1415926

    def __init__(self, radius):
        # radius为实例属性，每个圆不一样，应该绑定到self
        self.radius = radius

    def area(self):
        # 访问类属性的推荐方式：使用类名.Circle.PI，表达“这是类级别的数据”
        print(f'此圆的面积是 {Circle.PI * self.radius * self.radius}')

    def circumference(self):
        # 也可以通过self.PI访问（会先查实例、再查类），但语义上更推荐 Circle.PI
        print(f'此圆的周长是 {2 * Circle.PI * self.radius}')


c1 = Circle(1)
c2 = Circle(2)
c1.area()              # 不同实例共享同一个PI
c2.area()
c1.circumference()
c2.circumference()

# 【易错点1】“同名遮蔽（shadowing）”：
# 如果你在实例上赋值同名属性，会“遮蔽”类属性（仅对该实例生效）。
c1.PI = 3   # 在c1实例字典上新建一个键PI，遮蔽类属性Circle.PI
print('c1实例自己的PI：', c1.PI)          # 3（实例层命中）
print('c2仍使用类的PI：', c2.PI)          # 3.1415926（类层命中）
print('类上的PI：', Circle.PI)            # 3.1415926（类层）

# 建议：不要随意在实例上创建与类属性同名的属性，以免阅读和维护成本增大


# ------------------------------------------------------------
# 二、一个典型“类属性”场景：全局统计/聚合（如银行账户总额）
#   设计原因：总额属于系统范围的聚合信息，不属于任何一个具体账户 → 类属性更合适。
# ------------------------------------------------------------

class BankAccount:
    total_amount = 0  # 所有账户的总额（类属性）

    def __init__(self, name, init_money):
        self.name = name
        self.balance = 0
        self.deposit(init_money)

    def deposit(self, amount):
        # 修改实例余额
        self.balance += amount
        # 同步修改“系统总额”（类属性），用类名指向，语义清晰
        BankAccount.total_amount += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("余额不足")
        self.balance -= amount
        BankAccount.total_amount -= amount


acc1 = BankAccount('zhangsan', 10_000)
acc1.deposit(20_000)
acc1.withdraw(5_000)
print('系统总额（acc1阶段）：', BankAccount.total_amount)

acc2 = BankAccount('lisi', 2_000)
print('系统总额（acc2加入）：', BankAccount.total_amount)

# 【易错点2】修改类属性时请用“类名.类属性”：
# 若写成 self.total_amount += amount，可能会在实例上创建一个同名实例属性，
# 导致类属性不再被修改（出现“阴差阳错的遮蔽”BUG）。


# ------------------------------------------------------------
# 三、实例属性（instance attribute）
#   属于对象本身，多在__init__里通过self.xxx定义。
#   设计原因：每个对象有独立状态（如name/age），应存在对象自己的命名空间。
# ------------------------------------------------------------

class Person:
    species = 'Homo sapiens'  # 类属性：所有人类共享的物种名"智人/人类"

    def __init__(self, name, age, gender):
        # 以下都是实例属性：每个对象不同
        self.name = name
        self.age = age
        self.gender = gender

    def say(self):
        # 实例方法访问实例属性，用self
        print(f'我叫{self.name}，今年{self.age}岁，性别{self.gender}')

person = Person('zhangsan', 18, 'male')
person.say()

# __dict__：对象或类的“属性字典”
print('实例属性字典 person.__dict__ =', person.__dict__)  # 仅包含与self绑定的属性
print('类属性字典 Person.__dict__.keys() =', list(Person.__dict__.keys()))
# 注意：Person.__dict__ 中包含类属性、方法（函数对象）以及其他元数据（如__module__、__doc__）


# ------------------------------------------------------------
# 四、实例方法（instance method）
#   第一个参数是self（解释器自动传入），需要访问“具体对象的状态”时使用。
#   设计原因：每个对象的行为依赖其自身状态，需要与self绑定。
# ------------------------------------------------------------

class Named:
    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        # self指向调用该方法的实例，因此修改的是“该实例”的name
        self.name = new_name

    def greet(self):
        print(f'Hi, I am {self.name}')

p = Named('Alice')
p.greet()               # self → p
p.change_name('Bob')    # self → p
p.greet()


# ------------------------------------------------------------
# 五、再看Circle：把“常量”放类属性 vs 放实例属性的差异
#   设计权衡：
#     - π这样的常量应为类属性（共享、不变）
#     - 若把π放在实例属性，每个对象都会有一份冗余的拷贝，不经济也不语义化
# ------------------------------------------------------------

class CircleV2:
    def __init__(self, radius):
        # 这里把pi写成实例属性“不推荐”，只是为了展示差异
        self.pi = 3.1415926
        self.radius = radius

    def area(self):
        print('area =', self.pi * self.radius * self.radius)

    def length(self):
        print('length =', 2 * self.pi * self.radius)

c = CircleV2(1)
c.length()
c.area()


# ------------------------------------------------------------
# 六、静态方法（@staticmethod）
#   定义：无self、无cls；类与实例都能调用；本质是“放在类命名空间中的普通函数”。
#   设计原因：与类概念“相关”，但计算过程不依赖实例或类状态，放类里更聚合、更语义化。
#   何时用：
#     - 工具/纯函数逻辑，既不访问实例状态也不访问类状态
#     - 与该类语义强相关，便于组织代码与发现功能
#   何时不用：
#     - 若与类关联性弱，直接写为模块级函数也可（避免过度OOP）
# ------------------------------------------------------------

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

print('Calculator.add(1, 2) =', Calculator.add(1, 2))
cal = Calculator()
print('cal.add(3, 4) =', cal.add(3, 4))   # 也能调用，但不传self/cls

# 【易错点3】静态方法里若要访问类属性/实例属性，是做不到的——那该改成类方法或实例方法。


# ------------------------------------------------------------
# 七、类方法（@classmethod）
#   定义：第一个参数是cls（解释器自动传入类对象），常用于：
#     - 访问/修改类属性
#     - 提供“备用构造器/工厂方法”（返回cls(...)）
#   设计原因：行为在“类级别”发生（如修改类的状态、基于类的策略来创建实例）
# ------------------------------------------------------------

class PersonV2:
    # 类属性：所有实例共享
    name = 'zhangsan'

    @classmethod
    def change_name(cls, name):
        # 推荐使用cls而非明确写死类名 → 便于继承时多态
        cls.name = name
        print('cls是类对象：', cls)

print('类对象：', PersonV2)
person_v2 = PersonV2()
person_v2.change_name('lisi')  # 可以由实例调用，但传入的仍是“类对象”
print('读取类属性（经由实例读取，最终查到类上）：', person_v2.name)  # lisi


# ------------------------------------------------------------
# 八、类方法的“备用构造器”模式（常用范式）
#   设计原因：根据不同“输入格式/来源”，用类方法封装实例化细节，返回cls(...)。
# ------------------------------------------------------------

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    @classmethod
    def from_csv(cls, line):
        # 允许用一行CSV文本来构造User，屏蔽解析细节
        username, email = [s.strip() for s in line.split(',')]
        return cls(username, email)

    @classmethod
    def anonymous(cls):
        # 提供一个“命名良好”的备用构造方式
        return cls('guest', 'guest@example.com')

u1 = User.from_csv('alice, alice@example.com')
u2 = User.anonymous()
print('u1:', u1.__dict__)
print('u2:', u2.__dict__)



# ============================================================
# 补充：系统讲解类方法的本质、用途与设计思想
# ============================================================

# ------------------------------------------------------------
# （一、什么是类方法（`@classmethod`）
#
# 类方法是**绑定到类（class）**而不是实例（object）的方法。
# 定义时使用装饰器 `@classmethod`，其第一个参数不是 `self`，而是 `cls`，代表**当前类本身**。
#
# ```python
# class Example:
#     @classmethod
#     def func(cls, ...):
#         ...
# ```
#
# * `self`  实例方法使用的第一个参数（指向对象本身）
# * `cls`  类方法使用的第一个参数（指向类本身）
#
# 调用方式：
#
# ```python
# Example.func(...)      # 推荐的写法
# example = Example()
# example.func(...)      # 也能这样调用，但不常见
# ```
# ------------------------------------------------------------


# ------------------------------------------------------------
# （二、类方法的作用
#
# 类方法的核心意义在于：
#
# > 让类自己能"制造"实例、或执行与类本身相关的逻辑。
#
# 主要用途有两个方向：
#
# ### 1️⃣ **备用构造器（Alternative Constructor）**
#
# 有时创建对象的过程复杂，比如数据来自：
#
# * 一行 CSV 文本；
# * 一个 JSON 字符串；
# * 一个数据库查询结果；
# * 用户输入或网络请求。
#
# 我们希望：
#
# > 把"从这些格式解析并构造对象"的逻辑封装在类里，而不是写在类外。
#
# 这时，类方法非常适合：
#
# ```python
# class User:
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#
#     @classmethod
#     def from_csv(cls, line):
#         username, email = [s.strip() for s in line.split(',')]
#         return cls(username, email)
#
#     @classmethod
#     def from_dict(cls, data):
#         return cls(data['username'], data['email'])
# ```
#
# 用法：
#
# ```python
# u1 = User.from_csv("alice, alice@example.com")
# u2 = User.from_dict({"username": "bob", "email": "bob@example.com"})
# ```
#
# 这样：
#
# * **外部调用者**只需知道有 `from_csv` 这样的入口；
# * **内部实现细节**（如何解析字符串）都被封装了。
#
# ### 2️⃣ **类级操作（Class-level Operations）**
#
# 有时类方法并不返回实例，而是提供与类整体相关的功能：
#
# ```python
# class Counter:
#     count = 0
#
#     def __init__(self):
#         Counter.count += 1
#
#     @classmethod
#     def how_many(cls):
#         return cls.count
#
# print(Counter.how_many())  # 输出 0
# a = Counter()
# b = Counter()
# print(Counter.how_many())  # 输出 2
# ```
#
# 这种情况，类方法像是"类的工具函数"。
# ------------------------------------------------------------


# ------------------------------------------------------------
# （三、类方法 vs 静态方法 vs 实例方法
#
# | 特性    | 实例方法 (`self`) | 类方法 (`cls`) | 静态方法 (`@staticmethod`) |
# | ----- | ------------- | ----------- | ---------------------- |
# | 绑定对象  | 绑定实例          | 绑定类         | 不绑定任何对象                |
# | 第一个参数 | `self`        | `cls`       | 无                      |
# | 可访问属性 | 实例属性、类属性      | 类属性         | 只能访问显式传入的参数            |
# | 典型用途  | 操作对象内部状态      | 构造对象、操作类状态  | 工具函数、算法计算              |
#
# 例子对比：
#
# ```python
# class Demo:
#     name = "DemoClass"
#
#     def instance_method(self):
#         print("实例方法:", self)
#
#     @classmethod
#     def class_method(cls):
#         print("类方法:", cls.name)
#
#     @staticmethod
#     def static_method():
#         print("静态方法: 不关心类或实例")
# ```
# ------------------------------------------------------------


# ------------------------------------------------------------
# （四、总结类方法的"备用构造器"模式
#
# | 设计目标             | 实现方式                                       | 好处             |
# | ---------------- | ------------------------------------------ | -------------- |
# | 为不同输入来源提供不同的构造方式 | 定义多个 `@classmethod` 返回 `cls(...)`          | 统一入口、封装细节、命名清晰 |
# | 举例               | `from_csv()`, `from_json()`, `anonymous()` | 可读性强，便于扩展      |
#
# > 一句话记住：
# > **类方法是"创建对象的第二扇门"，命名良好、职责单一、可扩展性强。**
# ------------------------------------------------------------



# ------------------------------------------------------------
# 九、属性查找顺序 & 绑定行为（底层要点）
#   - 查找顺序：实例.__dict__ → 类.__dict__ → 父类.__dict__（遵循MRO）
#   - 绑定行为：
#       a) obj.method   → 产生“绑定方法”（bound method），自动携带self=obj
#       b) Class.method → 取到“函数对象”（function）或“描述符包装”，由调用方式决定是否绑定
# ------------------------------------------------------------

class DemoBind:
    def f(self):
        return 'instance method called'

print('绑定方法：', DemoBind().f)       # <bound method ...>（已经绑定self=DemoBind()）
print('函数对象：', DemoBind.f)         # <function DemoBind.f at ...>（未绑定，需要手动传实例）
# print(DemoBind.f())  # TypeError：缺少self
print(DemoBind.f(DemoBind()))            # 手动传入self，等价于 DemoBind().f()


# ------------------------------------------------------------
# 十、可变类型类属性的“坑”（重要！）
#   设计原因：类属性被所有实例共享。若它是可变对象（如list/dict），一个实例改了，所有实例都“看见”改变。
#   规范：若想“每个实例一份独立的容器”，请在__init__里用self.xxx = [] 定义为实例属性。
# ------------------------------------------------------------

class BagBad:
    items = []  # 类属性（共享）——危险：所有实例共享这一个列表！

    def add(self, item):
        BagBad.items.append(item)

b1 = BagBad()
b2 = BagBad()
b1.add('apple')
print('b2也看到apple：', b2.items)  # ['apple']

class BagGood:
    def __init__(self):
        self.items = []  # 实例属性（独立）

    def add(self, item):
        self.items.append(item)

g1 = BagGood()
g2 = BagGood()
g1.add('apple')
print('g2不受影响：', g2.items)     # []


# ------------------------------------------------------------
# 十一、小结与规范（讲义式要点）
#   1) 数据属于所有实例且相同 → 类属性；属于具体对象且不同 → 实例属性
#   2) 需要访问/修改实例状态 → 实例方法（self）
#      需要访问/修改类状态   → 类方法（cls）
#      既不访问实例也不访问类 → 静态方法（组织相关工具函数）
#   3) 修改类属性请用"类名.属性"或在类方法里用"cls.属性"，避免在实例上意外遮蔽
#   4) 可变类属性（list/dict/set）谨慎使用，常见Bug源头之一
#   5) 备用构造器优先用@classmethod实现，便于继承与多态
# ------------------------------------------------------------


