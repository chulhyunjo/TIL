def preOrder(now):
    if now == '.': return
    print(now, end='')
    preOrder(ch1[ord(now)-65])
    preOrder(ch2[ord(now) - 65])


def inOrder(now):
    if now == '.': return
    inOrder(ch1[ord(now)-65])
    print(now, end='')
    inOrder(ch2[ord(now) - 65])


def postOrder(now):
    if now == '.': return
    postOrder(ch1[ord(now)-65])
    postOrder(ch2[ord(now) - 65])
    print(now, end='')


V = int(input())
E = V - 1
ch1 = [''] * V
ch2 = [''] * V
for _ in range(V):
    p, c1, c2 = input().split()
    ch1[ord(p)-65] = c1
    ch2[ord(p)-65] = c2

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')