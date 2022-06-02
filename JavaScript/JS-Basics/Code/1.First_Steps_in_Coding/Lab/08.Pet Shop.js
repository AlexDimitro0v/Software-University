function solution(input) {
    let dogsFood = Number(input[0]);
    let catsFood = Number(input[1]);

    let totalPrice = dogsFood*2.50+catsFood*4
    console.log(`${totalPrice} lv.`)
}

solution(["13", "9"]);
