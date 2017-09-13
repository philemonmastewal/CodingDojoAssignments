var express      = require('express'),
    path         = require('path'),
    mongoose     = require('mongoose'),
    bodyParser   = require('body-parser'),
    port         = 3500,
    app          = express();

app.use(bodyParser.urlencoded());
app.set('views', path.join(__dirname,'./views'));
app.set('view engine', 'ejs');

mongoose.connect('mongodb://localhost/messageBoard', function(err, db){
  if(err){
    console.log("error w/ mongoose.connect");
    console.log(err);
  }
});
var Schema = mongoose.Schema;
var MessageSchema = new Schema({
  name: String,
  message: String,
  _comments: [{type: Schema.Types.ObjectId, ref: 'Comment'}]
});

MessageSchema.path('name').required(true, 'Name cannot be blank');
MessageSchema.path('message').required(true, 'Message cannot be blank');

mongoose.model("Message", MessageSchema);

var Message = mongoose.model("Message");

var CommentSchema = new mongoose.Schema({
  name: String,
  text: String,
  _message: {type: Schema.Types.ObjectId, ref: 'Message'}
});
CommentSchema.path('name').required(true, 'Name cannot be blank');
CommentSchema.path('text').required(true, 'Comment cannot be blank');

mongoose.model("Comment", CommentSchema);

var Comment = mongoose.model("Comment");

//these 2^^ can be put together var Comment=mongoose.model("Coment",CommentSchema)

//set up routes below


app.get("/", function(req, res){
  Message.find({}, false, true).populate('_comments').exec(function(err, results){
    res.render('index', { messages: results });
  });
});


app.post("/message", function(req, res){
  var newMessage = new Message({ name: req.body.name, message: req.body.message });
  newMessage.save(function(err){
    if(err){
      console.log(err);
      res.render('index', { errors: newMessage.errors });
    } else {
      console.log("success");
      res.redirect('/');
    }
  })
})


app.post("/comment/:id", function(req, res){
  var message_id = req.params.id;
  Message.findOne({ _id: message_id }, function(err, message){
    var newComment = new Comment({ name: req.body.name, text: req.body.comment });
    newComment._message = message._id
    Message.update({ _id: message._id }, {$push: {"_comments": newComment}}, function(err){

    });
    newComment.save(function(err){
      if(err){
        console.log(err);
        res.render('index', {errors: newComment.errors});
      } else {
        console.log("comment added");
        res.redirect("/");
      }
    });
  });
});





app.listen(3500, function(){
  console.log("server now running on port :3500");
});
