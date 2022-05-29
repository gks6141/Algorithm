n = int(input()) 
# map 지정된 함수로 처리 
arr = list(map(int, input().split())) 
stack = [] 
NGE = [-1] * n # 오큰수 배열
for i in range(n):
    x = arr[i] 
    if len(stack) == 0 or stack[-1][0] >= x: # 내림차순 형태라면(작거나 같은 원소를 만났다면)
        stack.append((x, i)) # (수, 인덱스) 형태로 삽입
    else: # 오름차순 형태라면(큰 수를 만났다면)
        while len(stack) > 0: # 역방향으로 하나씩 꺼내기
            previous, index = stack.pop()
            if previous >= x: # 크거나 같은 이전 원소를 만났다면 다시 삽입
                stack.append((previous, index))
                break
            else:
                NGE[index] = x 
        stack.append((x, i)) 

for x in NGE: 
    print(x, end=' ')