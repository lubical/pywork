from abstest import my_abs
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))

print('my_abs(10)', my_abs(10))
print('my_abs(-10)', my_abs(10))


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc())
print(calc(1, 2, 3, 4))


def add_end(L=[]):
    L.append('END')
    return L

print(add_end())
print(add_end())


def add_end1(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end1())
print(add_end1())


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

print(f1(1, 2))
print(f1(1, 2, c=3))
print(f1(1, 2, 3, 'a', 'b'))
print(f1(1, 2, 3, 'a', 'b', x=99))
print(f2(1, 2, d=99, ext=None))
args = (1, 2, 3, 4)
print(args)
kw = {'d': 99, 'x': '#'}
print(kw)
print(f1(*args, **kw))
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
print(f2(*args, **kw))

# Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

# 要注意定义可变参数和关键字参数的语法：

# *args是可变参数，args接收的是一个tuple；

# **kw是关键字参数，kw接收的是一个dict。

# 以及调用函数时如何传入可变参数和关键字参数的语法：

# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
