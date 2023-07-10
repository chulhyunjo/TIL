import sys
input = sys.stdin.readline

def find(x):
    if x == parents[x]:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x > y:
        x, y = y, x
    if x != y:
        parents[y] = x
        return True
    return False
while True:
    m, n = map(int,input().split())
    if not m and not n:
        break
    edges = []
    parents = [i for i in range(m)]
    sum1 = 0
    for _ in range(n):
        x, y, z = map(int,input().split())
        edges.append((z,x,y))
        sum1 += z
    edges.sort()

    cnt = 0
    for edge in edges:
        z, x, y = edge
        if union(x, y):
            cnt += 1
            sum1 -= z
        if cnt == n-1:
            break
    print(sum1)

