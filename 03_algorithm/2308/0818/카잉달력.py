for _ in range(int(input())):
    M, N, x, y = map(int,input().split())

    cnt = 1
    tmpx = tmpy = 1
    if M > N:
        x, y = y, x
        M, N = N, M

    while True:
        if tmpx - tmpy == x - y:
            cnt += x - 1
            break

        if (x - tmpx) == (N+y - tmpy):
            cnt += x - tmpx
            break
        else:
            tmpy = (tmpy + M) % N
            cnt += M
        if tmpy == 1:
            cnt = -1
            break

    print(cnt)



    # 10, 12
    # 3, 9
    # 1, 11 -> 11
    # 1, 9 -> 22
    # 1, 7 ->

    # 13 11
    # 1, 3 -> 14
    # 1, 5 -> 27
    # 1, 7 -> 40
    # 1, 9 -> 53
    # 1, 11 -> 66
    # 1, 2 -> 79
    # 5, 6 -> 83

