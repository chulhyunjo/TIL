for tc in range(1, int(input())+1):
    p = input().rstrip()
    q = input().rstrip()
    result = 'Y'

    if len(p) > len(q):
        p, q = q, p

    if p == q[:len(p)]:
        if p == q:
            result = 'N'
        elif (len(q) - len(p) == 1) and q[len(p)] == 'a':
            result = 'N'
        else:
            result = 'Y'

    print(f'#{tc} {result}')
