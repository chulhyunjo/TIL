## StringBuilder - 동기화X

- StringBuffer는 동기화되어 있다. 멀티 쓰레드에 안전(thread-safe)
  - 싱글 쓰레드: 한번에 1개 작업
  - 멀티 쓰레드: 한번에 N개 작업
- 멀티 쓰레드 프로그램이 아닌 경우, 동기화는 불필요한 성능 저하
- 이럴 땐 StringBuilder를 사용하면 성능 향상

