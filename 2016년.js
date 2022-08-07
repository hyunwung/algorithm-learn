function solution(a, b) {
    let day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];
    let date = new Date(`2016-${a}-${b}`);
    // console.log(new Date(`2016-${a}-${b}`))
    console.log(day[date.getDay()])
    return day[date.getDay()];
}
solution(5,24)