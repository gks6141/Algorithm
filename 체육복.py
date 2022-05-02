def solution(n, lost, reserve):
    student = list(range(1,n+1))
    for i in student:
        if lost not in i:
            lost
            answer = 0
    return answer



def solution(n, lost, reserve):
    #lost값을 제외한 reserve값  
    _reserve = [r for r in reserve if r not in lost] 
    #reserve값을 제외한 lost값
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)


def solution(n, lost, reserve):
    answer = 0
    for i in range(1, n+1):
        if i not in lost: #안 잃어버린 학생
            answer += 1
        else:
            if i in reserve: #잃어버렸지만 여분도 있는 학생
                answer += 1
                #remove() 리스트 형태의 data에서 일부 삭제하는 함수
                #del : 리;스트의 인덱스를 받아서 삭제하는 명령어
                reserve.remove(i)
                lost.remove(i)

    for i in lost: #잃어버리고 여분도 없어서 빌려야 하는 학생
        if i-1 in reserve:
            answer += 1
            reserve.remove(i-1)

        elif i+1 in reserve:
            answer +=1
            reserve.remove(i+1)

    return answer




def solution(n, lost, reserve):
    #SET 중복값 없이 출력
    reserve = set(reserve)
    
    for size in [0, 1, -2]:
        #map(변환 함수, 순회 가능한 데이터): 여러 개의 데이터를 한 번에 다른 형태로 변환하기 위해서 사용
        lost = set(map(lambda x : x+size, lost))
        reserve, lost = reserve - lost, lost - reserve

    return n - len(lost)
