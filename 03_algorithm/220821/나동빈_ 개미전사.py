n = int(input())
arr = list(map(int,input().split()))

for i in range(2,n):
    arr[i] = max(arr[i-1], arr[i] + arr[i-2])

print(arr)