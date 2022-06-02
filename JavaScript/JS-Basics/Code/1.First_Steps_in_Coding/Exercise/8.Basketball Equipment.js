function solution(input) {
    let yearlyFee = Number(input[0])

    let basketballShoes = yearlyFee - yearlyFee*40/100;
    let basketballSuit = basketballShoes - basketballShoes*20/100;
    let ball = 1/4 * basketballSuit;
    let accessories = 1/5 * ball;

    let totalSum = yearlyFee + basketballShoes + basketballSuit + ball + accessories
    console.log(totalSum)
}

solution(["365"]);