alp = ['L', 'U', 'R', 'D']
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
sX = sY = 1

n = int(input())
moves = list(input().split())
idx = 0
while idx < len(moves):
    while alp.index(moves[idx]) % 2:
        sX = (sX + dx[alp.index(moves[idx])]+1) % n
        idx += 1
    while not alp.index(moves[idx]) % 2:
        sY = (sY + dy[alp.index(moves[idx])]+1) % n
        idx += 1

print(sX, sY)