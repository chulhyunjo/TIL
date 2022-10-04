def population(x, y, d1, d2):
    po = [0] * 5
    # 1번
    for i in range(1, x+d1):
        for j in range(1, y+1):
            if array[i][j] == 5: break
            else: po[0] += graph[i][j]
    # 2번
    for i in range(1, x+d2+1):
        for j in range(n, y, -1):
            if array[i][j] == 5: break
            else: po[1] += graph[i][j]
    # 3번
    for i in range(x+d1, n+1):
        for j in range(1,y-d1+d2):
            if array[i][j] == 5: break
            else: po[2] += graph[i][j]
    # 4번
    for i in range(x+d2+1, n+1):
        for j in range(n, y-d1+d2-1, -1):
            if array[i][j] == 5: break
            else: po[3] += graph[i][j]
    return po

def dividLand5(x, y, d1, d2):
    for i in range(d1 + 1):
        array[x + i][y - i] = 5
    for i in range(d2 + 1):
        array[x + i][y + i] = 5
    for i in range(d2 + 1):
        array[x + d1 + i][y - d1 + i] = 5
    for i in range(d1 + 1):
        array[x + d2 + i][y + d2 - i] = 5

n = int(input())
graph = [[0]*n] + [[0] + list(map(int,input().split())) for _ in range(n)]
total = 0   # 전체 인원
for i in range(1, n+1):
    for j in range(1, n+1):
        total += graph[i][j]

if n % 2:
    b = n//2 +1
else:
    b = n//2
result = int(1e10)
for x in range(1, n+1):
    for y in range(1, n+1):
        for d1 in range(1, b):
            for d2 in range(1, b):
                if x+d1+d2 >n or y -d1 < 1 or y+d2 > n: continue
                array = [[0] * (n+1) for _ in range(n+1)]
                dividLand5(x,y,d1,d2)
                people = population(x,y,d1,d2)
                people[4] = total - sum(people)
                result = min(result, max(people)-min(people))

print(result)