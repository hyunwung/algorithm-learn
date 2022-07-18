function solution(array, commands) {
    var answer = [];
    for (let i=0; i<commands.length; i++){
        cake = array.slice(commands[i][0]-1,commands[i][1])
        cake.sort((a, b) => a - b)
        cake = cake[commands[i][2]-1]
        answer.push(cake)
    }
    return answer;
}
solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])

// function solution(array, commands) {
//     var answer = [];
//     for (let i=0; i<commands.length; i++){
//         cake = array.slice(commands[i][0]-1,commands[i][1])
//         cake.sort()
//         cake = cake[commands[i][2]-1]
//         answer.push(cake)
//     }
//     return answer;
// }
// solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])