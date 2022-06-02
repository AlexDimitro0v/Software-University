function solution(input) {
    let month = input[0];
    let nightsStay = Number(input[1]);
    let studioPrice;
    let apartmentPrice;

    switch(month){
        case "May":
        case "October":
            studioPrice = nightsStay * 50;
            apartmentPrice = nightsStay * 65;
            if (nightsStay>14){
                studioPrice = studioPrice-studioPrice*(30/100);
            }
            else if(nightsStay>7){
                studioPrice = studioPrice-studioPrice*(5/100);
            }
            break;
        case "June":
        case "September":
            studioPrice = nightsStay * 75.20;
            apartmentPrice = nightsStay * 68.70;
            if(nightsStay>14){
                studioPrice = studioPrice-studioPrice*(20/100);
            }
            break;
        case "July":
        case "August":
            studioPrice = nightsStay * 76;
            apartmentPrice = nightsStay * 77;
            break;
    }

    if(nightsStay>14){
        apartmentPrice = apartmentPrice-apartmentPrice*(10/100);
    }

    console.log(`Apartment: ${apartmentPrice.toFixed(2)} lv.`)
    console.log(`Studio: ${studioPrice.toFixed(2)} lv.`)

}

solution();