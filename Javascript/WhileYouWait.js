// Create a birthday countdown

var daysUntilMyBirthday = 23;

function whileYouWait(daysUntilMyBirthday) {

    if(daysUntilMyBirthday>30) {
      console.log("Oh no",daysUntilMyBirthday,"days until my brthday.That's such a long time");
    }
    if(daysUntilMyBirthday < 30 && daysUntilMyBirthday >=5){
      console.log("Yay",daysUntilMyBirthday, "days until my birthday, its almost here.");
    }
    if(daysUntilMyBirthday<5 && daysUntilMyBirthday>0) {
      console.log("Oh yeah! my birthday's going to be here in",daysUntilMyBirthday,"days.");
    }
    if (daysUntilMyBirthday===0){
      console.log("Wow, it's finally my birthday!");
    }
}
whileYouWait(daysUntilMyBirthday);
