var express = require("express");
var bodyParser  =require('body-parser');

var app = express(); // app is an application so it can run methods like get&post

app.use(express.static(__dirname + "/static"));
// // console.log(__dirname); to see what its form-group

app.use(bodyParser.urlencoded({ extended: true }));

app.set('views', __dirname + '/views');
//this will set the location for where express will look for the ejs views

app.set('view engine', 'ejs');
//this will set the view engine itself so that express knows that we are using ejs as opposed to another templating engine... like jade


app.get('/', function(request, response){
  response.send("Hello Express"); // this will send to response, that string
})

app.get("/users", function(request, response){
  //we will hard-code user data this time
  var users_array = [
    { name: "Philemon", email: "philemon@email.com" },
    { name: "Tyson", email: "Tyson@email.com" },
    { name: "Stuart", email: "Stuart@email.com" },
    { name: "Bill", email: "Bill@email.com" },
  ];

app.get("/users/:id", function (req, res){
  console.log("The user id requested is:", req.params.id);
  //this is to illustrate that you can use req.params here(above)
  res.send("You requested the user with id;" + req.params.id);
  //code to get user from db goes here, etc...
});

app.post('/users', function (req, res){
  console.log("Post Data \n\n", req.body)
  res.redirect('/')
});
response.render('users', { users: users_array });
  //we are passing a JavaScript object to the response.render() method. This way when we pass a piece of data to a view, every key-value pair within the larger piece of data becomes its own variable.
})


// weve handled our route but we havent told our application to listen anywhere yet...so
app.listen(7000, function(){
  console.log("listening on port 7000");
});


// this line will almost always be at the end of your server.js file (we only tell the server to listen after we have set up all of our rules)
















//from platform--
// First, we need to require the Express module:
//
// // Load the express module (Where do you think this comes from?)
// var express = require("express");
// Next, we are going to invoke the function returned to the express variable. Requiring "express" returns a "CreateApplication" function that we store in the express variable before we invoke it.
//
// // invoke var express and store the resulting application in var app
// var app = express();
// Now that we have created our express app, let's use it to handle requests:
//
// // let's handle the base route "/" and respond with "Hello Express"
// app.get('/', function(request, response) {
//   response.send("<h1>Hello Express</h1>");
// })
// // notice that the function is app.get(...) why do you think the function is called get?
// We have loaded the express module into our server file, invoked it to create the server itself, and created a route for the server to handle. Now we just have to tell the server to listen!
//
// // Tell the express app to listen on port 8000
// app.listen(8000, function() {
//   console.log("listening on port 8000");
// })
// // this line will almost always be at the end of your server.js file (we only tell the server to listen after we have set up all of our rules)
// Woohoo! You just created the server in your first Express app!
