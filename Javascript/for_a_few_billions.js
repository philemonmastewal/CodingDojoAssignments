function DoubleAmount(DollarAmount, days) {
    var total = DollarAmount;
    var i = 0;
    while(i < days && days > 0){
        total += total;
        i++;
    }
    return total;
}
console.log("The reward after 30 days would be",DoubleAmount(0.01, 30))



var penny = .01;

for (var i = 1; i < 31; i++){
  penny *= 2;
  if(penny > 10000){
    break;
  }
}
console.log("It would take", i, "days to make over $10,000. The exact amount earned after",i,"days, would be",penny);
