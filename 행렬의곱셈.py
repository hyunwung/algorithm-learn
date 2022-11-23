def solution(arr1, arr2):
    answer = []
    for a in range(len(arr1)):
        temp = []
        for b in range(len(arr2[0])):
            item = 0
            for c in range(len(arr2)):
                item += arr1[a][c] * arr2[c][b]
            temp.append(item)
        answer.append(temp)
    print(answer)
    return answer

solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]])