import sys
sys.setrecursionlimit(10**6)
def play(j,location,location2,horse,location3,location4):
    global ans
    if j == 10:
        result = sum(horse)
        ans = max(result, ans)
    else:
        for i in range(4):
            if location[i] + dice[j] > len(board) and not location4[i]:
                location[i] += dice[j]
                location4[i] = dice[j]
            if location4[i]:
                continue
            if 0<location[i]<=20 and not board[location[i]-1]%10:
                if board[location[i]-1] == 10:
                    if location2[i] + dice[j] > len(blue1) and not location3[i]:
                        location3[i] += dice[j]
                    if location3[i]:
                        continue
                    horse[i] += blue1[location2[i]+dice[j]-1]
                    location2[i] += dice[j]
                    play(j+1, location, location2, horse,location3,location4)
                    if location3[i]:
                        horse[i] -= blue1[location2[i]-1]
                        location2[i] -= location3[i]
                        location3[i] = 0
                    else:
                        location2[i] -= dice[j]
                        horse[i] -= blue1[location2[i] + dice[j] - 1]
                elif board[location[i]-1] == 20:
                    if location2[i] + dice[j] > len(blue2) and not location3[i]:
                        location3[i] += dice[j]
                    if location3[i]:
                        continue
                    horse[i] += blue2[location2[i]+dice[j]-1]
                    location2[i] += dice[j]
                    play(j+1, location, location2, horse,location3,location4)
                    if location3[i]:
                        horse[i] -= blue2[location2[i]-1]
                        location2[i] -= location3[i]
                        location3[i] = 0
                    else:
                        horse[i] -= blue2[location2[i] + dice[j] - 1]
                        location2[i] -= dice[j]
                elif board[location[i]-1] == 30:
                    if location2[i] + dice[j] > len(blue3) and not location3[i]:
                        location3[i] += dice[j]
                    if location3[i]:
                        continue
                    horse[i] += blue3[location2[i] + dice[j]-1]
                    location2[i] += dice[j]
                    play(j+1,location,location2,horse,location3,location4)
                    if location3[i]:
                        horse[i] -= blue3[location2[i]-1]
                        location2[i] -= location3[i]
                        location3[i] = 0
                    else:
                        horse[i] -= blue3[location2[i] + dice[j] - 1]
                        location2[i] -= dice[j]
            elif 0<=location[i]<=20:
                horse[i] += board[location[i] + dice[j]-1]
                location[i] += dice[j]
                play(j+1,location,location2,horse,location3,location4)
                if location4[i]:
                    horse[i] -= location[i]
                    location[i] -= location4[i]
                    location4[i] = 0
                else:
                    location[i] -= dice[j]
                    horse[i] -= board[location[i] + dice[j] - 1]

board = [i for i in range(2, 41, 2)]
blue1 = [13, 16, 19, 25, 30, 35, 40]
blue2 = [22, 24, 25, 30, 35, 40]
blue3 = [28, 27, 26, 25, 30, 35, 40]

dice = list(map(int,input().split()))
ans = 0
play(0,[0,0,0,0], [0,0,0,0], [0,0,0,0],[0,0,0,0],[0,0,0,0])
print(ans)