def solution(n):
    answer = n
    while n > 0:
        answer = answer+1
        if bin(answer)[2:].count("1") == bin(n)[2:].count("1"):
            break
    return answer

solution(15)