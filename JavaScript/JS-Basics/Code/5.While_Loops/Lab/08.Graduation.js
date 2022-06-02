function solution(input) {
    let name = input[0];
    let index=1;
    let gradesTotal=0;
    let failures=0;
    let exclusionGrade=1;

    for (let i = 1; i <= 12; i++) {
        let grade = Number(input[index]);
        if(grade<4){
            failures+=1;
            if (failures>1){
                exclusionGrade=i-1;
                break;
            }
        }
        gradesTotal+=grade;
        index++;
    }
    if (failures>1){
        console.log(`${name} has been excluded at ${exclusionGrade} grade`)
    }
    else{
        console.log(`${name} graduated. Average grade: ${(gradesTotal/12).toFixed(2)}`)
    }
}

solution(["Mimi",
    "5",
    "6",
    "5",
    "6",
    "5",
    "6",
    "6",
    "2",
    "3"])

;