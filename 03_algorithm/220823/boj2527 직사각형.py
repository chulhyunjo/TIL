for _ in range(4):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int,input().split())
    w = [0] * 50001
    h = [0] * 50001

    for i in range(x1, x2+1):
        w[i] += 1

    for i in range(y1, y2+1):
        h[i] += 1

    for i in range(x3, x4+1):
        w[i] += 1

    for i in range(y3, y4+1):
        h[i] += 1

    checkw = w.count(2)
    checkh = h.count(2)
    result = checkw + checkh
    if result == 0:
        if x1 > x3 and x2 < x4 and y1 > y3 and y2 < y4:
            print('a')
        elif x3 > x1 and x4 < x2 and y3 > y1 and y4 < y2:
            print('a')
        else:
            print('d')

    elif result == 2:
        print('c')

    elif (checkw == 1 and checkh) or (checkh == 1 and checkw):
        print('b')
    else:
        if (not checkw and checkh) or (not checkh and checkw):
            print('d')
        else:
            print('a')