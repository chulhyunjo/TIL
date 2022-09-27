def eratos(num):
    arr = [True] * (num+1)
    arr[0] = arr[1] = False

    for i in range(2, int(num**0.5)+1):
        if arr[i] == True:
            for j in range(2*i, num+1, i):
                arr[j] = False
    return [k for k in range(num+1) if arr[k] == True]


def sum_cow(i, s):
    if i == m:
        if s in prime_num:
            result.add(s)
    else:
        for j in range(n):
            if not used[j]:
                used[j] = 1
                sum_cow(i+1, s+cow[j])
                used[j] = 0


n, m = map(int,input().split())
cow = list(map(int,input().split()))
prime_num = eratos(9000)
result = set()
used = [0]*n
sum_cow(0,0)
if result:
    print(*sorted(result))
else:
    print(-1)