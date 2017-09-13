function VehicleConstructor(name, wheels, passengers, speed){
  if(!(this instanceof VehicleConstructor)){
    return new VehicleConstructor(name, wheels, passengers, speed)
  }
  var distanceTraveled = 0;
  var self = this;
  function updateDistanceTraveled(){
    distanceTraveled += self.speed;
    console.log(distanceTraveled);
  }

  this.speed = speed;
  this.name = name || "motorcycle";  // pipes are there to set a default
  this.wheels = wheels || 2;
  this.passengers = passengers || 1;

  this.makeNoise = function(noise){
    var noise = noise || "Honk Honk";
    console.log(noise)
  };
  this.move = function(){
    this.makeNoise();
    updateDistanceTraveled();
  };
  this.checkMiles = function(){
    console.log(distanceTraveled);
  };
}
var Bike = new VehicleConstructor("Bike", 2, 1, 100);

Bike.move();
Bike.move();
Bike.move();
Bike.move();


Bike.checkMiles();

console.log(Bike.speed);
