# 1부터 rows X columns까지의 숫자가 한줄씩 순서대로 나열
# 회전의 표현 (x1,y1,x2,y2)인 정수 4개로 표현 
# x1,y1 부터 x2,y2까지 직사각형 테두리
# 위치가 바뀐 숫자들중 가장작은 숫자들을 순서대로 배열에 담아 return
def solution(rows, columns, queries):
    answer = []
    # board 틀을 제작
    board = [[i+(j)*columns for i in range(1,columns+1)] for j in range(rows)]
    # print(board)

    for a,b,c,d in queries:
        stack = []
        r1, c1, r2, c2 = a-1, b-1, c-1, d-1

        # x1의 열의 정보
        for i in range(c1, c2+1):

            stack.append(board[r1][i])
            if len(stack) == 1:
                board[r1][i] = stack[-2]
                continue
            else:

        #x1기준 행의 정보     
        for j in range(r1+1, r2+1):
            stack.append(board[j][i])
            board[j][i] = stack[-2]
        # y2의 열의 정보 
        for k in range(c2-1, c1-1, -1):
            stack.append(board[j][k])
            board[j][k] = stack[-2]
        #y2의 행의 정보
        for l in range(r2-1, r1-1, -1):
            stack.append(board[l][k])
            board[l][k] = stack[-2]

        answer.append(min(stack))


    return answer



# 데크의 개념 : 양방향 큐   앞,뒤 양쪽 방향에서 엘리먼트를 추가하거나 제거 가능
# 양끝 엘리먼트의 append와 pop이 빠름
from collections import deque
def solution(rows, columns, queries):
    arr = [[i+columns*j for i in range(1,columns+1)] for j in range(rows)]

    answer, result = deque(), []
    for i in queries:
        a,b,c,d = i[0]-1,i[1]-1,i[2]-1,i[3]-1
        for x in range(d-b):
            answer.append(arr[a][b+x])
        for y in range(c-a):
            answer.append(arr[a+y][d])
        for z in range(d-b):
            answer.append(arr[c][d-z])
        for k in range(c-a):
            answer.append(arr[c-k][b])
        #deque.rotate(num): 데크를 num만큼 회전(양수 오른쪽, 음수 왼쪽)
        answer.rotate(1)
        # deq.append(item): 오른쪽 끝에 삽입
        result.append(min(answer))
        for x in range(d-b):
            arr[a][b+x] = answer[0]
            # deque.popleft: 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제
            answer.popleft()
        for y in range(c-a):
            arr[a+y][d] = answer[0]
            answer.popleft()
        for z in range(d-b):
            arr[c][d-z] = answer[0]
            answer.popleft()
        for k in range(c-a):
            arr[c-k][b] = answer[0]
            answer.popleft()
    return result