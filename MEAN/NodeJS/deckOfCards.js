function DeckConstructor(){
  var suits = ["Hearts", "Spades", "Clubs", "Diamonds"];
  var values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"];
  var deck;

  this.show = function(){
    console.log(deck);
    console.log("Length:", deck.length);
    return this;

  }

  var generateDeck = function(){
    deck = [];
    for (var i = 0; i < suits.length; i++){
      for (var j = 0; j < values.length; j++){
        var card = {};

        // card.suit = suits[i]; //creates key value pair if it doesnt exist, and will overwrite it if it does
        // card.value = values[j];
        //  // var card = {
        // //         suit: suits[i],
        // //         value: values[j],
        //  // }
        card = new Card(suits[i], values[j]);
        deck.push(card);
      }
    }
  }
  generateDeck();

  this.shuffle = function(){
    var numberOfShuffles = Math.floor((Math.random()*100) + 50);
    for (var i = 0; i <= numberOfShuffles; i++){
      var randInt1 = Math.floor(Math.random() * deck.length);
      var randInt2 = Math.floor(Math.random() * deck.length);
      var temp = deck[randInt1];
      deck[randInt1] = deck[randInt2];
      deck[randInt2] = temp;
    }
    return this;
  }
  this.reset = generateDeck;

  this.getDeck = function(){
    return deck;
  }
}

DeckConstructor.prototype.deal = function(){
  return this.getDeck().pop();
}

//Card Constructor
function Card(suit, value){
  // card = {}; we could have this
  this.suit = suit;
  this.value = value;
  // return card;   then this... but instead we can use 'this' and the key word 'new' w/(Card)
}
var myDeck = new DeckConstructor();
myDeck.show().shuffle().show().deal();
myDeck.deal();
myDeck.deal();
myDeck.show();
