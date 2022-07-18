function solution(arr) {
    var answer = 0;
    const sum = arr.reduce((a, b) => a + b, 0);
    var answer = (sum / arr.length) || 0;

    
    return answer;
}
solution([1,2,3,4])