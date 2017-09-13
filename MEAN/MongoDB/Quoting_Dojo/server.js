var express = require('express'),
    bodyParser = require('body-parser'),
    mongoose = require('mongoose'),
    path = require('path'),
    port = 3500,
    app = express();

// Set up body-parser to parse form data
app.use(bodyParser.urlencoded({extended: false}));

// Set up database connection, Schema, model
mongoose.connect('mongodb://localhost/quoting_dojo');


var QuoteSchema = new mongoose.Schema({
  name : String,
  quote : String
});

var Quote = mongoose.model('quotes', QuoteSchema);

//point the server to views
app.set('views', path.join(__dirname, './views'));
//we are using ejs as the view engine
app.set('view engine', 'ejs');

//Here are our ROUTES
app.get('/', function(req, res){
  res.render('welcome');
})

app.get('/quotes', function(req, res){
  //here we need logic to grab all the quptes and pass them into the rendered view

  Quote.find({}, function(err, results){
    if(err) { console.log(err); }
    res.render('quotes', { quotes: results });
  })
})

app.post('/quotes', function(req, res){
    console.log(req.body);
  Quote.create(req.body, function(err){
    if(err) { console.log(err); }
    res.redirect('/quotes');
  })
})
//Thats it for the ROUTES


app.listen(port, function(){
  console.log('listening on port 3500!');
});
