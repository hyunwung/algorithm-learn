def solution(answers):
    a=[1,2,3,4,5]
    b=[2, 1, 2, 3, 2, 4, 2, 5]
    c=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    result = []
    a_stack = 0
    b_stack = 0
    c_stack = 0
    for i in range(len(answers)):
        s1 = i % 5
        s2 = i % 8
        s3 = i % 10
        if a[s1] == answers[i]:
            a_stack += 1
        if b[s2] == answers[i]:
            b_stack += 1
        if c[s3] == answers[i]:
            c_stack += 1

    answer = max(a_stack,b_stack,c_stack)
    if a_stack == answer:
        result.append(1)
    if b_stack == answer:
        result.append(2)
    if c_stack == answer:
        result.append(3)
    result = result.sort()
    print(result)
    return result

solution([1,2,3,4,5,1,3,1,3,4,5,1,2,4,2,1,2])