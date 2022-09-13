n = int(input())
member = []

for _ in range(n):
    body = kg, cm = list(map(int,input().split()))
    member.append(body)

for i in member:
    count = 1
    for j in member:
        if i[0] < j[0] and i[1] < j[1]:
            count += 1

    print(count, end = ' ')