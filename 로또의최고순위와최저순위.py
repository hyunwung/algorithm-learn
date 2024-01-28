def solution(lottos, win_nums):
    answer = []
    max_value = 7
    lottos.count(0)
    if 0 in lottos:
        for i in lottos:
            if i in win_nums:
                answer.append(i)
        if len(answer) <= 1:
            temp = 6
        else:
            temp = max_value-len(answer)
        return[max_value-lottos.count(0)-len(answer),temp]
      
    else:
        for i in lottos:
            if i in win_nums:
                answer.append(i)
        answer1 = max_value-len(answer) - lottos.count(0)
        answer2 = max_value-len(answer)
        if answer1 == 7:
            answer1 = 6
        if answer2 == 7:
            answer2 = 6

        return [answer1 , answer2]

print(solution(	[1, 2, 3, 4, 5, 6],[7, 8, 9, 10, 11, 12] ))
# [3, 5]