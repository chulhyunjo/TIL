def cross(n, bd):  # 대각선 체크
    j = 0
    while n - j > 0:
        cnt_left = 0
        cnt_right = 0
        for p in range(n):
            if p + j < n and bd[p][p + j] == 'o':  # 왼쪽에서 내려가는 대각선
                cnt_left += 1
                if cnt_left >= 5:
                    return 1
            elif p + j < n and bd[p][p + j] != 'o':  # .을 만나면 초기화
                cnt_left = 0

            if p - j >= 0 and bd[n - p - 1][p - j] == 'o':  # 오른쪽에서 내려가는 대각선
                cnt_right += 1
                if cnt_right >= 5:
                    return 1
            elif p - j >= 0 and bd[n - p - 1][p - j] != 'o':
                cnt_right = 0

        j += 1


T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    bd = [list(input()) for _ in range(n)]

    if cross(n, bd):
        print(f'#{tc} YES')
    else:
        print("NO")