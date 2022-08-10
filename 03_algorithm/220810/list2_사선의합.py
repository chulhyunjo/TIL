n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

s = [0] * (2*n-1)
for i in range(n):
    for j in range(n):
        s[i+j] += arr[i][j]

print(s)