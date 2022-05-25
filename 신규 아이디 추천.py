#입력된 아이디와 유사하면서 규칙에 맞는 아이디를 추천해주는 프로그램
# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙임



import re

def solution(new_id):
    # 모두 소문자로 치환
    new_id = new_id.lower()
    #re.sub（정규 표현식, 대상 문자열 , 치환 문자） 
    new_id = re.sub('[^0-9a-z\._-]', '', new_id)
    new_id = re.sub('\.\.+', '.', new_id)

    while new_id[0] == '.' and len(new_id) > 1:
        new_id = new_id[1:]
    while new_id[-1] == '.' and len(new_id) > 1:
        new_id = new_id[:-1]
    if new_id == '.':
        new_id = ''

    if not new_id:
        new_id = 'a'

    new_id = new_id[:15]
    while new_id[-1] == '.':
        new_id = new_id[:-1]

    while len(new_id) <= 2:
        new_id += new_id[-1]

    return new_id






def step5to7(id):

    if id == '':
        id = 'a'

    if len(id) >= 16:
        id = id[0:15]
        if id[-1] == '.':
            id = id[0:14]   

    while(len(id) <= 2):
        id += id[-1]

    return id

def step1to4(id):
    id = id.lower()

    new_str = ''
    for c in id:
        if c >= 'a' and c <= 'z':
            new_str = new_str + c
        elif c >= '0' and c <= '9':
            new_str = new_str + c
        elif c == '-' or c == '_' or c == '.':
            new_str = new_str + c

    id = new_str
    new_str = ''

    for c in id:
        if c == '.' and len(new_str) >= 1 and new_str[-1] == '.':
            continue
        new_str = new_str + c

    id = new_str
    leftside = 0
    rightside = len(id)

    if id[0] == '.':
        leftside += 1

    if id[-1] == '.':
        rightside -= 1

    return id[leftside:rightside]

def solution(new_id):
    # print(step1to4(new_id))
    return step5to7(step1to4(new_id))