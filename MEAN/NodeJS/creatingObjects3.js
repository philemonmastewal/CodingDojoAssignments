function VehicleConstructor(name, wheels, passengers, speed){
  if(!(this instanceof VehicleConstructor)){
    return new VehicleConstructor(name, wheels, passengers, speed)
  }
  //create a string of characters to create a vin number
  var characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

  this.distanceTraveled = 0;
  this.speed = speed;
  this.name = name || "motorcycle";  // pipes are there to set a default
  this.wheels = wheels || 2;
  this.passengers = passengers || 1;

  this.vin = createVin();

  function createVin(){
    var vin = "";
    for (var i= 0; i < 17; i++){
      //generate random index for characters
      vin += characters[Math.floor(Math.random()*35)];
    }
    return vin;
  }
}



VehicleConstructor.prototype.makeNoise = function(noise){
  var noise = noise || "Honk Honk";
  console.log(noise);
  return this;
};

VehicleConstructor.prototype.move = function(){
  this.makeNoise();
  this.updateDistanceTraveled();
  return this;
};

VehicleConstructor.prototype.checkMiles = function(){
  console.log(this.distanceTraveled);
  return this;
};

VehicleConstructor.prototype.updateDistanceTraveled = function(){
  this.distanceTraveled += this.speed;
  console.log(this.distanceTraveled);
  return this;
}

var Bike = new VehicleConstructor("Bike", 2, 1, 100);

Bike.move();
Bike.move();
Bike.move();
Javascript


Bike.checkMiles();

console.log(Bike.speed);
