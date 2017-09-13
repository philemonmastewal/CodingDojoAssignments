import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  time = new Date();
  timezone = null;
  color = "yellow"

  getTime(selectedTimezone){
    this.time = new Date();
    if(selectedTimezone === 'PST'){
      this.time.setHours(this.time.getHours);
    } else if (selectedTimezone === 'MST'){
      this.time.setHours(this.time.getHours + 1);
    } else if (selectedTimezone === 'CST'){
      this.time.setHours(this.time.getHours + 2);
    } else if (selectedTimezone === 'EST'){
      this.time.setHours(this.time.getHours + 3);
    } else if (selectedTimezone === 'clear'){
      this.time.setHours(this.time.getHours + 3);
    }
    this.timezone = selectedTimezone;
  }
}


  clear(){
  this.timezone = [];
  }

}
