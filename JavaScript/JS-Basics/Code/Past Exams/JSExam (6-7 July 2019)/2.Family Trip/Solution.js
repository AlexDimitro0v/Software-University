function solution(input) {
    const budget = Number(input[0])
    const stayPeriod = Number(input[1])
    let price = Number(input[2])
    const VAT = Number(input[3])

    if (stayPeriod > 7){
        price = (price - price*5/100)*stayPeriod
    }
    else {
        price = price*stayPeriod
    }

    let additionalExpenses = budget*VAT/100
    let totalPrice = price + additionalExpenses

    if (budget >= totalPrice){
        console.log(`Ivanovi will be left with ${(budget-totalPrice).toFixed(2)} leva after vacation.`)
    }
    else {
        console.log(`${(totalPrice-budget).toFixed(2)} leva needed.`)
    }
}

solution(["800.5", "8", "100", "2"]);