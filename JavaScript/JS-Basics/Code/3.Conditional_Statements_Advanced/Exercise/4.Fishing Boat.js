function solution(input) {
    let budget = Number(input[0]);
    let season = input[1];
    let fishers = Number(input[2]);
    let finalPrice;

    switch(season){
        case "Spring":
            finalPrice = 3000;
            break;
        case "Summer":
        case "Autumn":
            finalPrice = 4200;
            break;
        case "Winter":
            finalPrice = 2600;
            break;
    }

    if(season!=="Autumn" && fishers%2===0){
        finalPrice = finalPrice-finalPrice*(5/100)
    }

    if(fishers<=6){
        finalPrice = finalPrice-finalPrice*(10/100)
    }
    else if(fishers>=7 && fishers <=11){
        finalPrice = finalPrice-finalPrice*(15/100)
    }
    else if(fishers>=12){
        finalPrice = finalPrice-finalPrice*(25/100)
    }

    let difference = Math.abs(finalPrice-budget);

    if(finalPrice<=budget){
        console.log(`Yes! You have ${difference.toFixed(2)} leva left.`)
    }
    else{
        console.log(`Not enough money! You need ${difference.toFixed(2)} leva.`)
    }
}

solution();