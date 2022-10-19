import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def check(d,bottom, top,sum1):
    global maxV
    if d == n:
        maxV = max(sum1, maxV)
        return
    elif sum1 + (n-d)*6 < maxV:
        return
    else:
        for j in range(6):
            if dice[d][j] == top:
                check(d+1,dice[d][j], dice[d][twin.get(j)], sum1 + max([dice[d][x] for x in range(6) if x != j and x != twin.get(j)]))


twin = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}
n = int(input())
dice = []
for _ in range(n):
    dice.append(list(map(int,input().rstrip().split())))
maxV = 0
for i in range(6):
    check(1, dice[0][i], dice[0][twin.get(i)], max([dice[0][x] for x in range(6) if x != i and x != twin.get(i)]))

print(maxV)