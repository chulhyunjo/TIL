# 내부 클래스(inner class)

- 클래스 안의 클래스

```java
class A { // 와부 클래스
    ...
    class B { // 내부 클래스
        ...
    }
}
```

- 내부 클래스에서 외부 클래스의 멤버를 쉽게 접근이 가능

- 코드의 복잡성을 줄인다. (캡슐화)



## 익명 클래스(anonymous class)

- 이름이 없는 일회용 클래스. 정의와 생성을 동시에

```java
new 조상클래스이름() {
    //멤버선언
}
		or
new 구현인터페이스이름() {
    //멤버선언
}
```

```java
class ~~~{
    Object iv = new Object(){void method(){}};				// 익명 클래스
    static Object cv = new Object{ void method(){} };		// 익명 클래스
    
    void myMethod() {
        Object lv = new Object(){ void method() {} };		// 익명 클래스
    }
}
```

