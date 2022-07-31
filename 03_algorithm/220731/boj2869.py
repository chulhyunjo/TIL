for _ in range(int(input())):
    vps = input()

    open = 0
    for i in range(len(vps)):
        if vps[i] == '(':
            open += 1
        else:
            if open > 0:
                open -= 1

            else:
                open = -999

    if open == 0:
        print('YES')
    else:
        print('NO')