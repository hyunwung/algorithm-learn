from collections import defaultdict
import random

def mix_members(members):
    # answer = {}
    answer = defaultdict(list)
    if len(members) % 7 >= 5 or len(members) % 7 == 0:
        for i in range(len(members)//7):
            for r in range(7):
                item = random.choice(members)
                answer[str(i + 1) + "조"].append(item)
                members.remove(item)
        rest = len(answer)+1
        for i in range(len(members)):
            item = random.choice(members)
            answer[str(rest)+"조"].append(item)

    if len(members) % 6 >= 5 or len(members) % 6 == 0:
        for i in range(len(members)//6):
            for r in range(6):
                item = random.choice(members)
                answer[str(i + 1) + "조"].append(item)
                members.remove(item)
        rest = len(answer) + 1
        for i in range(len(members)):
            item = random.choice(members)
            answer[str(rest)+"조"].append(item)
    if len(members) % 5 >= 5 or len(members) % 5 == 0:
        for i in range(len(members)//5):
            for r in range(5):
                item = random.choice(members)
                answer[str(i + 1) + "조"].append(item)
                members.remove(item)
        rest = len(answer) + 1
        for i in range(len(members)):
            item = random.choice(members)
            answer[str(rest)+"조"].append(item)

    return answer

mix_members(["김수한무","거북이","두루미","배트맨","슈퍼맨","엑스맨","젠틀맨","김치맨","라면맨","뿌이맨","객기맨","이니맨","맨맨맨","락스맨","치파맨"])