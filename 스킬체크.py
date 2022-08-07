def solution(x, n):
    a_list = []
    c = 0
    for i in range(n):
        c = c + x
        a_list.append(c)
    print(a_list)
    return a_list

solution(2,5)