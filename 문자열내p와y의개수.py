def solution(s):
    answer = True
    a = s.count("p")
    b = s.count("P")
    c = s.count("Y")
    d = s.count("y")
    if a+b == c+d:
        return True
    else:
        return False



solution("pPoooyY")