function solution(input) {
    let drink = String(input[0])
    let sugarType = String(input[1])
    let drinkNumber = Number(input[2])
    let price;

    if (drink==="Espresso") {
        if (sugarType === "Without") {
            price = 0.90*drinkNumber
        }
        else if (sugarType === "Normal") {
            price = drinkNumber
        }
        else if (sugarType === "Extra") {
            price = 1.20 * drinkNumber
        }
    }

    else if (drink==="Cappuccino") {
        if (sugarType === "Without") {
            price = drinkNumber
        }
        else if (sugarType === "Normal") {
            price = 1.20*drinkNumber
        }
        else if (sugarType === "Extra") {
            price = 1.60*drinkNumber
        }
    }

    else if (drink==="Tea") {
        if (sugarType === "Without") {
            price = 0.50*drinkNumber
        }
        else if (sugarType === "Normal") {
            price = 0.60*drinkNumber
        }
        else if (sugarType === "Extra") {
            price = 0.70*drinkNumber
        }
    }


    if (sugarType==="Without") {
        price = price - price*35/100
    }

    if (drink==="Espresso" && drinkNumber >= 5) {
        price = price - price*25/100
    }

    if (price>15) {
        price = price - price*20/100
    }

    console.log(`You bought ${drinkNumber} cups of ${drink} for ${price.toFixed(2)} lv.`)
}

solution(["Espresso", "Without", "10"]);