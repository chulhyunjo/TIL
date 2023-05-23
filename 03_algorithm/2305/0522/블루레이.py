n, m = map(int,input().split())
course = list(map(int,input().split()))
s = 0
e = 0
for i in course:
    if s<i:
        s = i
    e += i

while e>=s:
    middle = (s+e)//2

    cnt = 0
    sum1 = 0
    for i in range(n):
        if sum1 + course[i] > middle:
            sum1 = 0
            cnt += 1
        sum1 += course[i]

    if sum1 != 0:
        cnt += 1
    if cnt > m:
        s = middle + 1
    else:
        e = middle - 1

print(s)