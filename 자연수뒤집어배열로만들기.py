def solution(n):
    lists = list(str(n))
    lists.reverse()
    change_list = list(map(int,lists))
    return change_list

solution(12345)