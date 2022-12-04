def solution(progresses, speeds):
    # 결과를 담을 리스트
    answer = []
    time = 0 # 회당 작업 횟수
    count = 0 # 들어갈 카운트

    while len(progresses) > 0: # 길이만큼 반복
        if (progresses[0] + time * speeds[0]) >= 100: # 작업 + 시간 * 속도
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])

from collections import deque
#
# def solution(progresses, speeds):
#     answer = []
#     prog = deque(progresses)
#     spd = deque(speeds)
#
#     while prog:
#         for i in range(len(prog)):
#             prog[i] += spd[i]
#
#         tmp = 0
#         try:
#             while prog[0] >= 100:
#                 tmp += 1
#                 prog.popleft()
#                 spd.popleft()
#         except:
#             pass
#
#         if tmp > 0:
#             answer.append(tmp)
#
#     return answer
