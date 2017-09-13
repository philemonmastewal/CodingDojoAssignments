import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  quotes= [
    { body: 'I never am really satisfied that I understand anything; because, understand it well as I may, my comprehension can only be an infinitesimal fraction of all I want to understand about the many connections and relations which occur to me.', author: 'Ada Lovelace', rating: 25 },
    { body: 'fsd', author: 'durrrr', rating: 72 }
  ];

  createQuote(quote){
    console.log(quote);
    this.quotes.push(quote);
  }
  deleteQuote(quote){
    const idx = this.quotes.indexOf(quote);
    this.quotes.splice(idx, 1);
  }

}
