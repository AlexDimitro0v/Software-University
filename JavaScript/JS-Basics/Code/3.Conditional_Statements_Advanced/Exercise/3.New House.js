function solution(input) {
    let flowersType = input[0];
    let flowersNumber = Number(input[1]);
    let budget = Number(input[2]);
    let finalPrice;

    if(flowersType==="Roses"){
        finalPrice = flowersNumber*5
        if(flowersNumber>80){
            finalPrice = finalPrice - finalPrice*(10/100)
        }
    }
    else if(flowersType==="Dahlias"){
        finalPrice = flowersNumber*3.80
        if(flowersNumber>90){
            finalPrice = finalPrice - finalPrice*(15/100)
        }
    }
    else if(flowersType==="Tulips"){
        finalPrice = flowersNumber*2.80
        if(flowersNumber>80){
            finalPrice = finalPrice - finalPrice*(15/100)
        }
    }
    else if(flowersType==="Narcissus"){
        finalPrice = flowersNumber*3
        if(flowersNumber<120){
            finalPrice = finalPrice + finalPrice*(15/100)
        }
    }
    else if(flowersType==="Gladiolus"){
        finalPrice = flowersNumber*2.50
        if(flowersNumber<80){
            finalPrice = finalPrice + finalPrice*(20/100)
        }
    }

    let difference = Math.abs(finalPrice-budget)

    if(finalPrice<=budget){
        console.log(`Hey, you have a great garden with ${flowersNumber} ${flowersType} and ${difference.toFixed(2)} leva left.`)
    }
    else{
        console.log(`Not enough money, you need ${difference.toFixed(2)} leva more.`)
    }
}

solution();