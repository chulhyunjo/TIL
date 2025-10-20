def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

TC = int(input())

for i in range(TC):
    A, B = map(int, input().split())
    print(lcm(A, B))