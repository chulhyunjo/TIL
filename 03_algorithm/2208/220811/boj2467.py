n = int(input())
arr = list(map(int,input().split()))
l = 0
r = n - 1
result = int(1e13)
while l < r:
    if abs(arr[l] + arr[r]) < result:
        result_l = l
        result_r = r
        result = abs(arr[r] + arr[l])
    if arr[l] + arr[r] < 0:
        l += 1
    else:
        r -= 1

print(arr[result_l],arr[result_r])