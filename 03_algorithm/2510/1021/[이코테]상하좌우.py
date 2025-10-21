"""
입력
5
R R R U D D
"""
d = {
    "L": (-1, 0),
    "R": (1, 0),
    "U": (0, -1),
    "D": (0, 1)
}

N = int(input())
moves = list(input().split())

x, y = 1, 1
for move in moves:
    dx, dy = d[move]

    nx, ny = x + dx, y + dy
    if 1 > nx or nx > N: continue
    if 1 > ny or ny > N: continue
    x, y = nx, ny

print(y, x)
