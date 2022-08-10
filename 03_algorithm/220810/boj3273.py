n = int(input())
arr = sorted(list(map(int, input().split())))
target = int(input())

cnt = 0
i = 0
j = n-1
while True:
    if i == j:
        break
    if arr[i] + arr[j] < target:
        i += 1
    elif arr[i] + arr[j] > target:
        j -= 1
    else:
        cnt += 1
        i += 1

print(cnt)