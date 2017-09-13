var express      = require('express'),
    path         = require('path'),
    mongoose     = require('mongoose'),
    bodyParser   = require('body-parser'),
    port         = 8000,
    app          = express();


// Express basic setup
app.use(bodyParser.urlencoded({ extended: true}));
app.use(express.static(path.join(__dirname, './static')));
app.set('views', path.join(__dirname,'./views'));
app.set('view engine', 'ejs');


//Connect to db
mongoose.connect('mongodb://localhost/messageBoard');

//Need schema variable
//var Schema = mongoose.Schema; <-- u can write this and then remove mongoose from the mongoose.Schema below

// Create message schema
var MessageSchema = new mongoose.Schema({
    name: { type: String, required: true, minlength: 4 }
    content: { type: String, required: true}
    comments: [{ type: Schema.Types.ObjectId, ref: "Comment" }]
}, {timestamps: true});

//Create Comments Schema
var CommentSchema = new Schema({
  _message: {type: Schema.Types.ObjectId, ref: 'Message'},
  name: {type: String, required: true, minLength: 4},
  content: {typr: String, required: true}
},{timestamps: true});


//Register Models
var Message = mongoose.model('Message', MessageSchema);
var Comment = mongoose.model('Comment', CommentSchema);


//ROUTES
app.get('/', function(req, res){
  Message.find({})
  .populate('comments')
  .exec(function(err, results){
    if (err){ console.log(err); }
    console.log(results);
    res.render('index', { messages: results });
  });
});


app.post('/message', function(req, res){
  Message.create(req.body, function(err, result){
    if (err){ console.log(err); }
    res.redirect('/');
  })
})


app.post('/messages/:id?comments' function(req, res){
  // find message the comment will belong to
  Message.findOne({_id: req.params.id}, function(err, message){
    // create a comment using data from form-group
    var comment = new Comment(req.body);
    //set the reference like this
    comment._message = message._id;
    //the comment now belogns to the message we found above
    //now save both to the database
    comment.save(function(err){
      //push the comment into the comments array of the message we found
      message.comments.push(comment);
      //save the updated message
      message.save(function(err){
        if (err){ console.log(err);}
        else{
          res.redirect('/');
        }
      })
    })
  })
})


//settnug our server to listen to port
app.listen(port, function(){
  console.log("listening on port", port);
});
