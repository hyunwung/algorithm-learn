def solution(progresses, speeds):
    # 결과를 담을 리스트
    answer = []
    # 작업 리스트가 빌 때까지 반복
    while progresses:
        # 몇개의 기능이 배포되는지 저장
        cnt = 0
        # 작업 리스트가 남아있고 맨 앞의 작업의 진도가 100인 경우: 기능 배포 변수 증가. 해당 작업과 작업 속도를 리스트에서 제거
        while progresses and progresses[0] >= 100:
            cnt += 1
            progresses.pop(0)
            speeds.pop(0)

        # 작업 리스트의 진도를 증가
        progresses = [progresses[i] + speeds[i] for i in range(len(progresses))]

        # 만약 오늘 기능이 배포되었다면 결과리스트에 추가
        if cnt:
            answer.append(cnt)
    print(answer)
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
