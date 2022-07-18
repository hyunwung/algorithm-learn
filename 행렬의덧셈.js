function solution(arr1, arr2) {
    var answer = [];
    for (let i = 0; i<arr1.length; i++){
        let sum = []
        for (let j = 0; j<arr1[i].length; j++){
            sum.push(arr1[i][j] + arr2[i][j])
            
        }
        answer.push(sum)
    }
    console.log(answer)
    return answer;
}
solution([[1,2,3],[2,3,4]],[[3,4,6],[5,6,8]])