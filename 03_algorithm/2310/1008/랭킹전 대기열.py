import sys
input = sys.stdin.readline

p, m = map(int,input().split())
rooms = []
for _ in range(p):
    level, nick = input().rstrip().split()
    flag = 0
    for room in rooms:
        if len(room) == m : continue
        if room[0][0] - 10 <= int(level) <= room[0][0] + 10:
            room.append((int(level),nick))
            flag = 1
            break
    if not flag:
        rooms.append([(int(level), nick)])

for room in rooms:
    if len(room) != m:
        print('Waiting!')
    else:
        print('Started!')
    for l, n in sorted(room, key=lambda x:x[1]):
        print(l, n)