# def solution(numbers, target):
#     answer = 0
#     for i in numbers:
#         for j in range(len(numbers)):
#             if sum(numbers) == target:
#                 answer = answer+1
#             else:
#                 numbers[j] =numbers[j] * -1
#             print(sum(numbers))
#         nonlocal
#     return answer
#
# solution([4, 1, 2, 1],4)

answer = 0
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx== N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])

def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer

solution([4, 1, 2, 1],4)