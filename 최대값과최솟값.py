def solution(s):
    lists = list(map(int,s.split(" ")))

    answer =" ".join([str(min(lists)),str(max(lists))])

    return answer

solution("-1 -1")