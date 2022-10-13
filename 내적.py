def solution(a, b):
    lists = []
    for i in range(len(a)):
        lists.append(a[i]*b[i])
    return sum(lists)

solution([1,2,3,4],[-3,-1,0,2])