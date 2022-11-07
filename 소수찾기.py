from itertools import permutations


def sosu(n):
    if n < 2:
        return False

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True


def solution(numbers):
    answer = 0
    p = []
    result = []

    for i in range(1, len(numbers) + 1):
        p.extend(permutations(numbers, i))
        print(p)
        result = [int(''.join(i)) for i in p]
        print(result)

    for i in set(result):
        if sosu(i):
            answer += 1
    print(answer)
    return answer
solution("011")