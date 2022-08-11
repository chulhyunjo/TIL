import sys
input = sys.stdin.readline
n, c = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()
s = 0
e = n-1
result = 0
while s < e:
    mid = (s+e)//2
    if (arr[mid] - arr[s]) < (arr[e] - arr[mid]):
        e -= 1