function VehicleConstructor(name, wheels, passengers){
  var vehicle = {};

  vehicle.name = name || "motorcycle"  // pipes are there to set a default
  vehicle.wheels = wheels || 2;
  vehicle.passengers = passengers || 1;

  vehicle.makeNoise = function(noise){
    var noise = noise || "Honk Honk";
    console.log(noise)
  }
  return vehicle;
}
var Bike = VehicleConstructor("Bike", 2, 1);
Bike.makeNoise = function(){
  console.log("Ring Ring!")
}
console.log(Bike);
Bike.makeNoise();

var Sedan = VehicleConstructor("Sedan", 4, 4);
Sedan.makeNoise = function(){
  console.log("Honk HOnk HOnk!")
}
console.log(Sedan);
Sedan.makeNoise();


var Bus = VehicleConstructor("Bus", 8, 1);
Bus.pickUpPassengers = function(newPassengers){
  Bus.passengers += newPassengers
}
console.log(Bus);
console.log(Bus.passengers);
console.log(Bus.pickUpPassengers(14));
console.log(Bus.passengers);
console.log(Bus);
