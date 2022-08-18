n, k = map(int,input().split())
arr = list(map(int,input().split()))
result = sum(arr[0:k])
sub = []
result1 = result
for i in range(n-k):
    result1 -= (arr[i] - arr[i+k])
    sub.append(result1)

if k == 1:
    print(max(arr))
else:
    if sub:
        print(max(max(sub),result))
    else:
        print(result)
