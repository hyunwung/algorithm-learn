import sys

def solution(num, total):
    answer = []
    count = total / num
    print(count[1])
    # print(round(count))
    for i in count:
        print(i)
    return answer

solution(4,14)
# [2, 3, 4, 5]