n = int(input())
arr= list(map(int, input().split()))

s = 0
e = n-1
result = 200000001
while s < e:
    if abs(arr[s] + arr[e]) <= result:
        result = abs(arr[s] + arr[e])
        result_s = s
        result_e = e

    if arr[s] + arr[e] < 0:
        s += 1
    else:
        e -= 1

print(arr[result_s] + arr[result_e])
