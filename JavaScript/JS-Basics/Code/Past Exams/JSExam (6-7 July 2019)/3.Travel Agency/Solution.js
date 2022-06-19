function solution(input) {
    let city = input[0];
    let package = input[1];
    let isVIP = input[2];
    let stay = Number(input[3]);
    let price = 0;

    if (stay < 1){
        console.log("Days must be positive number!");
        return;
    }

    switch (city) {
        case "Bansko":
        case "Borovets":
            switch (package) {
                case "withEquipment":
                    price = 100 * stay;
                    if (isVIP === "yes"){
                        price -= price * (10/100)
                    }
                    break;
                case "noEquipment":
                    price = 80 * stay;
                    if (isVIP === "yes"){
                        price -= price * (5/100)
                    }
                    break;
                default:
                    console.log("Invalid input!");
                    return;
            }
            break;
        case "Varna":
        case "Burgas":
            switch (package) {
                case "withBreakfast":
                    price = 130 * stay;
                    if (isVIP === "yes"){
                        price -= price * (12/100)
                    }
                    break;
                case "noBreakfast":
                    price = 100 * stay;
                    if (isVIP === "yes"){
                        price -= price * (7/100)
                    }
                    break;
                default:
                    console.log("Invalid input!");
                    return;
            }
            break;
        default:
            console.log("Invalid input!");
            return;
    }
    console.log(`The price is ${price.toFixed(2)}lv! Have a nice time!`)
}

solution();