A = int(input())
B = int(input())
C = int(input())

num = f'{A * B * C}'
for i in range(10):
    print(num.count(f"{i}"))