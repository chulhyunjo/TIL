# 다양한 수로 이루어진 배열이 주어진다.
# 각 수들을 M번 더하여 가장 큰 수를 만들어야한다.
# 같은 숫자를 연속해서 K번을 초과하여 더할 수 없다.
# 인덱스가 다르다면 다른 숫자로 간주한다.
"""
입력
5 8 3
2 4 5 4 6

출력
18 + 5 + 18 + 5
46
"""

N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort(reverse=True)
firstNum = numbers[0] # 가장 큰 수
secondNum = numbers[1] # 두번째 큰 수

count = (M // (K+1)) * K
result = firstNum + secondNum * (M // (K+1))
print(result)