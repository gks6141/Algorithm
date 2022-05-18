#알파벳 소문자로 이루어진 문자열
#문자열에서 2개 붙어있는 짝을 찾음
#둘을 제거 다시 둘이있으면 제거 
#수행가능하면 1 수행불가면 0
def solution(s):
    answer = []
    for i in s:
        if not(answer):
            answer.append(i)
        else:
            if(answer[-1] == i):
                answer.pop()
            else:
                answer.append(i)    
    return not(answer)


def solution(s):
    s = list(s)
    a=[]
    a.append(s[0])

    for i in s[1:]:
        if len(a)<1:
            a.append(i)
            continue
        if a[-1] == i:
            a.pop()
        else:
            a.append(i)


    if len(a)==0:
        answer = 1
    else:
        answer = 0
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    return answer