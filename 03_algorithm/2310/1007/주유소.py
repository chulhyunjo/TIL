N = int(input())
distance = list(map(int,input().split()))
price = list(map(int,input().split()))

answer = 0
d = distance[0]
p = price[0]
for i in range(1, N-1):
    if price[i] >= p:
        d += distance[i]
    else:
        answer += d * p
        d = distance[i]
        p = price[i]

answer += p * d
print(answer)