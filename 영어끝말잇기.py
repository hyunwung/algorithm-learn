from collections import Counter

def solution(n, words):
    answer = []
    check=False
    for i in range(len(words)):
        answer.append(words[i])
        if len(answer) != len(set(answer)):
            print("중복")
            check = True
        if i == len(words)-1:
            return [0,0]

        if words[i][-1] != words[i+1][:1] or check == True:
            num1 = (i+1)//n
            if (i+2)%n == 0:

                return [n,num1]
            else:

                return [(i+2)%n,num1+1]





solution(3,	["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])