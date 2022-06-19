function solution(input) {
    let shirtPrice = Number(input[0]);
    let n = Number(input[1]);

    let shortsPrice = shirtPrice*0.75;
    let socksPrice = shortsPrice*0.20;
    let shoesPrice = (shirtPrice+shortsPrice)*2;
    let totalPrice = shirtPrice+shortsPrice+socksPrice+shoesPrice;
    let discountedPrice = totalPrice-totalPrice*(15/100);

    if (discountedPrice >= n){
        console.log("Yes, he will earn the world-cup replica ball!");
        console.log(`His sum is ${discountedPrice.toFixed(2)} lv.`);
    }
    else{
        console.log("No, he will not earn the world-cup replica ball.");
        console.log(`He needs ${Math.abs(discountedPrice-n).toFixed(2)} lv. more.`)
    }
}

solution(["55",
    "310"]);