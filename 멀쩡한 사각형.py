#gcd는 math 라이브러리에서 사용 가능
#gcd(int1, int2) :최대 공약수를 반환하는 라이브러리
def gcd(a,b): return b if (a==0) else gcd(b%a,a)    
def solution(w,h): return w*h-w-h+gcd(w,h)



from math import gcd
def solution(w,h):
    return w * h - (w/gcd(w, h) + h/gcd(w, h) - 1) * gcd(w, h)
    
    

def solution(w,h):
    import math

    if w==h:
        return w*(w-1)
    else :
        if h < w:
            t = w
            w = h 
            h =t 
        # 여기 왔으면 무조건 h > w
        # 새로운 함수 정의 
        # 짝수 판별자 함수
        def func(a,b):
            if a < b:
                t = a
                a = b
                b = t
            if b==0:
                return a
            return func(a%b,b)


        x = func(h,w)
        return w*h - (h+w-x)
