for tc in range(int(input())):
    n = int(input())
    d0 = [0] * 41
    d1 = [0] * 41
    d0[0], d0[1] = 1, 0
    d1[0], d1[1] = 0, 1

    for i in range(2,n+1):
        d0[i] = d0[i-1] + d0[i-2]
        d1[i] = d1[i-1] + d1[i-2]

    print(d0[n], d1[n])