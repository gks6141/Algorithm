# N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 것
#N이 주어졌을 때, 퀸을 놓는 방법의 수

def check(x):
# 이전 행에서 놓았던 모든 Queen들을 확인
    for i in range(x):
    # 위쪽 혹은 대각선을 확인
        if row[x] == row[i]:
            return False
        if abs(row[x] - row[i]) == x - i:
            return False
    return True

def dfs(x):
    global result
        if x == n:
            result += 1
        else:
            # x번째 행의 각 열에 Queen을 둔다고 가정
            for i in range(n):
                row[x] = i
                # 해당 위치에 Queen을 두어도 괜찮은 경우
                if check(x):
                    # 다음 행으로 넘어가기
                    dfs(x + 1)

queen = int(input())

row = [0] * queen
result = 0
dfs(0)
print(result)


