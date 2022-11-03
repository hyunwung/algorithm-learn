def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 4 , reverse=True)
    return str(int(''.join(numbers)))

solution([3, 30, 34, 5, 9]) # "9534330"
# solution([6, 10, 2]) # "6210"