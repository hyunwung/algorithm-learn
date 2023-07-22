
def solution(map, dir):
    answer = ''
    min_p = [1,1]
    max_p = [map,map]
    dir = dir.split(' ')
    for i in dir:
        if i == 'R':
            min_p[0] = min_p[0] + 1

        if i == 'L':
            if min_p[0] == 1:
                continue
            min_p[0] = min_p[0] - 1

        if i == 'U':
            if min_p[1] == 1:
                continue
            min_p[1] = min_p[1] - 1
        if i == 'D':
            min_p[1] = min_p[1] + 1
    for i in min_p:
        if answer == '':
            answer = str(i)
        else:
            answer = answer + ' ' + str(i)
    return answer

print(solution(5,"L R R D D"))
