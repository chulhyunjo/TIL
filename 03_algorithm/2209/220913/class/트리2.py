def find_root(V):
    for i in range(1, V+1):
        if par[i] == 0 : # 부모가 없으면 root
            return i

# 전위 순회
def preorder(n):
    global cnt
    if n:
        cnt += 1
        preorder(ch1[n])
        preorder(ch2[n])

# 중위 순회
def inorder(n):
    if n:
        inorder(ch1[n])
        print(n)
        inorder(ch2[n])

# 후위 순회
def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n)


V = int(input())
E = V - 1           # 간선 수
arr = list(map(int,input().split()))

ch1 = [0] * (V+1)   # 부모 인덱스, 자식번호 저장
ch2 = [0] * (V+1)
par = [0] * (V+1)   # 자식 인덱스, 부모번호 저장

for i in range(E):
    p, c = arr[2*i], arr[2*i+1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c
    if par[c] == 0:
        par[c] = p

root = find_root(V)
cnt = 0
preorder(3)
print(cnt)