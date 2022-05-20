# permutation(리스트, 해당 원소의 수)
from itertools import permutations
def solution(n):
    # 들어온 값을 나눠줌
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)




# permutation(리스트, 해당 원소의 수)
from itertools import permutations

def solution(numbers):
    answer = 0
    candidates, num_set = [], set()
    digits = [digit for digit in numbers]

    for i in range(1, len(numbers)+1):
        candidates += [*list(permutations(digits, i))]

    for candidate in candidates:
        num_set.add(int(''.join(map(str, candidate))))

    for num in num_set:
        if is_prime(num):
            answer += 1

    return answer

def is_prime(number):
    if number == 0 or number == 1:
        return False

    for i in range(2, number//2 + 1):
        if (number/i) == (number//i):
            return False

    return True