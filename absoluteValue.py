a = 100
if a >= 0:
    print(a)
else:
    print(-a)

print('''xioming
oxo
bsdf''')
print("10/3=", 10/3)
print("10//3=", 10//3)
n = 123
print(n)
f = 456.789
print(f)
s1 = 'Hello, world'
print(s1)
s2 = 'Hello, \'Adam\''
print(s2)
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(s3)
print(s4)
s1 = 72
s2 = 85
r = (85 - 72) / 72 * 100
#%% 转义%
print('%.1f%%' % r)
classmates = ['Michael','Bob','Tracy']
print(classmates)
print("The first one", classmates[0])
print("The last one", classmates[-1])
classmates.append('Adam')
print("add Adam", classmates)
classmates.insert(1,'Jack')
print("insert Jack to position 1", classmates)
classmates.pop()
print("pop the last one", classmates)
classmates.pop(1)
print("pop the position 1", classmates)
L = ['Apple', 123, True]
print('different list',L)
print('length of L', len(L))
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s)
print('length of s', len(s))
classmatesCantChange = ('Michael', 'Bob', 'Tracy')
print(classmatesCantChange)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L)
print(L[0][0])
print(L[1][1])
print(L[2][2])
t = ()
print(u't=()',t)
t = (1)
print(u't=(1)',t)
t = (1,)
print(u't=(1,)',t)
