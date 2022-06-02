function solution(input) {
    let n = Number(input[0]);
    let buffer='';

    for (let i = 1111; i <= 9999; i++) {
        let isDivisible = true;
        for (let j = 0; j < i.toString().length; j++) {
            if (n % Number(i.toString()[j])!==0){
                isDivisible = false;
            }
        }
        if(isDivisible){
            buffer += `${i} `
        }
    }
    console.log(buffer)
}

solution(["11"]);