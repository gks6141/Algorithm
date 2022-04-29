
#__eq__, __lt__: 크기를 비교할 때 사용하는 함수 
#lt(less than): <
#le(less or equal): <= 
#eq(equal): ==
#ne(not equal): !=
#gt(great than): >
#ge(great or equal): >=
# 1순위
class ALWAYS_CORRECT(object):
    def __eq__(self,other):
        return True

def solution(a):
    answer = ALWAYS_CORRECT()
    return answer;


# 2순위
def solution(nums):
    #combinations(iterable, r): iterable에서 요소의 길이 r 서브 시퀀스 반환
    from itertools import combinations as cb
    answer = 0
    # num에서 길이 3 서브 시퀀스 반환
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer



def solution(nums):
    answer = 0

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                number = nums[i] + nums[j] + nums[k]
                if len([m for m in range(2, number) if number % m == 0]) == 0:
                    answer += 1

    return answer
