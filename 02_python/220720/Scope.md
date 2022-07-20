## Scope

### Python의 범위(Scope)

- 함수는 코드 내부에 local scope를 생성하며, 그외의 공간인 global scope로 구분
- scope
  - global scope : 코드 어디에서든 참조할 수 있는 공간
  - local scope: 함수가 만든 scope. 함수 내부에서만 참조 가능
- variable
  - global variable : global scope에 정의된 변수
  - local variable : local scope에 정의된 변수



### 변수 수명주기(lifecycle)

- 변수는 각자의 수명주기(lifecycle)가 존재
  - built-in scope
    - 파이썬이 실행된 이후부터 영원히 유지
  - global scope
    - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
  - local scope
    - 함수가 호출될때 생성되고, 함수가 종료될 때까지 유지



```python
def func():
    a = 20
    print('local', a) # local 20
func()
print('global', a) # NameError: name 'a' is not defined
```



### *이름 검색 규칙(Name Resolution)

- 파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장
- 아래와 같은 순서로 이름을 찾아나가며, LEGB Rule이라 부름
  - **L**ocal scope: 지역 범위(현재 작업중인 범위)
  - **E**nclosed scope : 지역 범위 한 단계 위 범위
  - **G**lobal scope : 최상단에 위치한 범위
  - **B**uilt-in scope : 모든 것을 담고 있는 범위
- 함수 내에서는 바깥에 있는 Scope 변수를 **수정 할 수 없음**



#### 예시1)

```python
print(sum) # <built-in function sum>
print(sum(range(2))) # 1
sum = 5
print(sum) # 5
print(sum(range(2))) # TypeError: 'int' object is not callable
```



### global 문

- 현재 코드 블록 전체에 적용되며, 나열된 식별자(이름)이 global variable임을 나타냄

```python
# 함수 내부에서 글로벌 변수 변경하기
a = 10
def func1():
    global a
    a = 3

print(a) # 10
func1()
print(a) # 3
```

- 선언된적 없는 변수도 사용 가능

### nonlocal

- global을 제외하고 가장 가까운(둘러싸고 있는) scope의 변수를 연결하도록 함
  - nonlocal에 나열된 이름은 같은 코드 블록에 nonlocal 앞에 등장 x
- global과는 달리 이미 존재하는 이름과의 연결만 가능

```python
x = 0
def func1():
    x = 1
    def func2():
        nonlocal x
        x = 2
    func2()
    print(x) # 2
func1()
print(x) # 0
```

- 자주 사용 x



