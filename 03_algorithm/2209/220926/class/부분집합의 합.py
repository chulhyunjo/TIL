def f2(i, k, t, s, rs):
    global cnt
    cnt += 1
    if i == k:
        if t == s:
            for j in range(10):
                if bit[j]:
                    print(A[j], end = ' ')
            print()
    elif t<=s:
        return
    elif t > s + rs:
        return
    else:
        bit[i] = 0
        f2(i+1, k, t, s, rs-A[i])
        bit[i] = 1
        f2(i + 1, k, t, s+A[i], rs-A[i])

A = [i for i in range(1, 11)]
bit = [0] * 10
cnt = 0
f2(0,10,55,0,sum(A))
print(cnt)