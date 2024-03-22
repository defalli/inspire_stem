// Dta types:
/*//multiple comment in javascript
    1. String, 
     2. Integers/Numbers,
      3.Booleans,
      4 Arrays
      5 0bjects
*/
let name = "ian";
let height = 50

function submit(){
var input  = document.getElementById("input field").Value;

var inout = input + 1;
var input = parseInt(input);//Data type Conversion
console.log(typeof(height))
}

let adult = true;// boolean Datatype
let fruits = ['kiwi','apple','mango', 30 ,false]// Array or a list
let person = {
    firstname:'Ada'
    lastname:'kiwi'
    age: 18,
    address: (
        country: ' sudan'
        city:'khartoum'
        street:'bani bani'
    ),
    children:['kelly','Mary']

}
function saveItem(){
    var input = document.getElementById("inputfield").Value
    localstorage.setItem( 'inputItem',inputField);
    showWelcomMessage(inputField);
}
function showWelcomeMessage(inputField){
    var messageElement =document.getElementById("showmessage")
    messageElement.textContent= "we have saved ypur input as"+inputField
}Item = local.getItem
var storedItem = local.storage.getItem("inputfield")
if(storedItem){
    showWelcomeMessage(storedItem)
}