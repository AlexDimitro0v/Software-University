function solution(input) {
    let days = Number(input[0]);
    let housing = input[1];
    let rating = input[2];
    let nightStay = days-1
    let totalPrice;

    switch(housing){
        case "room for one person":
            totalPrice=18*nightStay;
            break;
        case "apartment":
            totalPrice=25*nightStay;
            if(days<10){
                totalPrice = totalPrice-totalPrice*(30/100);
            }
            else if(days>=10 && days <=15){
                totalPrice = totalPrice-totalPrice*(35/100);
            }
            else if(days>15){
                totalPrice = totalPrice-totalPrice*(50/100);
            }
            break;
        case "president apartment":
            totalPrice=35*nightStay;
            if(days<10){
                totalPrice = totalPrice-totalPrice*(10/100);
            }
            else if(days>=10 && days <=15){
                totalPrice = totalPrice-totalPrice*(15/100);
            }
            else if(days>15){
                totalPrice = totalPrice-totalPrice*(20/100);
            }
            break;
    }

    switch(rating){
        case "positive":
            totalPrice = totalPrice+totalPrice*(25/100);
            break;
        case "negative":
            totalPrice= totalPrice-totalPrice*(10/100);
            break;
    }

    console.log(totalPrice.toFixed(2))
}

solution(["30", "president apartment", "negative"]);