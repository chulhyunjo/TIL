import sys
input = sys.stdin.readline

N, M = map(int,input().split())
memo = dict()
cnt = N
for _ in range(N):
    word = input().rstrip()
    memo[word] = 1

for _ in range(M):
    words = input().rstrip().split(',')
    for w in words:
        if memo.get(w, 0):
            del memo[w]
            cnt -= 1
    print(cnt)
