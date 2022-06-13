function solution(input) {
    let examHour = Number(input[0]);
    let examMinute = Number(input[1]);
    let arrivingHour = Number(input[2]);
    let arrivingMinute = Number(input[3]);
    let totalMinutesExam = examHour*60+examMinute;
    let totalMinutesArrival = arrivingHour*60+arrivingMinute;
    let diff = Math.abs(totalMinutesExam-totalMinutesArrival);

    let hours = Math.floor(diff/60);
    let minutes = diff%60;

    // Being late
    if(totalMinutesArrival>totalMinutesExam){
        console.log("Late")
        if(diff < 60){
            console.log(`${minutes} minutes after the start`)
        }
        else{
            if(minutes<10){
                console.log(`${hours}:0${minutes} hours after the start`)
            }
            else{
                console.log(`${hours}:${minutes} hours after the start`)
            }
        }
    }
    else{
        if(diff<=30){
            // If the student arrives exactly on time or max 30 minutes before the exam
            console.log("On time")
        }
        else {
            console.log("Early")
        }

        if(diff===0){
            return;
        }
        else if(diff < 60){
            console.log(`${minutes} minutes before the start`)
        }
        else{
            if(minutes<10){
                console.log(`${hours}:0${minutes} hours before the start`)
            }
            else{
                console.log(`${hours}:${minutes} hours before the start`)
            }
        }
    }
}

/**
 * Extracts the hours
 * @param totalMinutes
 * @returns {number}
 */
function getHours(totalMinutes){
    return Math.floor(totalMinutes/60);
}

/**
 * Extracts the minutes
 * @param totalMinutes
 * @returns {number}
 */
function getMinutes(totalMinutes){
    return totalMinutes%60
}

solution(["9", "30", "9", "20"]);