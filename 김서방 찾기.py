#seoul = [kim,....,han]
#answer = 김서방은 1번째에 있다.
def solution(seoul):
    for n in range(0,1001):
        a = seoul[n]
        if a == "kim":
            n
    return n
    print("김서방은"+n+"에 있다")




def findKim(seoul):
    for i in range(len(seoul)):
        if seoul[i]=="Kim":
            #formatting: 문자열 중간중간에 특정 변수를 넣어주기 위해 사용
            #'{인덱스1},{인덱스2}'.format(값1,값2)
            return "김서방은 {}에 있다".format(i)



def findKim(seoul):
    #index 배열에서 값의 위치를 찾아주는 함수, 중복된 값이 있으면 가장 최소의 위치를 리턴
    return "김서방은 {}에 있다".format(seoul.index('Kim'))