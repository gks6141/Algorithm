def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3
    #int(숫자,base) : 해당 숫자의 x진법으로 나타냄
    answer = int(tmp, 3)
    return answer


def solution(n):
    answer = 0
    cnt = 1
    a = ''
    while n>0:
        a+=str(n%3)
        n = n//3
    print(a)
    for b in range(len(a),0,-1):
        answer += (int(a[b-1])*cnt)
        cnt *= 3
    return answer