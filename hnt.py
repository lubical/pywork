# 汉诺塔 n个盘子从a借助b到c
# n-1个盘子从a借助c到b
# 第n个盘子移到c
# n-1 个盘子从b借助a移动到c
# 递归边界 一个盘子直接移动


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(3, 'A', 'B', 'C')
# move(4, 'A', 'B', 'C')
