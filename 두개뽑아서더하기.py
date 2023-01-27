from itertools import combinations

def solution(numbers):
    answer = []
    result = list(combinations(numbers, 2))
    for i in result:
        answer.append(sum(i))

    return sorted(list(set(answer)))

solution([2,1,3,4,1])