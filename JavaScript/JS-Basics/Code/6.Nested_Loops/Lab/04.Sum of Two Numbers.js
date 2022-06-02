function solution(input) {
    let n1 = Number(input[0]);
    let n2 = Number(input[1]);
    let magicNumber = Number(input[2]);
    let counter=0;

    for (let i = n1; i <=n2; i++) {
        for (let j = n1; j <= n2; j++) {
            counter+=1;
            if(i+j===magicNumber){
                console.log(`Combination N:${counter} (${i} + ${j} = ${magicNumber})`)
                return;
            }
        }
    }
    console.log(`${counter} combinations - neither equals ${magicNumber}`)
}

solution(["1",
    "10",
    "5"])
;