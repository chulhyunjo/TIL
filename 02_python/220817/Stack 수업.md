# 스택

- 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조
- 선형구조를 갖는다.
  - 선형구조 : 자료 간의 관계가 1대1의 관계를 갖는다.
  - 비선형구조 : 자료 간의 관계가 1대N의 관계를 갖는다(ex. 트리)
- 자료를 삽입하거나 꺼낼 수 있다.
- **후입선출(LIFO, Last-In-First-Out)**
  - 1, 2, 3 순서대로 넣으면 3, 2, 1 역순으로 꺼낸다.



> 연산

- 삽입: 저장소에 자료를 저장. (push)
- 삭제: 저장소에서 자료를 꺼낸다. 역순.. (pop)
- 공백인지 아닌지 : isEmpty
- top에 있는 item(원소) 반환: (peek)



> push

```python
def push(item):
    s.append(item)
```



> pop

```python
def pop() :
    if len(s) == 0:
        # underflow
        return
    else :
        return s.pop(-1)
```



> Stack 응용 : function call

- 프로그램에서 함수 호추출과 복귀에 따른 수행 순서를 관리
  - 가장 마지막에 호출된 함수가 가장 먼저 실행을 완료하고 복귀하는 후입선출 구조
  - 후입 선출 구조의 스택을 이용하여 수행 순서 관리
  - 지역변수, 매개변수 및 수행 후 복귀할 주소 등의 정보를 스택 프레임(stack frame)에 저장
  - 함수의 실행이 끝나면 스택의 top원소를 삭제하면서 프레임에 저장되어 있던 복귀 주소를 확인하고 복귀
  - 함수 호출과 복귀에 따라 이 과정을 반복하여 전체 프로그램 수행이 종료되면 시스템 스택은 공백 스택이 된다.



> 괄호 확인

```python
# 여는 괄호 push
# 닫는 괄호 pop
# 더이상 괄호가 없을 때, 스택이 비어있으면 정상, 스택에 남은게 있으면 에러
T = int(input())
for tc in range(1, T+1):
    a = input()
    s = []
    answer = 1
    for i in a:
        if i == '(':		
            s.append(i)
        elif i == ')':
            if s: 			#짝 맞추기
                s.pop()
            else:			# 여는 괄호가 모자란 경우
                answer = 0
                break
	if s:					# 스택에 여는 괄호가 남아 있다면
        answer = 0
        
    print(f'#{tc} {answer}')
```



# 재귀 호출

- 자기 자신을 호출하여 순환 수행되는 것
- 재귀 호출의 예) 팩토리얼
  - n에 대한 factorial : 1부터 n까지의 모든 자연수를 곱하여 구하는 연산
  - 마지막에 구한 하위 값을 이용하여 상위 값을 구하는 작업을 반복

```
f0 = 0, f1 = 1
fi = f(i-1) + f(i-2) for i>=2
```

```python
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
```



> Stack 재귀

```python
def f(i,N):
    if i == N:
        print(i)
        return
    else:
        print(i)
        f(i+1, N)

f(0,3)
```



# Memoization

- 앞의 예에서 피보나치 수를 구하는 알고리즘에서 fibo(n)의 값을 계산하자마자 저장하면,

  실행 시간을 **O(n)**으로 줄일 수 있다.

- Memoization 방법을 적용한 알고리즘은 다음과 같다.

```python
#memo를 위한 배열을 할당하고, 모두 0으로 초기화 한다
#memo[0]을 0으로 memo[1]는 1로 초기화 한다

def fibo1(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n-1) _ fibo1(n-2))
    return memo[n]

memo = [0, 1]
```

조금 더 구체적으로 알고 싶다면

- PC : program counter