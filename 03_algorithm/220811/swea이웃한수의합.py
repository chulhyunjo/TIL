for tc in range(1,int(input())+1):
    n = int(input())
    arr = list(map(int,input().split()))

    maxV = int(-1e13)
    minV = int(1e13) # 10^13
    for i in range(n-1):
        sum1 = arr[i] + arr[i+1]
        maxV = sum1 if maxV < sum1 else maxV
        minV = sum1 if minV > sum1 else minV

    print(f'#{tc} {maxV} {minV}')
