function solution(input) {
    let n = Number(input[0]);
    let num = 0;
    for (let rows = 1; rows <= n;rows++) {
        let buffer="";
        for (let cols = 1; cols <= rows; cols++) {
            num += 1;
            if (num>n){
                break;
            }
            buffer+=`${num} `
        }
        console.log(buffer)
    }
}


function solution2(input){
    let n = Number(input[0]);
    let num = 1;
    let isBigger = false;
    let printCurrentLine="";

    for (let rows = 1; rows<=n; rows++){
        for (let cols=1; cols<=rows; cols++){
            if (num>n){
                isBigger = true;
                break;
            }
            printCurrentLine += `${num} `
            num+=1;
        }
        console.log(printCurrentLine);
        printCurrentLine="";
        if (isBigger){
            break;
        }
    }
}

solution(["15"]);