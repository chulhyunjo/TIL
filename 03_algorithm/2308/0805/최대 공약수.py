a, b = map(int,input().split())
if a < b:
    a, b = b, a

while a % b != 0:
    a, b = b, a%b

print('1'*b)