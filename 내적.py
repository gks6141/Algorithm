#내 풀이
def solution(a, b):
    answer=0
    for x in range(0,len(a)):
        y = a[x]*b[x]
        answer += y
    return answer

#1순위 
def solution(a, b):
    #zip: 함수 길이가 같은 리스트들의 요소를 묶어주는 함수
    #unzip: key,value를 각각의 리스트로 분해하는 함수
    #sum(A): 인자로 전달되는 A의 합을 리턴해주는 함수
    return sum([x*y for x, y in zip(a,b)])


#2순위
solution = lambda x, y: sum(a*b for a, b in zip(x, y))