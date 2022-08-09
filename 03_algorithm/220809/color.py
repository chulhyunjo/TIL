for tc in range(1, int(input())+1):
    n = int(input())
    area = [[0] * 10 for _ in range(10)]
    cnt = 0
    for _ in range(n):
        x1, y1, x2, y2, c = list(map(int, input().split()))
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if area[i][j] != c:
                    area[i][j] += c
                if area[i][j] == 3:
                    cnt += 1
    print(f'#{tc} {cnt}')