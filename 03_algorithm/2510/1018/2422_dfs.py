def dfs(current):
    global count

    if len(temp_combination) == 3:
        i, j, k = temp_combination
        if l[i][j] == 0 and l[j][k] == 0 and l[i][k] == 0:
            count += 1

    else:
        for i in range(current, N + 1):
            temp_combination.append(i)

            dfs(i + 1)

            temp_combination.pop()

N, M = map(int, input().split())

l = [[False] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    l[a][b] = True
    l[b][a] = True

temp_combination = []
count = 0

dfs(1)

print(count)