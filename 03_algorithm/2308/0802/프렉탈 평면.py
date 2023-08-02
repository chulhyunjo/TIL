s, N, K, R1, R2, C1, C2 = map(int,input().split())

def find(r, c, l, k, n):
    center = k * (l//n)
    left = int(l/2 - center/2)
    right = int(l/2 + center/2)
    if left <= r < right and left <= c < right:
        return True
    if l > N:
        if find(r%(l//N),c%(l//N),l//N, k, n):
            return True
        else:
            return False


L = N ** s
for i in range(R1, R2+1):
    for j in range(C1, C2+1):
        if find(i,j,L,K,N):
            print(1, end="")
        else:
            print(0,end="")
    print()