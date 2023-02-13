def solution(k, m, score):
    answer = 0
    score = sorted(score,reverse=True)
    for i in range(1,len(score)//m+1):
        answer = answer + score[m * i - 1] * m # 3 7 11
    return answer
solution(4,3,[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2])