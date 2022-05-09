#d : 부서별로 신청한 금액이 들어있는 배열, 
#budget: 예산
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        #마지막 요소를 제거하고  해당 요소를 반환
        d.pop()
    return len(d)



def solution(d, budget):
    d.sort()
    cnt = 0
    for i in d :
        budget -= i
        if budget < 0 :
               break
        cnt += 1
    answer = cnt
    return answer




def solution(d, budget):
    s = 0
    j = 0
    d.sort()
    for i in range(len(d)):
        s += d[i]
        if s > budget:
            break
        else:
            j += 1
    return j