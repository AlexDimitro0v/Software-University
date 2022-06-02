function solution(input) {
    let moneyNeeded = Number(input[0]);
    let moneyAvailable = Number(input[1]);
    let data = input[2];
    let money = Number(input[3])
    let days=0;
    let spendingDays=0;
    let index=4;

    while(moneyAvailable<moneyNeeded){
        if(spendingDays===5){
            console.log("You can't save the money.")
            console.log(days)
            return;
        }
        if(data==="spend"){
            spendingDays+=1;
            moneyAvailable-=money;
            if(moneyAvailable<0){
                moneyAvailable=0;
            }
        }
        else if (data==="save"){
            spendingDays=0;
            moneyAvailable+=money
        }
        data=input[index];
        index++;
        money=Number(input[index])
        index++;
        days+=1;
    }
    console.log(`You saved the money for ${days} days.`)
}

solution(["2000",
    "1000",
    "spend",
    "1200",
    "save",
    "2000"])
;