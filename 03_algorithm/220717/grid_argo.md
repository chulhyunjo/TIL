## 그리디 알고리즘

### 개념

> 그리디 알고리즘(탐욕법)은 현재 상황에서 지금 당장 좋은 것만 고르는 방법을 의미

- 일반적인 그리디 알고리즘은 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구
- 그리디 해법은 그 **정당성 분석**이 중요
  - 단순히 가장 좋아 보이는 것을 반복적으로 선택해도 최적의 해를 구할 수 있는지 검토
- 일반적인 상황> 최적의 해를 보장할 수 없을 때가 많다
- 코테> 탐욕법으로 얻은 해가 최적의 해가 되는 상황에서, 이를 추론할 수 있도록 출제



### 문제1) 곱하기 혹은 더하기

#### 문제 설명

> 각 자리가 숫자(0~9)로만 이루어진 문자열 S가 주어진다. 
>
> 오른쪽으로 하나씩 모든 숫자를 확인하며 'x' 혹은 '+' 연산자를 넣어 결과적으로 가장 큰수를 구하는 프로그램
>
> 단, +보다 x를 먼저 계산하는 일반적인 계산과는 달리 순서대로 이루어짐.
>
> ex) 02984-> ((((0+2)x9)x8)x4) = 576

```python
s = input()
# 첫 번째 문자를 숫자로 변경하여 대입
result = int(s[0])

for i in s[1:]:
    i = int(i)
    # 숫자 i가 0, 1일 경우 +하는 값이 x보다 크다
    if i <= 1 or result <= 1 :
        result += i
    # 이외의 경우에는 'x'
    else:
        result *= i
print(result)
```



### 문제2) 모험가 길드

#### 문제 설명

> 모험가는 N명이 있다. 
>
> 대상으로 '공포도'를 측정, 그룹을 구성하기 위해서는 공포도가 X인 모험가는 반드시 X명으로 구성.
>
> 최대 몇개의 모험가 그룹을 만들 수 있는지 최대값을 구하여라.

```python
n = int(input())
data = list(map(int,input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포도를 낮은 것 부터 하나씩 확인
    count += 1 # 현재 그룹에 해당 모험가를 포함
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 형성
        result += 1 # 총 그룹 수 증가
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화
print(result)
```
