def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        elif arr[i] != arr[i - 1]:
            answer.append(arr[i])
    print(answer)
    return answer

solution([1,1,3,3,0,1,1])