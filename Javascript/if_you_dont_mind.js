// If You Dont Mind Can I Have The Time?


var HOUR = 8;
var MIN = 50;
var PERIOD = "AM";

function whatTimeIsIt(hour,min,period){

  if (period== "AM"){
    var p="in the morning";

  }
  else{
    var p="in the evening";
  }


  if (min>30){
  var m="It's almost";
  }
  else{
  var m="It's just after";
  }

  if (min>30){
    hour+=1;
  }
  else{
    var h=hour;
  }

  var h=hour

  return m+" "+h+" "+p;
//
}
var result=whatTimeIsIt(HOUR,MIN,PERIOD)

console.log(result);
