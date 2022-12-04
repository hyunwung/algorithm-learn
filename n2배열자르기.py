def solution(n, left, right):
    answer = []
    temp = []
    plus = 2
    add = 1
    for i in range(1,n+1):
        temp.append(i)
        answer.append(temp)
    for j in temp:
        for p in range(1,j+1):

            # indexs = temp.index(p)
            temp[p-1] = j

        print(temp)


    return answer

solution(4,7,14)