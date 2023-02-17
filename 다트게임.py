import re

def solution(dartResult):
    answer = 0
    result = re.split('([*|#])' ,dartResult)
    temp = []
    temp2 = 0
    for i in range(len(result)):

        if "S" in i:
            temp2 = int(result[i][0]) ** 1
            temp.append(temp2)
        if "D" in i:
            temp2 = int(result[i][0]) ** 2
            temp.append(temp2)
        if "T" in i:
            temp2 = int(result[i][0]) ** 1
            temp.append(temp2)
        if "*" == i:
            if i == 0:
                result[i - 1][0]
            else:
                result[i - 1][0]
        if "#" == i:
            result[i - 1][0]
        temp2 = 0


    print(temp)
    return answer

solution("1S#2D*3T")