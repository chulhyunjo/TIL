def eratos(num):
    arr = [True] * (num+1)
    arr[0] = arr[1] = False

    for i in range(2, int(num**0.5)+1):
        if arr[i] == True:
            for j in range(2*i, num+1, i):
                arr[j] = False
    return [k for k in range(num+1) if arr[k] == True]


def sum_cow(i, j, s):
    if j == m:
        if s in prime_num:
            result.add(s)
    elif i < n:
        sum_cow(i+1, j+1 ,s+cow[i])
        sum_cow(i+1, j, s)


n, m = map(int,input().split())
cow = list(map(int,input().split()))
prime_num = eratos(sum(cow))
result = set()
sum_cow(0,0,0)
if result:
    print(*sorted(result))
else:
    print(-1)