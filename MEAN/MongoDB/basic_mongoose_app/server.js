// Require the Express Module
var express = require('express');
// Create an Express App
var app = express();
// Require body-parser (to receive post data from clients)
var bodyParser = require('body-parser');
// Integrate body-parser with our App
var mongoose = require('mongoose');
//Check the order of everything related to mongoose (require^ --> connect --> Schema --> Model --> route)

// This is how we connect to the mongodb database using mongoose -- "basic_mongoose" is the name of
//   our db in mongodb -- this should match the name of the db you are going to use for your project.
mongoose.connect('mongodb://localhost/basic_mongoose');

var UserSchema = new mongoose.Schema({
  first_name:  { type: String, required: true, minledngth: 6},
  last_name: { type: String, required: true, maxlength: 20 },
  age: { type: Number, min: 1, max: 150 },
  email: { type: String, required: true }
}, {timestamps: true });

mongoose.model('User', UserSchema); // We are setting this Schema in our Models as 'User'
var User = mongoose.model('User') // We are retrieving this Schema from our Models, named 'User'


app.use(bodyParser.urlencoded({ extended: true }));
// Require path
var path = require('path');
// Setting our Static Folder Directory
app.use(express.static(path.join(__dirname, './static')));
// Setting our Views Folder Directory
app.set('views', path.join(__dirname, './views'));
// Setting our View Engine set to EJS
app.set('view engine', 'ejs');
// Routes
// Root Request

// // The root route -- we want to get all of the users from the database and then render the index view passing it all of the users
// app.get('/', function(req, res) {
//   User.find({}, function(err, users) {
//     // This is the method that finds all of the users from the database
//     // Notice how the first parameter is the options for what to find and the second is the
//     //   callback function that has an error (if any) and all of the users
//     // Keep in mind that everything you want to do AFTER you get the users from the database must
//     //   happen inside of this callback for it to be synchronous
//     // Make sure you handle the case when there is an error, as well as the case when there is no error
//   })
// })




app.get('/', function(req, res) {
  // This is where we will retrieve the users from the database and include them in the view page we will be rendering.
  User.find({}, function(err, users){
      //if there is an error console.log that something went wrong
      if(err){
        console.log('something went wrong');
      }else{ //else console.log that we did well and then redirect to the root route
        console.log('successfully added a user!');
        res.render('index', {users: users});
      }
  })
})
// Add User Request
// This is the route that we already have in our server.js
// When the user presses the submit button on index.ejs it should send a post request to '/users'.  In
//  this route we should add the user to the database and then redirect to the root route (index view).
app.post('/users', function(req, res) {
 console.log("POST DATA", req.body);
 //create new User with the name and age corresponding to those from req.body
 var user = new User(req.body);
 // This is where we would add the user from req.body to the database.
 // Try to save that new user to the database (this is the method that actually inserts into the db) and run a callback function with an error (if any) from the operation.
  user.save(function(err){
    //if there is an error console.log that something went wrong
    if(err){
      console.log('something went wrong');
      res.render('index', {title: 'you have errors!', errors: user.errors})
    }else{ //else console.log that we did well and then redirect to the root route
      console.log('successfully added a user!');
      res.redirect('/');
    }
  })
})

// There is a lot that is happening in the code above, make sure that you understand everything that is going on. A few key points:
//
// notice that "User" is actually an object constructor (notice the _"new" keyword). The "User"_, which constructs user objects, have methods that talk to the database!
// ".save" is the method that actually inserts into the database.
// ".save" takes a callback function that has an error parameter so that we know whether or not the insert was successful (these callback functions really do come up everywhere in JS huh?). This is a pattern that you'll see often -- any method that interacts with the database will typically have a callback function as a parameter (the callback function will run when the database operation finishes).
//

// Setting our Server to Listen on Port: 7000
app.listen(7000, function() {
    console.log("listening on port 7000");
})
