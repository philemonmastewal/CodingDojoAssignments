import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  title = 'Initial Power Level:';
  power;
  saiyanPower;
  superSaiyanPower;
  superSaiyan2Power;
  superSaiyan3Power;
  superSaiyan4Power;

  onSubmit(){
    this.saiyanPower = this.power * 10;
    this.superSaiyanPower = this.power * 90;
    this.superSaiyanTwoPower = this.power * 150;
    this.superSaiyanThreePower = this.power * 250;
    this.superSaiyanFourPower = this.power * 500;
  }
}
