import sys
input = sys.stdin.readline

def turnStick(r,c,sticker):
    sticker = list(map(list, zip(*sticker[::-1])))
    return (c, r, sticker)

def isAttach(x, y, r, c, sticker):
    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1 and board[x+i][y+j] == 1:
                return False
    return True


def attach(x, y, r, c, sticker):
    cnt = 0
    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1:
                board[x+i][y+j] = 1
                cnt += 1
    return cnt


N, M, K = map(int,input().split())
board = [[0] * M for _ in range(N)]
stickers = []
answer = 0
for _ in range(K):
    r, c = map(int,input().split())
    sticker = [list(map(int,input().split())) for _ in range(r)]
    stickers.append((r,c,sticker))

for i in range(K):
    r, c, stick = stickers[i]
    cnt = 0
    if r > N or c > M:
        r, c, stick = turnStick(r, c, stick)
        cnt += 1

    flag = 0
    while cnt < 4:
        for i in range(N-r+1):
            for j in range(M-c+1):
                if isAttach(i, j, r, c, stick):
                    answer += attach(i, j, r, c, stick)
                    flag = 1
                    break
            if flag: break
        if flag: break
        else:
            cnt += 1
            r, c, stick = turnStick(r, c, stick)

print(answer)