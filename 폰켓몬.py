from itertools import combinations

def solution(nums):
    unique_types = len(set(nums))

    if len(nums) / 2 > unique_types:
        return unique_types
    else:
        return len(nums) / 2

print(solution([3, 3, 3, 2, 2, 2]))