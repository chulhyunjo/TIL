import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c = int(input())

time = a * 60 + b + c
print((time // 60) % 24, time % 60)