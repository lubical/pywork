# slot 确定类只能绑定的属性，对子类无效。
class Student(object):
    __slots__=('name', 'age')

s = Student()
s.name = 'Michael'
s.age = 25
print(s.name)
print(s.age)
s.score = 99
print(s.score)
