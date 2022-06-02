function solution(input) {
    let n = Number(input[0]);
    let number = 1;

    for (let i=0; i<=n; i+=2){
        console.log(number);
        number = number * 2 * 2
    }
}
