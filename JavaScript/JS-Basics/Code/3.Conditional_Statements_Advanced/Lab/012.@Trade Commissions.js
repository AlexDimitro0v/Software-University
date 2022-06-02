function solution(input) {
    let city = input[0];
    let sales = Number(input[1]);
    let tradeCommission;

    // return to escape/break a function
    if(city==="Sofia"){
        if(sales>=0 && sales<=500){
            tradeCommission = sales * (5/100)
        }
        else if(sales>500 && sales<=1000){
            tradeCommission = sales * (7/100)
        }
        else if(sales>1000 && sales<=10000){
            tradeCommission = sales * (8/100)
        }
        else if(sales>10000){
            tradeCommission = sales * (12/100)
        }
        else{
            console.log("error")
            return;
        }
    }
    else if(city==="Varna"){
        if(sales>=0 && sales<=500){
            tradeCommission = sales * (4.5/100)
        }
        else if(sales>500 && sales<=1000){
            tradeCommission = sales * (7.5/100)
        }
        else if(sales>1000 && sales<=10000){
            tradeCommission = sales * (10/100)
        }
        else if(sales>10000){
            tradeCommission = sales * (13/100)
        }
        else{
            console.log("error")
            return;
        }
    }
    else if(city === "Plovdiv"){
        if(sales>=0 && sales<=500){
            tradeCommission = sales * (5.5/100)
        }
        else if(sales>500 && sales<=1000){
            tradeCommission = sales * (8/100)
        }
        else if(sales>1000 && sales<=10000){
            tradeCommission = sales * (12/100)
        }
        else if(sales>10000){
            tradeCommission = sales * (14.5/100)
        }
        else{
            console.log("error")
            return;
        }
    }
    else{
        console.log("error")
        return;
    }
    console.log(tradeCommission.toFixed(2))
}

solution();