from functools import reduce
def normalize(name):
# return name[0].upper() + name[1:].lower()
    return name.capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def str2float(s):
    str = s.split(".")
    head = reduce(lambda x, y: x * 10 + y, map(int, str[0]))
    tail = reduce(lambda x, y: x * 10 + y, map(int, str[1]))
    return head + tail / (10 ** len(str[1]))

print('str2float(\'123.456\') =', str2float('123.456'))


def prod(L):
    return reduce(lambda x, y: x * y, map(int, L))


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


def is_plaindrome(n):
    return str(n) == str(n)[::-1]

output = filter(is_plaindrome, range(1, 1000))
print(list(output))
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


def by_score(t):
    return t[1]


L2 = sorted(L, key=by_name)
print(L2)
L2 = sorted(L, key=by_score)
print(L2)
