import sys
input = sys.stdin.readline
m, n = map(int, input().split())
arr = list(map(int, input().split()))

s = 1
e = max(arr)
result = 0
while s <= e:
    total = 0
    mid = (s+e) // 2
    if mid == 0:
        result = 0
        break

    for i in arr:
        total += (i // mid)

    if total >= m:
        s = mid + 1
        result = mid
    else:
        e = mid-1

print(result)