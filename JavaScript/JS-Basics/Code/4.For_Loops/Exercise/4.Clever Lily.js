function solution(input) {
    let age = Number(input[0]);
    let washingMachinePrice = Number(input[1]);
    let toyPrice = Number(input[2]);
    let totalSum = 0;
    let increasement = 0;

    for (let i = 1; i <= age; i++) {
        if(i%2===1){
            totalSum += toyPrice;
        }
        else if(i%2===0){
            increasement += 10;
            totalSum += increasement-1;
        }
    }

    let diff = Math.abs(totalSum-washingMachinePrice)

    if(totalSum>=washingMachinePrice){
        console.log(`Yes! ${diff.toFixed(2)}`)
    }
    else{
        console.log(`No! ${diff.toFixed(2)}`)
    }
}

solution(["21", "1570.98", "3"]);