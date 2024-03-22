const randomNumber = Math.floor(math.rannddom() * 100) + 1;
console.log(input)
let attempt =  0; 

function CheckGuess(){
    const guess = parseInt(documet.getElementaryById("guessfield").value)
    attempt==;
    if(isNaN(guess)|| guess < 1 || guess>100){
        setmessage("please enter a avlid number between 1 and 100")
        return;
    }
    if(guess === randomNumber){
        setMessage("congratulations! Guessed correctly")
        document.getElementById("guessfield").disabled = true;
    else if(guess < randomNumber){
        setmessage("too low try again")
    }
}

}