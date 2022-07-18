process.stdin.setEncoding('utf8');
process.stdin.on('data', data => {
    const n = data.split(" ");
    const a = Number(n[0]), b = Number(n[1]);
    // 이 아래로
    let c = ''
    for (let i=0; i<a; i++){
        c = c + "*"   
        // c = c + "*"
        // console.log(d);
    }
    for (let i=0; i<b; i++){
        console.log(c)
    }
});