## 오버로딩(overloading)

- 한 클래스 안에 같은 이름의 메서드 여러 개 정의하는 것



### 성립하기 위한 조건

1. 메서드 이름이 같아야 한다.
2. 매개변수의 **개수 또는 타입**이 달라야 한다. (이름만 다르면 안됨)
3. 반환 타입은 영향없다.

```java
class MyMath3 {
    int add (int a, int b) {
        return a + b;
    }
    
    long add (long a, long b) {
        return a + b;
    }
    
    int add(int[] a) {
        int result = 0;
        for (int i=0; i < a.length; i++){
            result += a[i];
        }
        
        return result;
    }
}
```



