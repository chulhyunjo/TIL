N, L = map(int,input().split())
arr = list(map(int,input().split()))
start = N-1
minL = [0] * N
minV = min(arr[N-L:N])
minL[start] = minV

for i in range(N-1):
    if start-i >=0 and arr[start-i] == minV:
        if start-i-L >=0:
            minV = min(arr[start-i-L:start-i])
        else:
            minV = min(arr[:start-i])
    elif start-i-L>=0 and arr[start-i-L] < minV:
        minV = arr[start-i-L]

    minL[start-i-1] = minV
print(*minL)