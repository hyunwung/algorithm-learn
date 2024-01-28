def solution(ingredient):
    answer = 0
    temp = []
    for i,val in enumerate(ingredient):
        temp.append(val)
        print(temp)
        if temp[-4:] == [1,2,3,1]:
            answer +=1
            for r in range(4):
                temp.pop()
        
    return answer


print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))

# 1 빵
# 2 야채
# 3 고기