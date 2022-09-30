def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x


def union(x, y):
    rep[find_set(y)] = find_set(x)

V = int(input())
E = int(input())
edge = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edge.append([u, v, w])
edge.sort(key=lambda x: x[2])
rep = [i for i in range(V + 1)]

N = V + 1
cnt = 0
total = 0
for u, v, w in edge:
    if find_set(u) != find_set(v):
        cnt += 1
        union(u, v)
        total += w
        if cnt == N - 1:
            break
print(total)