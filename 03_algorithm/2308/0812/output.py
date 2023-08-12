import sys
sys.stdout = open('input.txt', 'w')

nums = list(range(10, 50000*10+1, 10))
Q = list(range(2, 2*200000+1, 2))
print(50000, 200000)
print(*nums)
for q in Q:
    print(q)
sys.stdout.close()