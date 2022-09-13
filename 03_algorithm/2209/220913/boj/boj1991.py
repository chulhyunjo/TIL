def pre(n):
    if n != '.':
        print(n, end='')
        pre(ch1[ord(n) - 65])
        pre(ch2[ord(n) - 65])

def inorder(n):
    if n != '.':
        inorder(ch1[ord(n) - 65])
        print(n, end='')
        inorder(ch2[ord(n) - 65])

def post(n):
    if n != '.':
        post(ch1[ord(n) - 65])
        post(ch2[ord(n) - 65])
        print(n, end='')



V = int(input())
E = V - 1
ch1 = [''] * V
ch2 = [''] * V
for _ in range(V):
    p, c1, c2 = input().split()
    ch1[ord(p)-65] = c1
    ch2[ord(p)-65] = c2
pre('A')
print()
inorder('A')
print()
post('A')