def combination(d):
    if d == 9:
        playGame(order)
    elif d == 3:
        order[d] = 1
        combination(d+1)
    else:
        for i in range(2,10):
            if not used[i]:
                used[i] = 1
                order[d] = i
                combination(d+1)
                used[i] = 0
                order[d] = 0

def playGame(player):
    global maxV, num
    inning = 0
    score = 0
    num = 0
    for inning in hitter:
        g1, g2, g3 = 0, 0, 0
        out = 0
        while out < 3:
            if inning[player[num]-1] == 0:
                out += 1
            elif inning[player[num]-1] == 1:
                score += g3
                g1, g2, g3 = 1, g1, g2
            elif inning[player[num]-1]== 2:
                score += g2 + g3
                g1, g2, g3 = 0, 1, g1
            elif inning[player[num]-1] == 3:
                score += g1 + g2 + g3
                g1, g2, g3 = 0, 0, 1
            else:
                score += g1 + g2 + g3 + 1
                g1, g2, g3 = 0, 0, 0
            num = (num+1) % 9
    maxV = max(score, maxV)


end = int(input())
hitter = [list(map(int,input().split())) for _ in range(end)]
used = [0] * 10
order = [0] * 9
maxV = 0    # 결과
combination(0)
print(maxV)
