import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []

for _ in range(N):
    n = int(input())
    arr.append(n)

arr.sort()

for _ in range(M):
    find = int(input())
    s = 0
    e = N-1
    flag = -1
    while s<=e:
        mid = (s+e)//2
        if arr[mid] < find:
            s = mid + 1
        else:
            if arr[mid] == find:
                flag = mid
            e = mid - 1

    if flag == -1:
        print(-1)
    else:
        print(flag)