function solution(input) {
    let n = Number(input[0]);
    let p1=0;
    let p2=0;
    let p3=0;
    let p4=0;
    let p5=0;

    for (let i = 1; i <=n; i++) {
        let number = Number(input[i])
        if(number<200){
            p1+=1
        }
        else if(number>=200 && number<=399){
            p2+=1
        }
        else if(number>=400 && number<=599){
            p3+=1
        }
        else if(number>=600 && number<=799){
            p4+=1
        }
        else if(number>=800){
            p5+=1
        }
    }
    console.log(`${(p1/n*100).toFixed(2)}%`)
    console.log(`${(p2/n*100).toFixed(2)}%`)
    console.log(`${(p3/n*100).toFixed(2)}%`)
    console.log(`${(p4/n*100).toFixed(2)}%`)
    console.log(`${(p5/n*100).toFixed(2)}%`)
}

solution(["7", "800", "801", "250", "199", "399", "599", "799"]);