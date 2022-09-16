for t in range(1,int(input())+1):
    N=int(input())
    r=-1
    for i in range(1,N+1):
        if i**3==N:r=i;break
        if i**3>N:break
    print(f'#{t} {r}')