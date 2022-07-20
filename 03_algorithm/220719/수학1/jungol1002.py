from math import gcd
n = int(input())
array = list(map(int, input().split()))
gcd_result = gcd(array[0], array[1])
lcm_result = (array[0]*array[1])//gcd_result
for i in range(2,n):
    gcd_result = gcd(gcd_result, array[i])
    lcm_result = (lcm_result*array[i]) // gcd(lcm_result,array[i])

print(gcd_result, lcm_result)
