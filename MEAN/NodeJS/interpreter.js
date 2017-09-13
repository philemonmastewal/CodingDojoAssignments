
//PROBLEM

console.log(first_variable);
var first_variable = "Yipee I was first!";
function firstFunc() {
  first_variable = "Not anymore!!!";
  console.log(first_variable);
}
//ANSWER
console.log(first_variable);
var first_variable;
function firstFunc(){
  first_variable = "Not anymore!!!";
  console.log(first_variable);
}
console.log(first_variable);
// no data has been assigned to first_variable, so shows as console logs undefined.
first_variable = "Yipee I was first!";
console.log(first_variable);
// Yipee I was first was assigned to first_variable, so that is what is logged.


//PROBLEM

var food = "Chicken";
function eat() {
  food = "half-chicken";
  console.log(food);
  var food = "gone";       // CAREFUL!
  console.log(food);
}
eat();
console.log(food);

//ANSWER

var food; // Declare an outer scope food variable
function eat() {
  var food;
  food = "half-chicken";
  console.log(food); // half-chicken console.log, since there is a LOCAL food
  food = "gone";       // CAREFUL! LOCAL food is set to gone
  console.log(food); // LOCAL food is logged ('gone')l
}
food = "Chicken"; //outer food is set to "chicken"
eat(); // eat is invoked and the half_chicken and gone are logged (the local foods!)
console.log(food); // outer food is logged('chicken')
 /

//PROBLEM
var new_word = "NEW!";
function lastFunc() {
  new_word = "old";
}
console.log(new_word);


//ANSWER


var new_word; //outer scope new_word variable
function lastFunc(){
 new_word = 'old'; // still references the outer scope new_word variable
}
new_word = "NEW!";
console.log(new_word); //lastFunc wasn't invoked so console.log's "New"
