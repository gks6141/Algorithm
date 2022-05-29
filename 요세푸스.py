#1번부터 n번까지 원으로 않음
#k 번째 사람 계속 제거
import sys
input = sys.stdin.readline
# deque: queue와 달리 앞,뒤에서 삽입 삭제 가능(원형 기능 구현)
from collections import deque
n, k = map(int, input().split())
# 1부터 N까지의 원소를 삽입
d = deque([i for i in range(1, n + 1)])
result = [] 
for i in range(n):
    # K - 1번 "왼쪽으로 돌리기" 수행
    for i in range(k - 1):
        #popleft(): 앞(왼쪽)의 값 삭제 후 반환
        x = d.popleft()
        d.append(x)
    x = d.popleft() 
    result.append(x)


print('<', end='')
for i in range(len(result)):
    if i < len(result) - 1:
        print(result[i], end=', ')
    else: 
        print(result[i], end='')
print('>')