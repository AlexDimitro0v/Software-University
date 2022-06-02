function solution(input) {
    let n1 = Number(input[0]);
    let n2 = Number(input[1]);
    let buffer=""

    for (let i = n1; i <= n2; i++) {
        let evenSum = 0;
        let oddSum = 0;
        for (let j = 0; j < i.toString().length; j++) {
            // let currentDigit = Number(i.charAt(j));
            if(j%2===0){
                evenSum += Number(i.toString()[j])
            }
            else if(j%2===1){
                oddSum += Number(i.toString()[j])
            }
        }
        if(evenSum===oddSum){
            buffer+=`${i} `;
        }
    }
    console.log(buffer)
}

solution(["100000",
    "100050"])
;

