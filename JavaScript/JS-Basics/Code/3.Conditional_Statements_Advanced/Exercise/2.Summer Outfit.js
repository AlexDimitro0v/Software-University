function solution(input) {
    let degreesCelsius = Number(input[0]);
    let dayTime = input[1];
    let outfit;
    let shoes;

    switch (dayTime) {
        case "Morning":
            if(degreesCelsius>=10 && degreesCelsius <= 18){
                outfit = "Sweatshirt";
                shoes = "Sneakers";
            }
            else if(degreesCelsius>18 && degreesCelsius <= 24){
                outfit = "Shirt";
                shoes = "Moccasins";
            }
            else if(degreesCelsius>=25){
                outfit = "T-Shirt";
                shoes = "Sandals";
            }
            break;
        case "Afternoon":
            if(degreesCelsius>=10 && degreesCelsius <= 18){
                outfit = "Shirt";
                shoes = "Moccasins";
            }
            else if(degreesCelsius>18 && degreesCelsius <= 24){
                outfit = "T-Shirt";
                shoes = "Sandals";
            }
            else if(degreesCelsius>=25){
                outfit = "Swim Suit";
                shoes = "Barefoot";
            }
            break;
        case "Evening":
            if(degreesCelsius>=10 && degreesCelsius <= 18){
                outfit = "Shirt";
                shoes = "Moccasins";
            }
            else if(degreesCelsius>18 && degreesCelsius <= 24){
                outfit = "Shirt";
                shoes = "Moccasins";
            }
            else if(degreesCelsius>=25){
                outfit = "Shirt";
                shoes = "Moccasins";
            }
            break;
    }

    console.log(`It's ${degreesCelsius} degrees, get your ${outfit} and ${shoes}.`)
}

solution();