for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    result = 0
    for i in range(n):
        for j in range(n):
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    result += abs(arr[i][j] - arr[nx][ny])
    print(f'#{tc} {result}')