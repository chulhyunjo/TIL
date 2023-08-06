
def findPrime(a, b):
    numbers = [True] * (b-a+1)

    for i in range(2, int(b**0.5)+1):
        pow = i*i
        start_index = int(b//pow)
        if a % pow != 0:
            start_index += 1
        for j in range(start_index, int(b ** 0.5)+1):
            numbers[j*pow]



N, M = map(int,input().split())
