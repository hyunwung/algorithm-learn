function solution(n) {
    answer = Math.sqrt(n)
    if(answer%1===0) {
        answer = answer + 1
        answer = answer*answer
        return answer;
    }
    else{
        return -1;
    }
}
solution(3)