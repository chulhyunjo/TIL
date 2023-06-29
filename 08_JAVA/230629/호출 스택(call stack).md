# 호출 스택(call stack)

- 스택: 밑이 막힌 상자, 위에서 차곡차고 쌓인다.

- 메서드 수행에 필요한 메모리가 제공되는 공간

- 메서드가 호출되면 호출 스택에 메모리 할당, 종료되명 해제

- 아래 있는 메서드가 위의 메서드를 호출

  ![image-20230629144419448](C:\Users\chaom\AppData\Roaming\Typora\typora-user-images\image-20230629144419448.png)

 

## 기본형 매개변수

- 기본형 매개변수 - 변수의 값을 읽기만 할 수 있다 (read only)
- 참조형 매개변수 - 변수의 값을 읽고 변경할 수 있다 (read & write)



## static 메서드(클래스 메서드)

- 객체 생성 없이 클래스이름.메서드이름()으로 호출
- 인스턴스 멤버와 관련없는 작업을 하는 메서드
- 메서드 내에서 인스턴스 변수(iv) 사용 불가



## 인스턴스 메서드

- 인스턴스 생성 후, '참조변수.메서드이름()'으로 호출
- 인스턴스 멤버(iv, im)와 관련된 작업을 하는 메서드
- 메서드 내에서 인스턴스 변수(iv) 사용 가능



```java
class MyMath2 {
    long a, b; // 인스턴스 변수
    
    long add() { // 인스턴스 메서드
        return a + b;
    }
    
    // a, b 는 지역변수(lv)
    static long add(long a, long b) { // 클래서 메서드(static 메서드)
        return a + b;
    }
}
```



```java
class MyMathTest2 {
    public static void main(String[] args){
        MyMath2.add(200L, 100L); // 클래스 메서드 호출
        MyMath2 mm = new MyMath2(); // 인스턴스 생성
        mm.a = 200L;
        mm.b = 100L;
        long result = mm.add();
    }
}
```



## static은 언제 붙여야 하나?

- 속성 중에서 공통 속성에 static을 붙인다.
- 인스턴스 멤버를 사용하지 않는 메서드에 static을 붙인다.

![image-20230629150551791](C:\Users\chaom\AppData\Roaming\Typora\typora-user-images\image-20230629150551791.png)

static 메서드는 인스턴스 메서드(im)를 호출할 수 없다.

> static 메서드는 호출 시에 객체가 없을 수 있다.





