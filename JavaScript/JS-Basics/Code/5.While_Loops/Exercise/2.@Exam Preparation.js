function solution(input) {
    let badGrades = Number(input[0]);
    let index=1;
    let data=input[index];      // Name of the book
    index++;
    let grade=input[index];     // Grade
    let failureNumber=0;
    let sum=0;
    let grades=0;
    let lastTask=data;

    while(data!=="Enough"){
        if(Number(grade)<=4){
            failureNumber++;
            if(failureNumber>=badGrades){
                console.log(`You need a break, ${failureNumber} poor grades.`)
                return;
            }
        }
        grades+=Number(grade);
        lastTask=data;
        index++;
        data = input[index];
        index++;
        grade=input[index];
        sum++;
    }

    console.log(`Average score: ${(grades/sum).toFixed(2)}`)
    console.log(`Number of problems: ${sum}`)
    console.log(`Last problem: ${lastTask}`)
}

solution(["3",
    "Money",
    "6",
    "Story",
    "4",
    "Spring Time",
    "5",
    "Bus",
    "6",
    "Enough"]);