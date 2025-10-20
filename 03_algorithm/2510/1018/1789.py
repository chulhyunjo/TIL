N = int(input())

result = 0
for i in range(1, N+1):
    N -= i
    result += 1
    if N < i+1: break

print(result)