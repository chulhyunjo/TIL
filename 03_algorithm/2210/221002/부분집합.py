def f(i, N, s, t, rs):
    global answer
    global cnt
    cnt += 1
    if i == N:
        if s == t:
            answer += 1
        return
    elif s > t:
        return
    elif s + rs < t:
        return
    else:
        f(i+1, N, s+A[i], t, rs - A[i])
        f(i+1, N, s, t, rs - A[i])


A = [i for i in range(1,11)]
bit = [0] * 10
answer = 0
cnt = 0
f(0, 10, 0, 10, sum(A))
print(answer, cnt)