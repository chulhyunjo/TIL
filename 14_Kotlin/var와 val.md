# var와 val

- var: **변할 수 있는 수**(variable)의 약자로, 내용을 재 대입할 수 있다.
- val: **값**(value)의 약자로, 식별자의 값을 단 한 번만 초기화할 수 있다. 일단 값을 초기화하고 나면 내용을 변경할 수 없다.

> 식별자: 프로그램을 이루는 요소를 가리키는 데에 사용

`var 식별자 = 초기화`

```kotlin
fun main() {
    var whole = 11
    var fractional = 1.4
    var words = "twas brillig"
    
    // var는 가변이다.
    var sum = 1
    sum += 3
    sum = sum + 2 
}
```

