def solution(players, callings):
    result = {player: i for i, player in enumerate(players)} # 선수: 등수
    for i in callings:
        point = result[i]
        players[point] , players[point-1] = players[point-1] , players[point]
      
        result[players[point]]=point
        result[players[point-1]]=point -1
  
    
    return players

solution(["mumu", "soe", "poe", "kai", "mine"],["kai", "kai", "mine", "mine"])
# ["mumu", "kai", "mine", "soe", "poe"]