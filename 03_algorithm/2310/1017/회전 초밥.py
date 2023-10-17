import sys
input = sys.stdin.readline

N, d, k, c = map(int,input().split())
belt = []
for _ in range(N):
    belt.append(int(input()))

l = 0
r = k-1
answer = 0
cnt = [0] * (d+1)
eat = set()

for i in range(l, r+1):
    cnt[belt[i]] += 1
    eat.add(belt[i])

while l < N:
    if c in eat:
        answer = max(len(eat), answer)
    else:
        answer = max(len(eat)+1, answer)

    cnt[belt[l]] -= 1
    if cnt[belt[l]] == 0:
        eat.discard(belt[l])
    l += 1
    r += 1
    cnt[belt[r%N]] += 1
    eat.add(belt[r%N])

print(answer)