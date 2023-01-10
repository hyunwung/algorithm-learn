def solution(d, budget):
    answer = 0
    for i in range(len(d)):
        if budget < min(d):
            answer = i
            return answer
            break
        budget = budget - min(d)
        d.remove(min(d))
        answer = i+1

    return answer


solution([2, 2, 3, 3],10)