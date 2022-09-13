S = list(input())
P = []
Q = 0
while S:
    if S[-1] == '(':
        S.pop()
        K = int(S.pop())
        Q = Q * K
        while P[-1] != ')':
            Q += P.pop()
        P.pop()
    elif S[-1] == ')':
        P.append(S.pop())
        P.append(Q)
        Q = 0
    else:
        S.pop()
        Q += 1
print(Q)