# 트리(TREE)

- 가계도와 같은 계층적인 구조를 표현할 때 사용할 수 있는 자료구조

![img](https://blog.kakaocdn.net/dn/bfRCJ5/btqEo8GNNn9/VPGp3EOJPt6uKDcLrI11r1/img.jpg)

## 관련 용어

- 루트 노드(root node) : 부모가 없는 최상위 노드
- 단말 노드(leaf node) : 자식이 없는 노드
- 크기(size) : 트리에 포함된 모든 노드의 개수
- 깊이(depth) : 루트 노드부터의 거리
- 높이(height) : 깊이 중 최대값
- 차수(degree) : 각 노드의 (자식 방향) 간선 개수 (자식의 수)

기본적으로 트리의 크기가 N일 때, 전체 간선의 개수는 N - 1 개이다.



## 이진 탐색 트리(Binary Search Tree)

- 이진 탐색이 동작할 수 있도록 고안된 효율적인 탐색이 가능한 자료구조의 일종
- 이진 탐색 트리의 특징 : 왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드
  - 부모 노드보다 왼쪽 자식 노드가 작습니다.
  - 부모 노드보다 오른쪽 자식 노드가 큽니다.



> 이진 탐색 트리가 이미 구성되어 있다고 가정하고 데이터를 조회하는 과정

- 찾고자하는 원소 : 37

![image-20220821140358930](C:\Users\chaom\AppData\Roaming\Typora\typora-user-images\image-20220821140358930.png)

![image-20220821140434887](C:\Users\chaom\ssafy8\04_TIL\02_python\220817\image-20220821140434887.png)



## 트리의 순회

- 트리 자료구조에 포함된 노드를 특정한 방법으로 한 번씩 방문하는 방법
  - 트리의 정보를 시각적으로 확인할 수 있다.
- 대표적인 트리 순회 방법은 다음과 같다
  - 전위 순회(pre-order traverse) : 루트를 먼저 방문
  - 중위 순회(in-order traverse) : 왼쪽 자식을 방문한 뒤에 루트를 방문
  - 후위 순회(post-order traverse) : 오른쪽 자식을 방문한 뒤에 루트를 방문

![image-20220821141648563](C:\Users\chaom\AppData\Roaming\Typora\typora-user-images\image-20220821141648563.png)



- 전위 순회 : A → B → D → E → C → F → G
- 중위 순회 : D → B → E → A → F → C → G
- 후위 순회 : D → E → B → F → G → C → A