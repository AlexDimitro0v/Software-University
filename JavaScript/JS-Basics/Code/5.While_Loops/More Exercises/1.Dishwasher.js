function solution(input) {
    let data = input[0];
    let detergent = Number(data)*750
    let index=1;
    let counter=0;
    let washedDishes=0;
    let washedPots=0;
    while(true){
        data=input[index++];
        let washedVessel = Number(data);
        if(data==="End"){
            break;
        }
        counter++;
        if (counter===3){
            detergent -= washedVessel*15;
            counter = 0;
            washedPots+=washedVessel;
        }
        else{
            detergent -= washedVessel*5;
            washedDishes+=washedVessel;
        }
        if (detergent < 0){
            console.log(`Not enough detergent, ${Math.abs(detergent)} ml. more necessary!`);
            return;
        }
    }
    console.log(`Detergent was enough!`);
    console.log(`${washedDishes} dishes and ${washedPots} pots were washed.`);
    console.log(`Leftover detergent ${detergent} ml.`);
}

solution(["2", "53", "65", "55", "End"]);