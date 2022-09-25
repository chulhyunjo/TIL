A, B = map(int,input().split())
L = R = 0

while A > 1 and B > 1:
    if A < B:
        R += B//A
        B = B%A
    elif A > B:
        L += A//B
        A = A%B
L += A - 1
R += B - 1
print(L, R)