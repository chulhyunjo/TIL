for _ in range(4):
    w = [0] * 50001
    h = [0] * 50001
    x1, y1, x2, y2, p1, q1, p2, q2 = map(int,input().split())
    for i in range(x1,x2+1):
        w[i] += 1
    for j in range(y1, y2+1):
        h[j] += 1

    for i in range(p1, p2+1):
        w[i] += 1
    for j in range(q1, q2+1):
        h[j] += 1

    cntW = w.count(2)
    cntH = h.count(2)

    if cntW == 1 and cntH == 1:
        print('c')
    elif (cntW > 1 and cntH == 1) or (cntH > 1 and cntW == 1):
        print('b')
    elif cntW == 0 and cntH == 0:
        print('d')
    else:
        if (cntW and not cntH) or (cntH and not cntW):
            print('d')
        else:
            print('a')