
#1 순위

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
            #set: 겹치는 숫자가 없이 저장
            #sorted:  오름차순으로 저장
    return sorted(list(set(answer)))



# 2순위
from itertools import combinations

def solution(numbers):
    answer = []
    #combinations(range(1, 46), 6): 1~45의 숫자중에서 6개를 뽑아내는 경우의수를 리턴 
    l = list(combinations(numbers, 2))

    for i in l:
        answer.append(i[0]+i[1])
    answer = list(set(answer))
    answer.sort()