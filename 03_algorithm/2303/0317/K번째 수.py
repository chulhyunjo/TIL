n = int(input())
k = int(input())

s=1
e=k
result = 0
while s<=e:
    mid = (s+e)//2
    cnt = 0
    for i in range(1,n+1):
        if mid // i > n:
            cnt += n
        else:
            cnt += mid//i
    if cnt >= k:
        e = mid-1
        result = mid
    else:
        s = mid+1

print(result)