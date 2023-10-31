# 전위 순회
def preorder(n):
    print(chr(n+65), end='')
    if tree[n][0] != '.':
        preorder(ord(tree[n][0])-65)
    if tree[n][1] != '.':
        preorder(ord(tree[n][1])-65)

# 중위 순회
def inorder(n):
    if tree[n][0] != '.':
        inorder(ord(tree[n][0])-65)
    print(chr(n+65), end='')
    if tree[n][1] != '.':
        inorder(ord(tree[n][1])-65)

# 후위 순회
def postorder(n):
    if tree[n][0] != '.':
        postorder(ord(tree[n][0])-65)
    if tree[n][1] != '.':
        postorder(ord(tree[n][1])-65)
    print(chr(n+65), end='')

N = int(input())
tree = [[] for _ in range(N)]

for i in range(N):
    parent, c1, c2 = input().split()
    tree[ord(parent)-65].append(c1)
    tree[ord(parent)-65].append(c2)

preorder(0)
print()
inorder(0)
print()
postorder(0)