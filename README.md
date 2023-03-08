# CodingTest

[![Solved.ac프로필](http://mazassumnida.wtf/api/v2/generate_badge?boj=sw_devin)](https://solved.ac/sw_devin)
[![Solved.ac잔디](http://mazandi.herokuapp.com/api?handle=sw_devin&theme=warm)](https://solved.ac/sw_devin)

## 📍목표

- 코딩 테스트 감 잃지 않기.
- 라이브 코딩 테스트 대비.

## ⚠️ 규칙

- 매주 알고리즘 주제를 정합니다.
- 해당 주제와 관련있는 문제를 3개 선정하여 풀고 양식에 따라 해설을 정리합니다.
- 일요일 자정까지 문제 풀이를 완료합니다. [문제 정리 노션](https://yebini.notion.site/8bdfab3193b14ba6adf1695372df85f3?v=5309f437f6a140c8829b2e3132864ff5)
- 월요일 자정까지 스터디원의 문제 풀이를 보고 코드 리뷰를 답니다.
- 화요일 자정까지 스터디원의 피드백을 반영하여 코드를 개선합니다.

## 🔍 Python Tips

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
meeting.sort(key=lambda x: x[1])  # 1번째 원소 기준 정렬
meet = sorted(meeting, key=lambda x:x[1])
```

**이중리스트의 특정 위치 원소만 뽑아내기**

```python
kg = [build[i][0] for i in range(N)]
cm = [build[i][1] for i in range(N)]
```

### 사전 활용

**사전의 기본값 생성**

```python
from collections import defaultdict
graph = defaultdict(list)   # 기본값이 list()로 지정됨
```

### Python 수행시간 측정 소스코드

```python
import time
start_time = time.time()  # 측정 시작
## 프로그램 소스코드
end_time = time.time()  # 측정 종료
print("time: ", end_time - start_time)  # 수행 시간 출력
```
