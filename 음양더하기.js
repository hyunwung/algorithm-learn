function solution(absolutes, signs) {
    var answer = 0
    for (let i=0; i<absolutes.length; i++){
        if(signs[i]===true){
            answer = answer + absolutes[i]
            // answer = answer
        }
        else{
            answer = answer - absolutes[i]
            // answer = answer+absolutes[i]
        }
    }
    console.log(answer)
    return answer;
}
solution([4,7,12],[true,false,true])