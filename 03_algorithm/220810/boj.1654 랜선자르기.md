[출처]https://www.acmicpc.net/problem/1654

# boj.1654 랜선자르기

### [문제 설명]

<hr>

주인공은 N개의 랜선을 만들어야 하는 상황이다.

그래서 친구에게 K개의 랜선을 받아 모두 N개의 같은 길이의 랜선을 만들고자 한다.

K의 랜선을 잘라서 만들어야 한다.

 기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정하자.

그리고 자를 때는 항상 센티미터 단위로 정수 길이만큼 자른다고 가정하자. N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다. 

이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오.



### [입력]

<hr>

첫째 줄에는 오영식이 이미 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N이 입력된다. 

K는 1이상 10,000이하의 정수이고, N은 1이상 1,000,000이하의 정수이다. 그리고 항상 K ≦ N 이다.

 그 후 K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 단위의 정수로 입력된다. 

랜선의 길이는 2^31-1보다 작거나 같은 자연수이다.



### [출력]

<hr>

첫째 줄에 N개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력한다.



### [입력 예제]

<hr>

```
                입력												      출력
                4 11													200
                802
                743
                457
                539
```



### [힌트]

<hr>

802cm 랜선에서 4개, 743cm 랜선에서 3개, 457cm 랜선에서 2개, 539cm 랜선에서 2개를 잘라내 모두 11개를 만들 수 있다.



### [정답]

<hr>

```python
import sys
input = sys.stdin.readline

k, n = map(int,input().split())
arr = [int(input()) for _ in range(k)]

start = 1
end = max(arr)

result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for line in arr:
        if line >= mid:
            total += (line // mid)

    if total < n:
        end = mid - 1

    else:
        result = mid
        start = mid + 1

print(result)
```



### [정답 설명]

<hr>

```python
k, n = map(int,input().split())
arr = [int(input()) for _ in range(k)]
```

- k : 현재 가지고 있는 랜선들의 개수
- n: 잘라서 만들어야 하는 랜선의 개수
- arr : 현재 가지고 있는 랜선들의 길이를 담을 리스트



```python
start = 1 # 시작 위치를 0으로 설정했을때 실행 중 mid값이 0이 되어 ZeroDivisionError가 떴다.
end = max(arr) # 랜선의 길이가 제일 긴 것을 end로 설정
result = 0 # 랜선의 공통 길이를 담을 result 변수 선언
```

이진 탐색을 하기 위해 `start, end`를 설정해야 한다.



```python
while start <= end: # start가 end와 겹쳤을 경우 종료 시키기 위해 조건문 선언
    total = 0	# 잘랐을때 얻는 랜선의 개수를 담을 변수 선언
    mid = (start + end) // 2 # 이진 탐색을 위해 중간값을 선언
    for line in arr:	# arr 리스트에서 갖고 있는 랜선의 길이 하나씩 반복문 돌리기
        if line >= mid:
            total += (line // mid) # mid만큼 잘랐을 경우 생기는 랜선의 개수는 (랜선의 길이 // 자른 길이)

    if total < n:	# 얻고자하는 목표 개수를 못 채웠을 경우 더 짤라야 하므로 end = mid -1 로 설정한다.
        end = mid - 1	# 더 짧은 길이로 짜르기 위함.

    else: # 얻고자하는 목표 개수를 채우거나 넘겼을 때 실행
        result = mid # 최종적으로 공통 길이를 담아서 출력해야 하므로 자른 mid값을 result에 담는다.
        start = mid + 1 # 더 길게 자를 수 있는지 확인하기 위해 start = mid + 1로 이진 탐색 반복
```

