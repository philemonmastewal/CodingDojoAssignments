var x = [3,5,"Dojo","rocks","Michael","Sensei"]
for(i=0;i<x.length;i++){
  console.log(x[i]);
}
x.push(200);
console.log(x);

// Push another arr to arr x
x.push(["hello", "world", "JavaScript is Fun"]);

console.log(x);

// Print all the sum of numbers from 1-500
var sum = 0;
for (var i = 1; i < 501; i++) {
  sum += i;
}
console.log(sum);


// Find minimum value of following arr
var arr = [1,5,90,25,-3,0];

var min = arr[0];
for (var i = 1; i < arr.length; i++) {
  if (arr[i] < min){
    min = arr[i];
  }
}
console.log(min);

// Find average value of arr
var sum = arr[0];
for (var i = 1; i < arr.length; i++) {
    sum  += arr[i];
}
console.log(sum/arr.length);

// Iterate through object
var new_ninja = {
  name: 'Jessica',
  profession: 'coder',
  favorite_language: 'JavaScript',
  dojo: 'Dallas'
};

for (var key in new_ninja){
  console.log(key + " : " + new_ninja[key]);
}
