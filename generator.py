g = (x * x for x in range(10))
for n in g:
    print(n)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib(6))


def triangles():
    L = [1, ]
    while True:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(0, len(L) - 1)] + [1]

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
