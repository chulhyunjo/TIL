def dfs(i):
    global answer
    global sum1
    if sum1 > answer:
        return

    if i == n:
        if sum1 < answer:
            answer = sum1

    for j in range(n):
        if not visited[j]:
            visited[j] = True
            sum1 += arr[i][j]
            dfs(i+1)
            visited[j] = False
            sum1 -= arr[i][j]


for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    visited = [False] * n
    answer = 1000
    sum1 = 0
    dfs(0)
    print(f'#{tc} {answer}')