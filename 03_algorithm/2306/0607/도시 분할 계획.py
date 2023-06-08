import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

N, M = map(int, input().split())
edge = []
parent = list(range(N+1))
for _ in range(M):
    a, b, c = map(int, input().split())
    edge.append((c, a, b))

edge.sort(key = lambda x: x[0])

answer = 0
lastCost = 0
for cost, a, b in edge:
    parentA = find(a)
    parentB = find(b)
    if parentA != parentB:
        union(parentA,parentB)
        answer += cost
        lastCost = cost
print(answer - lastCost)