#N개의 문제 줌, 문제를 풀었을 때 컵라면을 몇개 줄 것인지
#N+1
#heapq : 이진 트리 기반의 최소 힙 자료구조 제공 
import heapq
n = int(input())
array = []
q = []


# 문제 정보를 입력 받은 이후에, 데드라인을 기준으로 정렬
for i in range(n):
    a, b = map(int, input().split(' '))
    array.append((a, b))
array.sort()


for i in array:
    a = i[0]
    heapq.heappush(q, i[1])
    # 데드라인을 초과하는 경우에는 최소 원소를 제거
    if a < len(q):
        #heappop() : 원소 삭제
        heapq.heappop(q)
print(sum(q))