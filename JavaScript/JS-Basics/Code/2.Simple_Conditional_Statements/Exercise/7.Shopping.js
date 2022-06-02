function solution(input) {
    let budgetPetar = Number(input[0]);
    let videoCards = Number(input[1]);
    let processors = Number(input[2]);
    let RAM = Number(input[3]);

    let videoCardsPrice = videoCards*250;
    let processorsPrice = videoCardsPrice*0.35*processors;
    let RAMPrice = videoCardsPrice*0.10*RAM;

    let totalPrice = videoCardsPrice + processorsPrice + RAMPrice;
    if (videoCards > processors) {
        totalPrice = totalPrice - totalPrice*0.15
    }
    let difference = Math.abs(totalPrice-budgetPetar);

    if (totalPrice>budgetPetar){
        console.log(`Not enough money! You need ${difference.toFixed(2)} leva more!`);
    }
    else {
        console.log(`You have ${difference.toFixed(2)} leva left!`)
    }
}

solution(["920.45", "3", "1", "1"]);