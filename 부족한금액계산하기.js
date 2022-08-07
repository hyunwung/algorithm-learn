function solution(price, money, count) {
    let prices = 0
    for (let i=1; i<count+1; i++){
        prices = (price*i)+prices
        
    }
    answer = prices-money
    if (prices < money){
        return 0
    }
    return answer;
}
solution(3,20,4)