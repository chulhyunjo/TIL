a, k = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
num1 = 0
num2 = 0

for i in range(a-1, -1, -1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            cnt += 1
            arr[j], arr[j+1] = arr[j+1], arr[j]
            if cnt == k:
                num1 = arr[j]
                num2 = arr[j + 1]


if cnt < k:
    print(-1)
else:
    print(num1, num2)