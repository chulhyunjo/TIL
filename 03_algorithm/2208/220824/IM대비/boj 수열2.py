n, k = map(int,input().split())
arr = list(map(int,input().split()))

first_arr = sum(arr[:k])
result = first_arr
for i in range(n-k):
    first_arr += arr[i+k] - arr[i]
    result = max(first_arr, result)

print(result)