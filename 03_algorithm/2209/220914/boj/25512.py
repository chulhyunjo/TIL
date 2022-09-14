import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def play(i,color):
    global cnt
    cnt += score[i][color]
    if tree.get(i,0):
        for q in tree.get(i):
            if color == 1:
                play(q,0)
            else:
                play(q,1)


n = int(input().rstrip())
tree = dict()
for _ in range(n-1):
    a, b = map(int,input().rstrip().split())
    tree[a] = tree.get(a,[]) + [b]

score = [list(map(int,input().rstrip().split())) for _ in range(n)]
result = 10**10
for q in range(2):
    cnt = 0
    play(0, q)
    result = min(cnt,result)
print(result)