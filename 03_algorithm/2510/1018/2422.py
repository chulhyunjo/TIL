from itertools import combinations

N, M = map(int, input().split())

l = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    l[a][b] = 1
    l[b][a] = 1

result = 0
flavors = range(1, N+1)

for flavor_set in combinations(flavors, 3):
    i, j, k = flavor_set
    if l[i][j] == 0 and l[j][k] == 0 and l[i][k] == 0 : result += 1

print(result)