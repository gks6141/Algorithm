def solution(s):
    b = 0
    c = 0
    for i in list(s):
        if i == 'p':
            b += 1
        elif i == 'P':
            b += 1
        elif i == 'y':
            c += 1
        elif i == 'Y':
            c += 1
    if b == c:
        d = True        
    else:
        d = False
    return d


def numPY(s):
    return s.lower().count('p') == s.lower().count('y')

#lower: 모두 소문자로 변형
# counter: 리스트에서 중복 인자 누적하여 숫자 셈
from collections import Counter
def numPY(s):
    c = Counter(s.lower())
    return c['y'] == c['p'] 

# 변형
def numPY(s):
    a = 0
    b = 0
    for i in s:
        if i == "p" or i== "P":
            a += 1
        elif i == "y" or i == "Y":
            b += 1
    if a == b:
        return True
    else:
        return False
    return True 
