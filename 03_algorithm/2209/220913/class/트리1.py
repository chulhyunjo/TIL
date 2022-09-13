'''
정점 번호 V = 1 ~ (E+1)
간선 수
부노 - 자식 순
4
1 2 1 3 3 4 3 5
'''
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

E = int(input())
arr = list(map(int,input().split()))
V = E + 1
root = 1
# 부모를 인덱스로 자식 번호 저장
ch1 = [0] * (V + 1)
ch2 = [0] * (V + 1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0: # 아직 자식이 없으면
        ch1[p] = c  # 자식1로 저장
    else:
        ch2[p] = c  # 있다면 자식2로 저장

preorder(root)
print()
inorder(root)
print()
postorder(root)