n = int(input())
arr = [[0] * 1001 for _ in range(1001)]
cnt = [0] * (n+1)
for q in range(1,n+1):
    x1, y1, w, h = map(int,input().split())
    for i in range(y1,y1+h):
        arr[i][x1:x1+w] = [q] * w
for i in range(0, n):
    for j in range(1001):
        cnt[i+1] += arr[j].count(i+1)
print(*cnt[1:], sep='\n')