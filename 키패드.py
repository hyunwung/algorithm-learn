def solution(numbers, hand):
    answer = ''
    star = 10

    sharp = 12
    left = 11
    right = 12
    for i in numbers:
        if (i==1 or i == 4 or i == 7 or i == star):
            answer = answer+"L"
        elif (i == 3 or i == 6 or i == 9 or i == sharp):
            answer = answer+"R"
        else:
            if (abs(numbers[i-1]-i) < abs(numbers[i+1]-i)):
                if(abs(numbers[i-1]-i)==):
                    answer = answer + "L"
        # if ((numbers[i+1]-i == 2 or 5 or 8 or 0) or i - numbers[i+1] == 2 or 5 or 8 or 0):# 나머지 2 5 8 10
        #     if (hand=="right"):
        #         answer = answer + "R"
        #     elif (hand == "left"):
        #         answer = answer + "L"
        # elif (abs(numbers[i-1]-i) < abs(numbers[i+1]-i)):
        #


    print(answer)
    return answer

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right")