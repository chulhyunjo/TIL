import sys
input = sys.stdin.readline

def pre(i):
    global last
    if i <= len(A):
        tree[i] = A[last]
        last += 1
        pre(2*i)
        pre(2*i+1)

def post(i):
    if i <= len(A):
        post(2*i)
        post(2*i+1)
        print(tree[i])

A = []
while True:
    try:
        A += [int(input().rstrip())]
    except:
        break
tree = [0] * (len(A)+1)
last = 0
pre(1)
print(tree)
post(1)