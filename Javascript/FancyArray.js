var arr = ["James","Jill","Jane","Jack"];
function fancyArray (arr,symbol){
  for (var i = 0; i < arr.length; i++){
    console.log(i,symbol, arr[i]);
  }
}
fancyArray(arr,"->");
