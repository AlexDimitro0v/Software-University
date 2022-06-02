function solution(input) {
    let index = 0;
    let openTabs = Number(input[0]);
    index++;
    let salary = Number(input[1]);
    index++;

    for (let i = 0; i < openTabs; i++) {
        let website = input[index]
        index++;
        if(website==="Facebook"){
            salary -= 150;
        }
        else if(website==="Instagram"){
            salary -= 100;
        }
        else if(website==="Reddit"){
            salary -= 50;
        }
        if(salary<=0){
            console.log("You have lost your salary.");
            return;
        }
    }
    console.log(Math.trunc(salary))
}

solution();