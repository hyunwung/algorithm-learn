def solution(n, m, section):
    answer = 1
    for i in section:
        if i > answer * m:
            answer = answer + 1
    return answer

print(solution(4,1,[1, 2, 3, 4]))