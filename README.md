# Python 문법 정리

### 입력

**몇 개의 숫자를 한 줄에 입력 받기**

```jsx
N, K = map(int, input().split())
```

**한 줄 입력을 리스트로 받기**

```python
distance = list(map(int, input().split()))
```

**여러줄 입력을 리스트로 받기**

```jsx
coins = list(int(input()) for _ in range(N))
```

**조금 더 빠르게 입력 받기**

```python
import sys
input = sys.stdin.readline
expr = input().strip()
# python의 Shadowing을 이용해서 이대로 input()처럼 쓸 수 있음
```

**이중리스트 입력 받기**

```python
conferences = [list(map(int, input().split())) for _ in range(N)]
input().split() : 문자열을 argument를 기준으로 나누고 나뉜 문자열들의 리스트를 반환
input().rstrip() : 오른쪽 끝 공백 지우기
```

### 출력

**줄바꿈 안하고 한줄에 출력하기**

```python
for r in range(N):
    print(rank[r] + 1, end=' ')
```

### 반복문

**while ~ else , for ~ else** 

```python
# 반복문의 조건에 안맞을 때, else의 구문이 실행됨.
```

**세 개의 수를 중복 없이 선택하기 (순서 상관 없음)**

```python
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
```

### 리스트 활용

**리스트차집합 (집합 아님)**

```python
ex_lost = [i for i in lost if i not in reserve]
```

**이중리스트 정렬하기**

```python
meeting.sort(key=lambda x: x[0])  # 0번째 원소 기준 정렬
meeting.sort(key=lambda x: x[1])  # 1번째 원소 기준 정렬
```

**이중리스트의 특정 위치 원소만 뽑아내기**

```python
kg = [build[i][0] for i in range(N)]
cm = [build[i][1] for i in range(N)]
```
