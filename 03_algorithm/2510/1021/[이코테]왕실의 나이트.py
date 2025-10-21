d = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
position = input()
x = int(position[1])
y = ord(position[0]) - 96

result = 0
for dx, dy in d:
    nx, ny = x + dx, y + dy
    if 1 > nx or nx > 8 or 1 > ny or ny > 8: continue
    result += 1

print(result)