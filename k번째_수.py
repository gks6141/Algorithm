#commands =[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
#array = [1, 5, 2, 6, 3, 7, 4]
def solution(array, commands):
    for a in commands(range(0,2),):
        i = int(commands[a,0])
        j = int(commands[a,1])
        k = int(commands[a,2])
        array = array[i-1:j-1]
        array = sorted(array,reverse=False)
        answer = array[k-1]
    return answer




#1순위 답
def solution(array, commands):
    # lambda 매개변수 : 표현식  - 장점 : 코드의 간결함 메모리의 절약
    # def 함수이름(매개변수) return 표현식  -->  lambda 매개변수 : 표현식
    #map(함수, 리스트) :map 함수는 리스트에서 원소를 하나씩 꺼내서 함수를 적용시킨 결과를 새로운 리스트에 담아줌
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))



#2 순위 답
def solution(array, commands):
    answer = []
    # for command in commands: //i,j,k = command --> for i,j,k in commands:    
    for command in commands:
        #각각의 원소를 i,j,k 원소에 맞게 대칭하여 뽑아냄
        i,j,k = command
        # append안에 조건들을 붙여서 입력 가능
        # sorted(리스트, reverse = Ture) = sort(reverse=Ture)
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer

#2순위 변형
def solution(array, commands):
    answer = []
    for i,j,k in commands:
        answer.append(sorted(array[i-1:j])[k-1])
    return answer



# 제일 비슷한 로직의 답
def solution(array, commands):
    answer = []
    # for command in commands --> array에서 n번째 차원의 원소들을 list로 추출 함
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        #같은 숫자가 나왔을 경우 한개의 수만 뽑기때문에 answer의 리스트에 추가하는 조건문을 생성
        if i == j:
            answer.append(array[i-1])
            continue
        
        # array로 덮어쓰기 할 경우 다음 반복때 영향이 미침
        n = array[i-1:j]
        # .sort(reverse=Ture) 오름차순
        n.sort()

        result = n[k-1]
        answer.append(result)

    return answer