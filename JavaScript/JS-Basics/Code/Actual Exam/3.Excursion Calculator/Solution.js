function solution(input) {
    let people = Number(input[0]);
    let season = input[1];
    let price = 0;

    switch (season) {
        case "spring":
            if (people <= 5){
                price = 50 * people;
            }
            else if (people > 5){
                price = 48 * people;
            }
            break;

        case "summer":
            if (people <= 5){
                price = 48.50 * people;
            }
            else if (people > 5){
                price = 45 * people;
            }
            break;

        case "autumn":
            if (people <= 5){
                price = 60 * people;
            }
            else if (people > 5){
                price = 49.50 * people;
            }
            break;

        case "winter":
            if (people <= 5){
                price = 86 * people;
            }
            else if (people > 5){
                price = 85 * people;
            }
            break;
    }

    if (season === "summer"){
        price = price - price * (15/100);
    }
    else if (season === "winter"){
        price = price + price * (8/100);
    }

    console.log(`${price.toFixed(2)} leva.`)
}

solution(["15",
    "autumn"]);