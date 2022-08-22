def f(i,N,s,t):
    global answer
    if i == N:                          # 모든 원소가 고려된 경우
        if s == t:                      # 부분집합의 합이 t면
            answer += 1
        return
    else:
        f(i+1, N, s+A[i], t)            # A[i]가 포함된 경우
        f(i+1, N, s, t)                 # A[i]가 포함되지 않은 경우


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * 10
answer = 0
f(0, 10, 0, 10)
print(answer)