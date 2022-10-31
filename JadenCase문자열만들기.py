
def solution(s):
    words = s.split(" ")
    print(words)
    for i in range(len(words)):
        words[i] = words[i].capitalize()
    result = " ".join(words)
    print(result)
    return result

solution("for the last week")