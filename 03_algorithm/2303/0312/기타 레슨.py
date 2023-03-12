n, m = map(int,input().split())
numbers = list(map(int,input().split()))

s = max(numbers)
e = sum(numbers)

while s <= e:
    mid = (s+e) // 2
    sum = 0
    count = 0
    for i in range(n):
        if sum + numbers[i] > mid:
            count += 1
            sum = 0
        sum += numbers[i]

    if sum != 0:
        count += 1

    if count > m:
        s = mid + 1
    else:
        e = mid - 1

print(s)