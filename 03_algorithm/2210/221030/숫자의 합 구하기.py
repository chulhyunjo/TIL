n = int(input())
m = int(input())
arr = sorted(list(map(int,input().split())))

start_index = 0
end_index = n-1
result = 0

sum1 = arr[start_index] + arr[end_index]
while start_index < end_index:
    if sum1 > m:
        sum1 -= arr[end_index]
        end_index -= 1
        sum1 += arr[end_index]
    elif sum1 < m:
        sum1 -= arr[start_index]
        start_index += 1
        sum1 += arr[start_index]
    else:
        result += 1
        sum1 -= arr[start_index]
        start_index += 1
        sum1 += arr[start_index]
print(result)
