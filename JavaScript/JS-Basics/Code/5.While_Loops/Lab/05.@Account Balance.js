function solution(input) {
    let data = input[0];
    let money = 0;
    let index=1;
    while(data!=="NoMoreMoney"){
        if(Number(data)<0){
            console.log("Invalid operation!");
            break;
        }
        money+=Number(data);
        console.log(`Increase: ${Number(data).toFixed(2)}`)
        data = input[index];
        index++;
    }
    console.log(`Total: ${money.toFixed(2)}`);
}

solution(["120",
    "45.55",
    "-155"]);