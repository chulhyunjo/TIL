def bit_print(i):       # 7번 비트-> 0번 비트 출력
    s = ''
    for j in range(7,-1,-1):
        s += '1' if (i&(1<<j)) else '0'
    print(s)

bit_print(5)
bit_print(-5)
bit_print(-6)
bit_print(-6>>1)