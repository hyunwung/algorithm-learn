# def solution(people, limit):
#     answer = 0
#     people.sort()
#     num = 0
#     print(people)
#     for i in people:
#         if people[num] + people[num+1] > limit:
#             people.pop(num)
#             answer = answer + 1
#             break
#         elif people[num] + people[num+1] <= limit:
#             people.pop(num)
#             people.pop(num)
#             answer = answer + 1
#     print(answer + len(people))
#     return answer + len(people)
#solution([70, 50, 80, 50,60,80],100)


from collections import deque


def solution(people, limit):
    answer = 0

    people.sort()

    start, end = 0, len(people) - 1
    print(start)
    while start <= end:
        answer += 1
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1

    return answer


solution([70, 50, 80, 50,60,80],100)