n, m = map(int,input().split())
numbers = [False] * (m-n+1)

for i in range(2, int(m**0.5)+1):
    p = i**2
    s = int(n/p)
    if n % p != 0:
        s += 1
    for j in range(s, m//p+1):
        numbers[int((j*p) - n)] = True
answer = 0
for i in range(0, m-n+1):
    if not numbers[i]:
        answer += 1

print(answer)