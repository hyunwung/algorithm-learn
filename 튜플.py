
def solution(s):
    answer = []
    s= s[2:-2].split("},{")
    s.sort(key=len)

    for i in s:
        lists = i.split(",")
        for j in lists:

            if int(j) not in answer:
                answer.append(int(j))
    print(answer)
    return answer

solution("{{20,111},{111}}")