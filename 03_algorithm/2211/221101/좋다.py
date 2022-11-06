n = int(input())
arr = list(map(int,input().split()))
arr.sort()
result = 0

for i in range(n):
    start = 0
    end = n-1
    sum1 = arr[start] + arr[end]
    while start < end:
        if start == i:
            sum1 -= arr[start]
            start += 1
            sum1 += arr[start]
            continue

        if end == i:
            sum1 -= arr[end]
            end -= 1
            sum1 += arr[end]
            continue
        if sum1 < arr[i]:
            sum1 -= arr[start]
            start += 1
            sum1 += arr[start]
        elif sum1 > arr[i]:
            sum1 -= arr[end]
            end -= 1
            sum1 += arr[end]
        else:
            result += 1
            break

print(result)