def solution(number, limit, power):
    weight = 0
    for i in range(1,number+1):
        temp = []
        for j in range(1,int(i**(1/2))+1):
            if i % j == 0:
                print(j)
                temp.append(j)
                if j ** 2 != i:
                    temp.append(i // j)
        if len(temp) > limit:
            weight = weight + power
        else:
            weight = weight + len(temp)
    return weight

solution(10,3,2)
# 21