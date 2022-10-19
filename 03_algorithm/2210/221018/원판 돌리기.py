def check():
    global total, num
    remove = set()
    for i in range(1,n+1):
        for j in range(m):
            p = (point[i]+j)%m
            if arr[i][p] == -1: continue
            flag = 0
            if i < n and arr[i][p] == arr[i+1][(point[i+1]+j)%m]:
                flag = 1
                remove.add((i+1,(point[i+1]+j)%m))
            if arr[i][p] == arr[i][(p+1)%m]:
                flag = 1
                remove.add((i,(p+1)%m))
            if arr[i][p] == arr[i][p-1 if p-1>=0 else m-1]:
                q = p-1 if p-1>=0 else m-1
                flag = 1
                remove.add((i,q))
            if flag : remove.add((i,p))
    for x,y in remove:
        total -= arr[x][y]
        arr[x][y] = -1
        num -=1


n, m, t = map(int,input().split())
arr = [[-1]*m]
point = [0]*(n+1)
total = 0
num = n*m
for _ in range(n):
    line = (list(map(int,input().split())))
    for i in line:
        total += i
    arr.append(line)
arr += [[-1]*m]
for _ in range(t):
    x, d, k = map(int,input().split())
    if d == 1:
        for idx in range(x, n+1, x):
            point[idx] = (point[idx] + k) % m
    else:
        for idx in range(x, n+1, x):
            point[idx] = (point[idx] + (m-k)) % m
    tmp = total
    check()
    if total and tmp == total:
        avg = total / num
        for i in range(1,n+1):
            for j in range(m):
                if arr[i][j] == -1: continue
                else:
                    if arr[i][j] > avg:
                        arr[i][j] -= 1
                        total -=1
                    elif arr[i][j] < avg:
                        arr[i][j] += 1
                        total += 1
print(total)