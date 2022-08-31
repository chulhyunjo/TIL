from itertools import combinations
import sys
input = sys.stdin.readline

while True:
    k, *arr = map(int,input().rstrip().split())
    if k == 0: break
    for j in combinations(arr,6):
        print(*j)
    print()