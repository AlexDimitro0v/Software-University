function solution(input) {
    let greenArea = Number(input[0]);
    let price = greenArea*7.61
    let discount = price*(18/100)
    let finalPrice = price - discount
    console.log(`The final price is: ${finalPrice} lv.`)
    console.log(`The discount is: ${discount} lv.`)
}

solution(["150"]);