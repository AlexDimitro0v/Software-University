function solution(input) {
    let data = input[0];
    let freeSpots = input[1];
    let index=2;
    let totalTickets=0;
    let p1=0;
    let p2=0;
    let p3=0;
    while(data!=="Finish"){
        let movie=data;
        let ticketType = input[index++];
        let movieTickets = 0;
        let availableSeats = freeSpots;
        let isFinished = false;
        while(availableSeats > 0 && ticketType!=="End"){
            availableSeats-=1;
            totalTickets+=1;
            movieTickets+=1;
            if (ticketType==="student"){
                p1+=1
            }
            else if (ticketType==="standard"){
                p2+=1
            }
            else if (ticketType === "kid"){
                p3+=1
            }
            if (availableSeats <= 0 || ticketType === "Finish"){
                isFinished = true;
                break;
            }
            ticketType=input[index++];
        }
        console.log(`${movie} - ${((movieTickets/freeSpots)*100).toFixed(2)}% full.`)
        data=input[index++];
        freeSpots=input[index++]
    }

    console.log(`Total tickets: ${totalTickets}`)
    console.log(`${((p1/totalTickets)*100).toFixed(2)}% student tickets.`)
    console.log(`${((p2/totalTickets)*100).toFixed(2)}% standard tickets.`)
    console.log(`${((p3/totalTickets)*100).toFixed(2)}% kids tickets.`)
}

solution(["Taxi",
    "10",
    "standard",
    "kid",
    "student",
    "student",
    "standard",
    "standard",
    "End",
    "Scary Movie",
    "6",
    "student",
    "student",
    "student",
    "student",
    "student",
    "student",
    "Finish"])
;