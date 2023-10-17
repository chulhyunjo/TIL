N = int(input())
balls = input()

cnt = [0,0,0,0]
answer = 0

r = 0
b = 0
for i in range(N):
    if balls[i] == 'R':
        b += 1
        cnt[1] += r
        r = 0
    else:
        r += 1
        cnt[0] += b
        b = 0

r = 0
b = 0
for i in range(N-1, -1, -1):
    if balls[i] == 'R':
        b += 1
        cnt[2] += r
        r = 0
    else:
        r += 1
        cnt[3] += b
        b = 0

print(min(cnt))