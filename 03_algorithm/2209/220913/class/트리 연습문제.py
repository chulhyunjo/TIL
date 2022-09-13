def find_root(V):
    for i in range(1, V+1):
        if par[i] == 0 : # 부모가 없으면 root
            return i

# 전위 순회
def preorder(n):
    if n:
        print(n, end = ' ') # visit(n)
        preorder(ch1[n])
        preorder(ch2[n])
# 중위 순회
def inorder(n):
    if n:
        inorder(ch1[n])
        print(n, end = ' ') # visit(n)
        inorder(ch2[n])
# 후위 순회
def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n, end = ' ') # visit(n)


V = int(input()) # 정점 개수(마지막 정점 번호)
E = V - 1       # 간선 개수
arr = list(map(int,input().split()))

ch1 = [0] * (V+1)
ch2 = [0] * (V+1)
par = [0] * (V+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c
    par[c] = p

root = find_root(V)
preorder(root)
print()
inorder(root)
print()
postorder(root)
print()