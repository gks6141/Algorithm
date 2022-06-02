# 2^n * 2^n인 2차원 배열을 z모양 탐색
def solve(n, x, y):
    global result
    if n == 2:
        if x == X and y == Y:
            print(result)
            return
        result += 1
        if x == X and y + 1 == Y:
            print(result)
            return
        result += 1
        if x + 1 == X and y == Y:
            print(result)
            return
        result += 1
        if x + 1 == X and y + 1 == Y:
            print(result)
            return
        result += 1
        return
        
solve(n / 2, x, y)
solve(n / 2, x, y + n / 2)
solve(n / 2, x + n / 2, y)
solve(n / 2, x + n / 2, y + n / 2)
result = 0
N, X, Y = map(int, input().split(' '))
solve(2 ** N, 0, 0)


