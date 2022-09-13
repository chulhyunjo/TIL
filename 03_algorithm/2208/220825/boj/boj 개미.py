n, m = map(int,input().split())
x, y = map(int,input().split())
k = int(input())

x1 = k-(n-x)
y1 = k-(m-y)

resultX = x1 % (2 * n)
resultY = y1 % (2 * m)

print(abs(n-resultX), abs(m-resultY))