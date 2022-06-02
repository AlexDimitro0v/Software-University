function solution(input) {
    let destination = input[0];
    let index=1;

    while(destination!=="End"){
        let moneySaved=0;
        let moneyNeeded = Number(input[index]);
        index++;
        while(moneySaved<moneyNeeded){
            let money = Number(input[index]);
            moneySaved+=money;
            index++;
        }
        console.log(`Going to ${destination}!`)
        destination = input[index];
        index++;
    }
}

solution(["France",
    "2000",
    "300",
    "300",
    "200",
    "400",
    "190",
    "258",
    "360",
    "Portugal",
    "1450",
    "400",
    "400",
    "200",
    "300",
    "300",
    "Egypt",
    "1900",
    "1000",
    "280",
    "300",
    "500",
    "End"]);