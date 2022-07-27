# 에러와 예외처리

> 버그란?

- 최초의 버그는 1945년 프로그래밍 일종인 코볼 발명자 그레이스 호퍼가 발견
- 역사상 최초의 컴퓨터 버그는 Mark 2라는 컴퓨터 화면에 벌레인 나방이 들어가 합선을 일으켜 비정상적으로 동작
- 이때부터 소프트웨어에서 발생하는 문제를 버그라고 부름



> 디버깅의 정의

- 잘못된 프로그램을 수정하는 것을 디버깅이라함
- 에러 메시지가 발생하는 경우
  - 해당 하는 위치를 찾아 메시지를 해결
- 로직 에러가 발생하는 경우
  - 명시적인 에러 메시지 없이 예상과 다른 결과가 나온 경우
    - 정상적으로 동작하였던 코드 이후 작성된 코드를 생각해봄
    - 전체 코드를 살펴봄
    - 휴식을 가져봄
    - 누군가에게 설명해봄





### 문법 에러(Syntax Error)

- SyntaxError가 발생하면, 파이썬 프로그램은 실행되지 않음
- 파일이름, 줄번호, ^문자를 통해 파이썬이 코드를 읽어 나갈 때 (parser)문제가 발생한 위치를 표현
- 줄에서 에러가 감지된 가장 앞의 위치를 가리키는 캐럿(caret)기호 (^)를 표시

- Invalid syntax 
  - 문법오류
- assign to literal
  - 잘못된 할당



### 예외(Exception)

- 실행 도중 예상치 못한 상황을 맞이하면, 프로그램 실행을 멈춤
  - 문장이나 표현식이 문법적으로 올바르더라도 발생하는 에러
- 실행 중에 감지되는 에러들을 예외라고 부름
- 예외는 여러 타입으로 나타나고, 타입이 메시지의 일부로 출력됨
  - NameError, TypeError등을 발생한 예외 타입의 종류
- 모든 내장 예외는 Exception Class를 상속 받아 이뤄짐
- 사용자 정의 예외를 만들어 관리할 수 있음



- ZeroDivisionError `10/0`
- NameError `print(name_error)`
- TypeError `1 + '1'`
- IndexError
- KeyError
- ModuleNotFoundError
- ImportError
- KeyboardInterrupt > `ctrt+C`
- IndentationError > 들여쓰기 x



> 예외 처리

- try문 (statement) / except 절(clause)을 이용하여 예외 처리를 할 수 있음
- try문
  - 오류가 발생할 가능성이 있는 코드를 실행
  - 예외가 발생되지 않으면, except없이 실행 종료
- except 문
  - 예외가 발생하면 실행
  - 예외 상황을 처리하는 코드를 받아서 적절한 조치를 취함

```python
try:
    num = input('숫자입력 : ')
    print(int(num))
except ValueError:
    print('숫자가 입력되지 않았습니다!')
```

