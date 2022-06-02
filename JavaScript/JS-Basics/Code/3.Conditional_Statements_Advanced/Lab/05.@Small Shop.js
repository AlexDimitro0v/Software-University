function solution(input) {
    let product = input[0];
    let city = input[1];
    let quantity = Number(input[2]);
    let finalPrice;     // LET is used as block-scoped within the function, can be updated
    // In the index.ts file in IKARUS, you can see that VAR is used as a global-scoped
    // variable that is updated within multiple functions

    if(product === "coffee"){
        if(city==="Sofia"){
            finalPrice = quantity * 0.50
        }
        else if(city==="Plovdiv"){
            finalPrice = quantity * 0.40
        }
        else if(city==="Varna"){
            finalPrice = quantity * 0.45
        }
    }

    else if(product === "water"){
        if(city==="Sofia"){
            finalPrice = quantity * 0.80
        }
        else if(city==="Plovdiv"){
            finalPrice = quantity * 0.70
        }
        else if(city==="Varna"){
            finalPrice = quantity * 0.70
        }
    }

    else if(product === "beer"){
        if(city==="Sofia"){
            finalPrice = quantity * 1.20
        }
        else if(city==="Plovdiv"){
            finalPrice = quantity * 1.15
        }
        else if(city==="Varna"){
            finalPrice = quantity * 1.10
        }
    }

    else if(product === "sweets"){
        if(city==="Sofia"){
            finalPrice = quantity * 1.45
        }
        else if(city==="Plovdiv"){
            finalPrice = quantity * 1.30
        }
        else if(city==="Varna"){
            finalPrice = quantity * 1.35
        }
    }

    else if(product === "peanuts"){
        if(city==="Sofia"){
            finalPrice = quantity * 1.60
        }
        else if(city==="Plovdiv"){
            finalPrice = quantity * 1.50
        }
        else if(city==="Varna"){
            finalPrice = quantity * 1.55
        }
    }

    console.log(finalPrice);
}

solution(["coffee", "Varna", "2"]);