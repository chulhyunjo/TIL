n, d = map(int, input().split())
count = [0] * 10

for i in range(1, n+1):
    now = str(i)
    for j in now:
        count[int(j)] += 1

print(count[d])