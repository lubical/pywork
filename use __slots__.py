# use __slots__
# python类允许动态绑定类，即运行时绑定。
from types import MethodType


class Student(object):
    pass


s = Student()
s.name = 'Michael'
print(s.name)


def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

s2 = Student()
# s2.set_age(25)
# 类绑定分为两种 实例绑定，类绑定，
# 前者只有绑定实例能用相应函数，后者对于所有实例均有效


def set_score(self, score):
    self.score = score


Student.set_score = set_score
s.set_score(100)
print(s.score)
s2.set_score(99)
print(s2.score)

# slots能限制类里只能有某些特定的属性。


class Student(object):
    __slots__ = ('name', 'age')


s = Student()
s.name = 'Michael'
s.age = 25
# s.score = 100
