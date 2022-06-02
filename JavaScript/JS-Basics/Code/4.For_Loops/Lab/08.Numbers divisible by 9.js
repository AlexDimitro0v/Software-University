function solution(input) {
    let n1 = Number(input[0]);
    let n2 = Number(input[1]);
    let totalSum=0;
    let numbers="";

    for (let i = n1; i <= n2; i++) {
        if(i%9===0){
            totalSum+=i;
            numbers+=`${i}\n`
        }
    }
    console.log(`The sum: ${totalSum}`);
    console.log(numbers)
}

solution(["100", "200"]);