n, m = map(int, input().split())
array = [[0] * m for _ in range(n)]
cnt = 1

for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            array[i][j] = cnt
            cnt += 1
    else:
        for j in range(m-1,-1,-1):
            array[i][j] = cnt
            cnt += 1

for i in array:
    print(*i)