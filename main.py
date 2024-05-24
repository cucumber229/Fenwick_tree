a = [5, 4, -1, 7, 10, -5, 6, 3, 0, -1, -5, 3, 14, 0, -2, 6]
print(len(a))
fenwick_tree = [0] * len(a)


def f(i):
    return i & (i + 1)


def g(i):
    return i | (i + 1)


for i in range(len(a)):
    fenwick_tree[i] = sum(a[f(i):i + 1])  # заполняем дерево, показываем на каких отрезках считаем суммы

print(fenwick_tree)


def psum(end):
    s = 0
    index = end - 1
    while index >= 0:
        s += fenwick_tree[index]
        index = f(index) - 1
    return s

def sum_range(start, end):
    return psum(end) - psum(start)


def update(index, elem):
    delta = elem - a[index]
    while index <= len(fenwick_tree):
        fenwick_tree[index] += delta
        index = g(index)
