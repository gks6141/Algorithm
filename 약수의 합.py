def solution(n):
    b= []
    for a in range(1,3001):
        if n%a == 0:
            b.append(a)
    answer = sum(b)
    return answer


def sumDivisor(num):
    # 나누기 2를하여 성능을 올릴 수 있음
     return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])


#문자열을 정수로 바꾸기
def solution(s):
    answer = int(s)
    return answer