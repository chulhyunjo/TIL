for tc in range(1, int(input()) + 1):
    n = int(input())
    area = [[0] * 10 for _ in range(10)]
    for _ in range(n):
        x1, y1, x2, y2, c = list(map(int, input().split()))
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if area[i][j] != c:
                    area[i][j] += c

    dx = [0, 0, 1, -1]
    dy = [1, 1, 0, 0]
    result = 0
    for i in range(10):
        for j in range(10):
            cnt = 0
            if area[i][j] == 1:
                for m in range(4):
                    nx = i + dx[m]
                    ny = j + dy[m]
                    if 0 <= nx < 10 and 0 <= ny < 10:
                        if area[nx][ny] == 1:
                            cnt += 1
                result += (4 - cnt)
            if area[i][j] == 2:
                for m in range(4):
                    nx = i + dx[m]
                    ny = j + dy[m]
                    if 0 <= nx < 10 and 0 <= ny < 10:
                        if area[nx][ny] == 2:
                            cnt += 1
                result += (4 - cnt)
    print(f'#{tc} {result}')
