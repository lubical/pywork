class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object(name=%s)'% self.name
    __repr__ = __str__

s = Student('Michael')
print(s)

class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b,self.a + self.b
        if self.a > 100:
           raise StopIteration();
        return self.a
    def __getItem__(self,n):
      if isinstance(n,int):
        a,b = 1,1
        for x in range(n):
           a,b = b,a+b
        return a
      elif isinstance(n,slice):
         start = n.start
         stop = n.stop
         step = n.step
         if start is None:
            start = 0
         if step is None:
            step = 1
         a,b = 1,1
         L = []
         for x in range(stop):
            if x >= start and x % step ==0:
               L.append(a)
            a,b = b,a+b
         return L

for n in Fib():
    print(n)
f = Fib() 
print(list(f[0:15]))
print(list(f[0:15:2]))
print(list(f[0:15:3]))
