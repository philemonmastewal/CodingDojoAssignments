var quarters = 100;
function randomChance(quarters) {
  var win = 50;
  while (quarters > 0) {
    if(win == Math.floor(Math.random()*100)+1){
      quarters += Math.floor(Math.random()*50)+51;
      quarters -= 1;
      console.log(quarters);
    }
    else {
          quarters -= 1;
          if(quarters == 0){
              console.log(quarters);
          }
    }
  }
}
randomChance(23);
