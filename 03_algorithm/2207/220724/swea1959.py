for tc in range(int(input())):
    n, m = map(int, input().split())
    ai = list(map(int, input().split()))
    bj = list(map(int, input().split()))
    result = 0
    if n > m:
        n, m = m, n

    for i in range(m-n+1):
        summ = 0
        for j in range(n):
            if len(ai) < len(bj):
                summ += ai[j] * bj[i + j]
            else:
                summ += bj[j] * ai[i+j]

        if summ > result:
            result = summ
    print(f'#{tc+1} {result}')