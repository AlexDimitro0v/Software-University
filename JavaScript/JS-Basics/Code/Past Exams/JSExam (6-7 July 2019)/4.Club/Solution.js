function solution(input) {
    let desiredWinning = Number(input[0]);
    let totalPrice = 0;
    let index = 1;

    while (input[index]!=="Party!") {
        let cocktail = String(input[index]);
        index ++;
        let cocktailNumber = Number(input[index]);

        let cocktailPrice = cocktail.length*cocktailNumber;
        if (cocktailPrice % 2 === 1) {
            cocktailPrice = cocktailPrice - cocktailPrice*25/100;
        }

        totalPrice += cocktailPrice;
        index ++;
    }

    if (totalPrice>=desiredWinning) {
        console.log("Target acquired.");
    }
    else {
        console.log(`We need ${(Math.abs(totalPrice-desiredWinning)).toFixed(2)} leva more.`);
    }

    console.log(`Club income - ${(totalPrice).toFixed(2)} leva.`);
}

solution(["100", "Sidecar", "7", "Mojito", "5", "White Russian", 10, "Party!"]);