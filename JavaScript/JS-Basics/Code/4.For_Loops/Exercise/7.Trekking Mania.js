function solution(input) {
    let climbers = Number(input[0]);
    let p1=0;
    let p2=0;
    let p3=0;
    let p4=0;
    let p5=0;
    let totalNumberOfPeople=0;

    for (let i = 1; i <= climbers; i++) {
        let people = Number(input[i]);
        totalNumberOfPeople += people;
        if (people<=5){
            p1+=people;
        }
        else if (people>=6 && people<=12){
            p2+=people
        }
        else if (people>=13 && people<=25){
            p3+=people
        }
        else if (people>=26 && people<=40){
            p4+=people
        }
        else if (people>=41){
            p5+=people
        }
    }

    console.log(`${(p1/totalNumberOfPeople*100).toFixed(2)}%`)
    console.log(`${(p2/totalNumberOfPeople*100).toFixed(2)}%`)
    console.log(`${(p3/totalNumberOfPeople*100).toFixed(2)}%`)
    console.log(`${(p4/totalNumberOfPeople*100).toFixed(2)}%`)
    console.log(`${(p5/totalNumberOfPeople*100).toFixed(2)}%`)
}

solution(["10", "10", "5", "1", "100", "12", "26", "17", "37", "40", "78"]);