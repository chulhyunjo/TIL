T = int(input())
for tc in range(1,T+1):
    n, m, k = map(int,input().split())
    arr = sorted(list(map(int,input().split())))
    bread = idx = time = 0
    result = 'Possible'
    while True:
        while idx < n and arr[idx] >= time and bread:
            idx += 1
            bread -= 1

        time += m
        bread += k
        if idx == n: break
        if arr[idx] < time:
            result = 'Impossible'
            break
    print(f'#{tc} {result}')