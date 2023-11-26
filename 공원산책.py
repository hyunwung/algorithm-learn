def solution(park, routes):
    answer = []
    maps = [len(park),len(park[0])] # [height,width]
    start = []
    obstacle = []
    for i in range(len(park)):
        if 'S' in park[i]:
            temp = park[i].find('S')
            start.append(i)
            start.append(temp)
        if 'X' in park[i]:            
            temp = park[i].find('X')+1
            obstacle.append([temp,i+1])
    for i in range(len(routes)):
        # 맵을 초과하는지
        # 장애물이 있는지
        # E S W N 체크
        if routes[i][0] == 'E':
            if int(routes[i][2]) + start[0] > maps[0]:
                continue
            else:
                for r in obstacle:
                    if r[0] <= start[1] + int(routes[i][2]):
                        continue
                    else:
                        start[0] = start[0] + int(routes[i][2])
            
        if routes[i][0] == 'W': 
            print(0-1)
            if start[0] - int(routes[i][2]) < 0:
                continue
            else:
                for r in obstacle:
                    print(r[0] ,start[1] - int(routes[i][2]))
                    if r[0] >= start[1] - int(routes[i][2]):
                        continue
                    else:
                        start[0] = start[0] - int(routes[i][2])
        
        if routes[i][0] == 'S':
            if start[1] + int(routes[i][2]) > maps[1]:
                continue
            else:
                for r in obstacle:
                    if r[1] <= start[1] + int(routes[i][2]):
                        continue
                    else:
                        start[1] = start[1] + int(routes[i][2])
       
        if routes[i][0] == 'N':
            if start[1] - int(routes[i][2]) < 0:
                continue
            else:
                for r in obstacle:
                    if r[1] >= start[1] - int(routes[i][2]):
                        continue
                    else:
                        start[1] = start[1] - int(routes[i][2])

    answer.append(start[1])
    answer.append(start[0])

    return 
solution(["SOO","OXX","OOO"],["E 2","S 2","W 1"])
# [2,1]