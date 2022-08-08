n = int(input())
arr = list(map(int, input().split()))

for i in range(n-1, 0, -1):
    for j in range(0,i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)