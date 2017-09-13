import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Dojo Mail';

  emails = [
    { email: "George@Washington.com", importance : true, subject: "USA", content:"I was the first president" },
    { email: "Curious@George.com", importance : true, subject: "Bananas", content:"I am a monkey" },
    { email: "Steve@Jobs.com", importance : true, subject: "Apples", content:"I lie macbooks" },
    { email: "Bob@bob.com", importance : false, subject: "Bob", content:"I am bob" }

  ]

}
