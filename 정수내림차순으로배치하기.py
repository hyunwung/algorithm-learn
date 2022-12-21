def solution(n):
    answer = []
    answer2 = ""
    for i in str(n):
        answer.append(int(i))
    answer.sort()
    for i in answer:
        answer2 = str(i)+answer2
    return int(answer2)

solution(118372)