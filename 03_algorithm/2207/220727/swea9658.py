for tc in range(1, int(input())+1):
    n = int(input())
    cnt = 0
    while n >=10:
        n /= 10
        cnt += 1
    n = round(n, 1)
    if n >= 10:
        n /= 10
        cnt += 1
        n = round(n, 1)

    print(f'#{tc} {n}*10^{cnt}')