def water_melon(n):
    s = "수박" * n
    return s[:n]


# 실행을 위한 테스트코드입니다.
print("n이 3인 경우: " + water_melon(3));
print("n이 4인 경우: " + water_melon(4));



def solution(n):
    return "".join(["수박"[i%2] for i in range(n)])