
function solution(s) {   
    value = s.length%2
    if (value === 0){
        sLengthHalf = Math.floor( s.length / 2 )
        answer =(s[sLengthHalf-1]+s[sLengthHalf])   
    }
    else{
        sLengthHalf = Math.floor( s.length / 2 )
        answer = (s[sLengthHalf])   
    }
    console.log(answer)
    return answer;
}
solution("qwer")