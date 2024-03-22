let input = document.getElementById("input box");
let buttons=document.querySelectorAll("button");//gives as an array(stores multiple values)

let string = "";
let arr = Array.from(buttons)

arr.forEach( button=> {
    button.addEventListeners('click',(e)=>{
        if(e.target.innerHTML == "="){
            string = string = eval(string);
            input.value= string;
        }else if(e.target.innerHTML == "AC"){
            string = "";
            input.value = string;
        }else if(e.target.innerHTML == "DEL"){
            string = string.substring(0,string.length-1);
            input.value = string;
        }else{
            string +=e.target.innerHTML;
            input.value = string;
        }
    })
})

