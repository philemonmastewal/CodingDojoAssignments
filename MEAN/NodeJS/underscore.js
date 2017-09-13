var _ = {
   map: function(array, callback) {
     //code here;
     for(var x = 0; x < array.length; x++){
       array[x] = callback(array[x]);
     }
     return array;
   },

   reduce: function(array, callback, memo) {
     for(var x = 0; x < array.length; x++){
       memo = callback(memo, array[x]);
     }
    return memo;
   },

   find: function(array, callback, value) {
     var result;
     for(var x = 0; x < array.length; x++){
       result = callback(array[x], value);
       if(result == value) {
         break;
       }
     }
    return result;
   },

   filter: function(array, callback) {
     var result = []
     for(var x = 0; x < array.length; x++){
       var i = callback(array[x]);
       if(i) {
         result.push(i);
       }
     }
    return result;
   },

   reject: function(array, callback) {
     var result = []
     for(var x = 0; x < array.length; x++){
       var i = callback(array[x]);
       if(!i) {
         result.push(array[x]);
       }
     }
    return result;
   }
}
// you just created a library with 5 methods!
arr = [1,2,3,4,5,6,7,8,9,10,2,2,2]
// console.log(_.map(arr, function (num){ return num * 3;}));
// console.log(_.reduce(arr, function(memo, num){ return memo + num; }, 0));
// console.log(_.find(arr, function(num, val){ if( num == val ){ return num; }; }, 2));
// console.log(_.filter(arr, function(num){ if(num % 2 == 0){ return num } }));
console.log(_.reject(arr, function(num){ return num % 2 == 0 }));
