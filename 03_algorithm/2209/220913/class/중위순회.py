def inorder(n):
    if n:
        inorder(ch1[n])
        print(alp[n-1],end='')
        inorder(ch2[n])


for tc in range(1, 11):
    V = int(input())
    ch1 = [0] * (V+1)
    ch2 = [0] * (V+1)
    alp = []
    for _ in range(V):
        n, *arr = input().split()
        n = int(n)
        alp.append(arr[0])
        for i in range(1, len(arr)):
            if ch1[n] == 0:
                ch1[n] = int(arr[i])
            else:
                ch2[n] = int(arr[i])
    print(f'#{tc}', end = ' ')
    inorder(1)
    print()