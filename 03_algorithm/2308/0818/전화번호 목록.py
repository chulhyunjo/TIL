import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    numbers = []
    for _ in range(n):
        numbers.append(input().rstrip())

    # 정렬
    numbers.sort()
    answer = 'YES'
    for i in range(n-1):
        # 다음 번호가 이전 번호로 시작하면 NO
        if numbers[i+1].find(numbers[i]) == 0:
            answer = 'NO'
            break
    print(answer)