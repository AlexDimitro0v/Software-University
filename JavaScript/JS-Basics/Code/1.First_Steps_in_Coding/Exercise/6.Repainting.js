function solution(input) {
    let packing = Number(input[0]);
    let paint = Number(input[1]);
    let paintWater = Number(input[2]);
    let hoursNeeded = Number(input[3]);

    let priceForPacking = (packing+2)*1.50
    let priceForPaint = (paint+paint*10/100)*14.50
    let paintWaterPrice = paintWater*5
    let totalPrice = priceForPacking+priceForPaint+paintWaterPrice+0.40
    let bill = (totalPrice*30/100)*hoursNeeded
    let finalSum = totalPrice + bill

    console.log(`${finalSum.toFixed(2)}`)
}

solution(["10", "11", "4", "8"]);