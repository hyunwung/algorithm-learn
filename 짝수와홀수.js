function solution(num) {
    var answer = '';
    value = num % 2
    console.log(value)
    if (value === 0){
        answer = "Even"
    }
    else{
        answer = "Odd"
    }
    return answer;
}
solution(4)