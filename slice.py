from collections import Iterable
import os
L = list(range(100))
print(L)
print(L[:10])
print(L[-10:])
print(L[:10:2])
print(L[::5])
print(L[:10])
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)


print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in[(1, 1), (2, 4), (3, 9)]:
    print(x, y)

print([d for d in os.listdir('.')])
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print(d)
for k, v in d.items():
    print(k, '=', v)

L = ['Hello', 'World', 'IBM', 'Apple']
print(L)
print([s.lower() for s in L if isinstance(s, str)])

print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
