import sys
input = sys.stdin.readline

N, M = map(int,input().split())
parents = list(range(N+1))
edge = []

for _ in range(M):
    a, b, c = map(int,input().split())
    edge.append((c, a, b))
edge.sort(key = lambda x: x[0])

def find(x):
    if x == parents[x]:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parents[y] = x
        return True
    return False

cnt = 0
result = 0
if N == 2:
    print(0)
else:
    for c, a, b in edge:
        if union(a, b):
            result += c
            cnt += 1
            if cnt >= N-2:
                break
    print(result)