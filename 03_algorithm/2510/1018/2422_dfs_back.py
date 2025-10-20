def dfs(current, depth):
    global count

    if depth == 3:
        i, j, k = temp_combination
        if l[i][j] == 0 and l[j][k] == 0 and l[i][k] == 0:
            count += 1
        return

    for i in range(current, N + 1):
        if depth == 1:
            now = temp_combination[0]
            if l[now][i] == 1: continue

        temp_combination.append(i)

        dfs(i + 1, depth+1)

        temp_combination.pop()

N, M = map(int, input().split())

l = [[False] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    l[a][b] = True
    l[b][a] = True

temp_combination = []
count = 0

dfs(1, 0)

print(count)