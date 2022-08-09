T = int(input())
for tc in range(1, T+1):
    n = int(input())
    numbers = list(map(int, input().split()))
    minV = 1000001
    maxV = 0

    for num in numbers:
        if num < minV:
            minV = num
        if num > maxV:
            maxV = num

    result = maxV - minV
    print(f'#{tc} {result}')