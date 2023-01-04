def solution(left,right):
    answer = 0
    for i in range(left,right+1):
        ex = 0
        for a in range(1,i+1):
            if i % a == 0:
                ex = ex + 1
        if ex % 2 == 0:
            answer = answer+i
        else:
            answer = answer-i
    return answer

