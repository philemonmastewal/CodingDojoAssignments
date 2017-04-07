function DoubleAmount(DollarAmount, days) {
    var total = DollarAmount;
    var i = 1;
    while(i < days && days > 1){
        total += total;
        i++;
    }
    return total;
}
console.log(DoubleAmount(0.01, 30))



var penny = .01;

for (var i = 1; i < 31; i++){
  penny *= 2;
  if(penny > 10000){
    break;
  }
}
console.log(penny,"it would take", i, "days to make over $10,000");
