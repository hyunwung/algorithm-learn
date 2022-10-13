def solution(n):
    change = str(n)
    lists = list(change)
    change_list = list(map(int,lists))
    ans = sum(change_list)
    return ans
