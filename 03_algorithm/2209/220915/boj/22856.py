import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def inorder(i):
    c1, c2 = tree.get(i)[0], tree.get(i)[1]
    if c1 != -1:
        inorder(c1)
    intree.append(i)
    if c2 != -1:
        inorder(c2)


def inorder_cnt(i):
    global cnt
    move = 0
    c = tree.get(i)
    if c[0] != -1:
        cnt += 1
        move += 1
        inorder_cnt(c[0])
    if c[1] != -1:
        cnt += 1
        inorder_cnt(c[1])
    if i == intree[-1]:
        print(cnt)
        exit()
    cnt += 1

N = int(input().rstrip())
tree = dict()
root = 1
for _ in range(N):
    n, c1, c2 = map(int,input().rstrip().split())
    tree[n] = [c1,c2]
intree = []
cnt = 0
inorder(1)
inorder_cnt(1)
