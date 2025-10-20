N, K = map(int, input().split())

g = [[0] * 6 for i in range(2)]

for i in range(N):
    s, y = map(int, input().split())
    g[s][y-1] += 1

result = 0
for i in range(2):
    for j in range(6):
        if g[i][j] > 0:
            result += g[i][j] // K
            if g[i][j] % K != 0: result += 1
print(result)