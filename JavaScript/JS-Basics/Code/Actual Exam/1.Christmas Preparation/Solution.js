function solution(input) {
    let wrappingPaper = Number(input[0]);
    let fabricRolls = Number(input[1]);
    let glueLitres = Number(input[2]);
    let discount = Number(input[3])/100;

    let wrappingPaperPrice = wrappingPaper*5.80;
    let fabricRollsPrice = fabricRolls*7.20;
    let gluePrice = glueLitres*1.20;
    let totalPrice = wrappingPaperPrice+fabricRollsPrice+gluePrice;

    let finalPrice = totalPrice - totalPrice*discount;
    console.log(finalPrice.toFixed(3));
}

solution(["2",
    "3",
    "2.5",
    "25"])
;