#3^a+3^a+나머지
#a가 3보다 작아야함
#a가 3 초과 시 다음 3^a를 만들고 나머지가 값이 3보다 작으면 3^a를 만들지 않는다
#마지막은 나머지가 3이하여야된다.
import pandas as pd
def solution(n):
    world = [1,2,4,11,12,14,21,22,24,41]
    df =pd.DataFrame(world)
    # str(df.iloc[n-1,0])
    return str(df.iloc[n-1,0])



def change124(n):
    num = ['1','2','4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer
print(change124(10))



def change124(n):
    if n<=3:
        return '124'[n-1]
    else:
        #divmod(x, y) : 나머지와 몫을 튜플로 반환해주는 함수
        q, r = divmod(n-1, 3) 
        return change124(q) + '124'[r]
print(change124(10))