import sys
input = sys.stdin.readline

N = int(input())

Music = list(map(int,input().split()))

cnt = [0] * N

# [1] 1 ~ i까지의 실수한 부분을 cnt리스트에 담는다
for i in range(1, N):
    if Music[i] < Music[i-1]:   # 현재 난이도가 이전 난이도보다 낮으면 실수하는 부분
        cnt[i] = cnt[i-1] + 1
    else:
        cnt[i] = cnt[i-1]

Q = int(input())
# [2] a ~ b 사이에 실수한 부분의 개수
# 1 ~ b 까지 실수한 개수 - 1 ~ a 까지 실수한 개수
for _ in range(Q):
    a, b = map(lambda x: int(x) - 1, input().split())
    print(cnt[b] - cnt[a])