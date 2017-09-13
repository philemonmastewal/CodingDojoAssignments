from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re
import bcrypt
import md5

EMAILREGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9._-]+.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key= "catdogfish"
mysql = MySQLConnector(app,"theWall")


'''map out the project first, like a storyboard'''
    #Login|Registration
        #routes -> login/registration page ... you can have thos as opposed to *
        #Login
            #routes
                #route to the page to login ->GET  *
                #route to handle my login -> POST
                    #validations
        #Registration
            #routes
                #route to the page to register ->GET *
                #route to handle my login -> POST

    #The message board
        #messages
        #commenrs


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    #do i need to go to the DB
        #what do i need to do before I go into the DB
        #what data do I need to go to the DB
    #request.form -> everytime we get data we need to see if its clean, (make sure no sql injections possible)
        #validation
    #query = ""
    #data = {}
    #mysql.query_db()
    #what do i need to do before i exit this
        #should i reroute
        #should i send data to the view
    queryValid = "SELECT * FROM users WHERE email = :one"
    data={
        "one":request.form["email"]
        }
    emailResult = mysql.query_db(queryValid, data)
    #we are constructing this query to see if someone is attempting to register using an email address that already exists...below we will compare emailresult with request.form["email"],which is the submitted email address. if the result is empty that should prove that the submitted email is not already in the DB

    fname=request.form["first_name"]
    lname=request.form["last_name"]
    email=request.form["email"]
    pword=md5.new(request.form["password"]).hexdigest();
    cpword=md5.new(request.form["confirm_password"]).hexdigest();
    #below we will check if any of these blocks are empty
    #We will set up a flag to see if anythig was tripped so if it is it is set to false and we will know where and we wont send an improper request to the database flag can be called whatever we will call it validation

    isValid=True
    if(len(fname)== 0 or len(fname) > 45):
        print "invalid fname"
        flash("first name has to between 1 and 45 characters")
        isValid=False #this means if their is an error it will set the Flag to false
    elif not fname.isalpha(): #isalpha is a built in method for strings that will check to see that each character is an alphabetical character
        print "invalid fname"
        flash("Name must be alphabetical only")
        isValid=False
    if(len(lname)==0 or len(lname) > 45):
        print "invalid lname"
        flash("Last name has to between 1 and 45 characters")
        isValid=False
    elif(not lname.isalpha()): #isalpha is a built in method for strings that will check to see that each character is an alphabetical character
        flash("Last name must be alphabetical only")
        isValid=False
    if(len(email)==0):
        flash("email cannot be blank")
        isValid=False
    elif not EMAILREGEX.match(email):
        flash("email has to be in john@doe.com")
        isValid=False
    elif (emailResult!=[] ):
        flash("There is already a user registered with this email address")
        isValid=False
    if(len(pword)<8):
        flash("password must be at least 8 characters")
        isValid=False
    if(not cpword):
        flash("confirmation cannot be blank")
        isValid=False
    if(not cpword == pword):
		flash("confirmation does not match password")
		isValid = False
    #the regex object was built above and then its passed the email and will see if their is a match
    #if not EMAILREGEX.match(email) we should move this into the if block above and add an elif
    #if nothing went wrong isValid should be true
    if isValid:
        query = "INSERT INTO `thewall`.`users` (`first_name`, `last_name`, `email`, `password`, `created_at`) VALUES (:one, :two, :three, :four, now())"
        data = {
        "one":fname,
        "two":lname,
        "three":email,
        "four":pword
        }
        print mysql.query_db(query,data)
        flash("Successful Registration")
    return redirect('/')
    #     return "got to database"
    # else:
    #     return "invalid"
    #
    #
    # return "Register route"

@app.route('/login', methods=['POST'])
def login():
    email=request.form["email"]
    pword=md5.new(request.form["password"]).hexdigest()
    isValid = True;

    if(len(email)==0):
        flash("email cannot be blank")
        isValid=False
    elif not EMAILREGEX.match(email):
        flash("email has to be in john@doe.com")
        isValid=False
    if(len(pword)<8):
        flash("password must be at least 8 characters")
        isValid=False

    if isValid:
        query = "SELECT * FROM users WHERE email = :one LIMIT 1"
        data = {
            "one":email
        }

        result = mysql.query_db(query,data)
        session['user'] = result
        print session['user']
        if result == []:
            flash("nobody here with that email") #this test will see if that email is in the db
            print "Result is empty"
            return redirect('/')
        else:
            user = result[0]
            if md5.new(request.form["password"]).hexdigest() == pword:
                flash('successful login')
                session["logged_id"] = user["id"]
                session["logged_name"] = user["first_name"]
                print "Logged in"
                return redirect('/dashboard')
            else:
                flash("wrong password")
                return redirect('/')
        #print result #this will let u see what your getting back
        # print result[0]
        # return str(result[0])
    #return "Login Route" #this will let u know u have successfully gone through to here
    else:
        return redirect('/')
@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
    messages_query = "SELECT messages.id, first_name, last_name, message_content, messages.created_at FROM messages JOIN users ON users.id = messages.user_id ORDER BY messages.id DESC" #this will show all messages created, then the join will filter based on the one connected to the user id
    comments_query = "SELECT comments.message_id, first_name, last_name, comments.comment, comments.created_at FROM comments JOIN users ON users.id = comments.user_id ORDER BY comments.id DESC"

    result1 = mysql.query_db(messages_query)
    result2 = mysql.query_db(comments_query)

    return render_template("dashboard.html", messages = result1, comments=result2, name = session["logged_name"])
@app.route("/messages", methods=['POST'])#WE KNOW POST IS FOR SENDING INFO WHICH MEANS THIS route will be used to create a message - RESTful
def createMessage():
    message = request.form['message']
    query = "INSERT INTO messages (user_id, message_content, created_at, updated_at) VALUES (:one, :two, NOW(), NOW())"

    data = {
        "one":session['logged_id'],
        "two":message
    }
    # user_id/:one = session["user"][0][id] #this will remember which user is posting but above it is logged_id
    print mysql.query_db(query,data)
    return redirect("/dashboard")

@app.route("/messages/<message_id>/comments", methods=['POST'])
def createComment(message_id):

    query = "INSERT INTO comments (comment, created_at, updated_at,message_id,user_id) VALUES (:one, now(), now(), :two, :three);"
    data = {
        "one":request.form['comment'],
        "two":message_id,
        "three":session['logged_id']
    }

    mysql.query_db(query,data)
    return redirect('/dashboard')


app.run(debug=True)
