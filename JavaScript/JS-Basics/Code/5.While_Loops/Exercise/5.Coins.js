function solution(input) {
    let returnMoney = Math.floor(Number(input[0])*100);
    let coins=0;

    while(returnMoney>0){
        coins+=1;

        if(200<returnMoney){
            returnMoney-=200;
        }
        else if(100<=returnMoney){
            returnMoney-=100;
        }
        else if(50<=returnMoney){
            returnMoney-=50;
        }
        else if(20<=returnMoney){
            returnMoney-=20;
        }
        else if(10<=returnMoney){
            returnMoney-=10;
        }
        else if(5<=returnMoney){
            returnMoney-=5;
        }
        else if(2<=returnMoney){
            returnMoney-=2;
        }
        else if(1<=returnMoney){
            returnMoney-=1;
        }
    }

    console.log(coins)
}

solution(["0.56"]);