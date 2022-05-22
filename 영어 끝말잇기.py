# n과 사람들이 순서대로 말한 단어 words 가 매개변수
# 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락


def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]



def solution(n, words):
    answer = []
    turn = 0
    wordList = [words[0]]
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for idx in range(1, len(words)):
        if words[idx-1][-1] != words[idx][0]:
            turn = idx
            break
        if words[idx] in wordList:
            turn = idx
            break
        wordList.append(words[idx])
    answer = [turn%n +1, turn//n + 1]
    if turn == 0:
        answer = [0, 0]
    return answer



import math
def solution(n, words):
    answer = []
    Pnum =0
    arr =[]
    i=0
    count = 1
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    arr.append(words[0])
    while(1):
        if len(arr)!=len(words):
            if words[i][-1]==words[i+1][0] and words[i+1] not in arr:
                arr.append(words[i+1])
                Pnum= (Pnum+1)%n
                i=(i+1)%(len(words)-1)
                count+=1
            else :
                count=(count+1)/n
                Pnum= (Pnum+1)%n
                break
        else :
            count=(count+1)/n
            Pnum= (Pnum+1)%n
            return [0,0]
    answer = [Pnum+1,math.ceil(count)]
    print(round(5/2,-1))
    return answer