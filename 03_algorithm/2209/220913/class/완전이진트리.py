def pre(n):
    if n <= size:
        print(tree[n])
        pre(2*n)
        pre(2*n + 1)

tree = [0, 'A', 'B', 'C', 'D', 'E', 'F']
size = len(tree) - 1
pre(1)