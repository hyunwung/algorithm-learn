
def solution(s, skip, idx):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    answer = ""
    for i in list(skip):
        alpha = alpha.replace(i, "")

    for i in s:
        change = alpha[(alpha.index(i) + idx) % len(alpha)]
        answer += change
    print(answer)
    return answer

solution("aukks","wbqd",5)