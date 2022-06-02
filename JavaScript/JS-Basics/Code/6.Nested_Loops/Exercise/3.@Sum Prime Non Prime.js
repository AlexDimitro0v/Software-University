function solution(input) {
    let data = input[0];
    let index=1;
    let primeSum=0;
    let nonPrimeSum=0;

    while(data!=="stop"){
        let prime = true;
        let num = Number(data);

        if(Number(data)<0){
            console.log("Number is negative.");
            data=input[index];
            index++;
            continue;
        }
        else if (num===1 || num === 0){
            prime = false;
        }

        for (let i = 2; i < num; i++) {
            if (num % i === 0){
                prime=false;
                break;
            }
        }

        if(prime){
            primeSum += num;
        }
        else {
            nonPrimeSum += num
        }

        data=input[index++];
    }

    console.log(`Sum of all prime numbers is: ${primeSum}`)
    console.log(`Sum of all non prime numbers is: ${nonPrimeSum}`)
}

solution(["3",
    "9",
    "-9",
    "0",
    "7",
    "19",
    "4",
    "stop"]);