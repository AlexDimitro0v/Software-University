function solution(input) {
    let pencils = Number(input[0]);
    let markers = Number(input[1]);
    let clearMaterial = Number(input[2]);
    let discountPercentage = Number(input[3])/100;

    let price = pencils*5.80+markers*7.20+clearMaterial*1.20;
    let priceAfterDiscount = price - price*discountPercentage;
    console.log(priceAfterDiscount);
}

solution(["2", "3", "4", "25"]);