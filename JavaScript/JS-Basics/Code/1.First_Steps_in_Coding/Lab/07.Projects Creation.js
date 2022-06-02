function solution(input) {
    let name = input[0];
    let projectsNumber = Number(input[1]);
    let totalHoursNeeded = projectsNumber*3
    console.log(`The architect ${name} will need ${totalHoursNeeded} hours to complete ${projectsNumber} project/s.`)
}

solution();