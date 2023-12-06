N = int(input())
dots = []

for _ in range(N):
    x, y = map(int,input().split())
    dots.append([x,y])

dots.sort(key = lambda x : (x[1], x[0]))
for x,y in dots:
    print(x, y)