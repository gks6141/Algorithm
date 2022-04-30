# 먼저 리스트에서 1/2를함
# len(list) 만큼 선택
# 거기에 만약 중복된 숫자가 포함된다면 중복된 숫자가 가장 많은 value를 뽑고 나머지 뽑기 
#  최대 고를수 있는 종류 뽑기 

#min(iterable): 매개변수로 들어온 인자 내부에서 제일 작은 값을 반환
#min( A, B): A와 B중에 작은걸 반환
#1 순위
def solution(ls):
    return min(len(ls)/2, len(set(ls)))


#2순위
def solution(nums):
    answer = 0
    #set: 중복되지 않은 원소를 얻고자 할때 사용
    # 중복을 허용하지 않음
    # 순서가 없음(Unordered)
    myList = set(nums)
    if len(nums)/2 > len(myList):
        answer = len(myList)
    else:
        answer = len(nums)/2
    return answer

#not in 연산자 : 확인하고자 하는 데이터가 있으면 False, 없으면 True를 반환
#값이 있는지 확인 
# a= [1,2,3,4,5]
# for 1 in a: 
#     print('1 exit')
# 비슷하게 생각한 알고리즘
def solution(nums):
    kind = []
    answer = int(len(nums)/2) # 3
    for num in nums:
        if num not in kind:
            kind.append(num)
    # 결과 = A if 조건 else B --> 조건이 Ture 경우: A  ,False 경우: B
    result = len(kind) if answer > len(kind) else answer 
    return result