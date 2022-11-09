def solution(n):
    answer = 0
    for i in range(1,n+1):
        key= []
        for j in range(n):
            key.append(i+j)
            if sum(key) > n:
                break
            if sum(key) == n:
                answer = answer + 1
                break

    return answer

solution(15)