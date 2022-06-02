function solution(input) {
    let n1 = Number(input[0]);
    let n2 = Number(input[1]);
    let operation = input[2];
    let result;

    switch(operation){
        // Ternary operator https://www.codingem.com/javascript-if-else-on-one-line/#:~:text=Writing%20a%20one%2Dline%20if,by%20using%20the%20ternary%20operator.&text=Running%20this%20code%20prints%20%E2%80%9CAdult%E2%80%9D%20into%20the%20console.&text=This%20code%20works%20fine.,by%20using%20the%20ternary%20operator.
        case "+":
            let addition = n1+n2
            result = `${n1} ${operation} ${n2} = ${addition} - ${addition%2===0 ? "even" : "odd"}`
            console.log(result);
            break;
        case "-":
            let subtraction = n1-n2
            result = `${n1} ${operation} ${n2} = ${subtraction} - ${subtraction%2===0 ? "even" : "odd"}`
            console.log(result);
            break;
        case "*":
            let multiplication = n1*n2
            result = `${n1} ${operation} ${n2} = ${multiplication} - ${multiplication%2===0 ? "even" : "odd"}`
            console.log(result);
            break;
        case "/":
            if(n2 !== 0){
                let division=n1/n2
                result = `${n1} ${operation} ${n2} = ${division.toFixed(2)}`
                console.log(result);
            }
            else{
                console.log(`Cannot divide ${n1} by zero`)
            }
            break;
        case "%":
            if(n2 !== 0) {
                let quotientDivision = n1 % n2
                result = `${n1} ${operation} ${n2} = ${quotientDivision}`
                console.log(result);
            }
            else{
                console.log(`Cannot divide ${n1} by zero`)
            }
            break;
    }
}

solution();