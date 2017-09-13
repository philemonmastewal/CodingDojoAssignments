function runningLogger(){
  console.log('I am running!');
}
function multiplyByTen(x){
  if (typeof(x) == "number"){
    return x*10;
  }
}
function stringReturnOne(){
  return "This is string #1";
}

function stringReturnTwo(){
  return "This is string #2";
}

function caller(param){
  if(typeof(param) == "function"){
    param();
  }
}

function myDoubleConsoleLog(param1,param2){
  if(typeof(param1)=="function" && typeof(param2)=="function"){
    console.log(param1(),param2())
  }
}

function caller2(param1){
  console.log("starting");
  var x = setTimeout(function(){
    if (typeof(param)=="function"){
      param(stringReturnOne, stringReturnTwo);
    }
  },2000);
  console.log('ending');
  return "interesting";
}

console.log(caller(myDoubleConsoleLog));
