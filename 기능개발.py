#각 기능 은 진도가 100%dlfEo tjqltm qksdud
#speeds : 뒤에 있는 기능이 100퍼센트일때 앞에 있는 기능이 배포될때 같이 배포 
def solution(progresses, speeds):
    Q=[]
    #zip을 이용하여 기능의 작업률과 속도를 합쳐서 계산이 쉽도록 함
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]




def solution(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer