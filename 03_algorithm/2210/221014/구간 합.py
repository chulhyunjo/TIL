for tc in range(1, int(input())+1):
    n, k = map(int,input().split())
    maxV = 0
    for i in range(n):
        line = list(map(int,input().split()))
        sum1 = 0
        if i + k >= n: end = n
        else: end = i+k
        for j in range(i,end):
            sum1 += line[j]
        maxV = sum1 if maxV < sum1 else maxV
    print(f'#{tc} {maxV}')