N, K = map(int,input().split())
line = list(input())
r = h = -1

for i in range(N):
    if h == -1 and line[i] == 'H':
        h = i
    if r == -1 and line[i] == 'P':
        r = i
    if r != -1 and h != -1:
        break

answer = 0
while 0<=r<N and 0<=h<N:
    if abs(h - r) <= K:
        answer += 1
        h += 1
        r += 1
        while h < N and line[h] != 'H':
            h += 1
        if h - r > K:
            r = h-K
        while r < N and line[r] != 'P':
            r += 1
    else:
        if h > r:
            r += 1
            while r < N and line[r] != 'P' or not abs(h - r) <= K:
                r += 1
        else:
            h += 1
            while h < N and line[h] != 'H' or not abs(h - r) <= K:
                h += 1

print(answer)