from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
app =  Flask(__name__)
app.secret_key = "tuna"
mysql = MySQLConnector(app,'full_friends')

@app.route('/')#This route will: Display all of the friends on the index.html page
def index():
    query = "SELECT * from users"
    #above we are creating a variable for the string we want to pass into mySQLworkbench
    friends = mysql.query_db(query)
    #Above we have created another variable, "friends", which will run the query that you have passed into mysql.query_db(),<--"query", on the DB, when you connect to the DB you want to send it a SQL command....so you could have even written mysql.query_db("SELECT * from users"), but using variables is simpler, and SO the variable "friends" will hold everything that is returned from the query, mysql.query_db()
    return render_template('index.html', showFriends = friends)
    #Above we do showFriends = friends to so that we can pass any of the info from friends in the python server, to the html and display it whenever we call "{{showFriends}}" in the index.html file ..... we do this because Flask wants us to name whatever we pass through, which is why initially we did friends=friends and it was still fine just a little confusing

@app.route('/friends', methods = ["POST"])# This route will: Handle the add friend form submit and create the friend in the DB
def createFriend(): #this function will run the same query as the one you type into mySQLworkbench so you can just copy it below
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name,  :email, NOW(), NOW())"
    #primary keys are set to auto increment so it will know what row it is on, so we dont have to keep track of that
    #VALUES must be labeled the names you gave them in the index.html file so it can know to pull from what people type in
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    #request.form will hold what people type into the input with the coressponding name, and pass what the they type as the data, above
    #now we actually have to run it, so we will do that below
    #You are goint to pass in the query string we labeled above as well as the data that is above.
    #the mysql object from the mysqlconnection.py is what will go through the info and put it together for us and run that query
    mysql.query_db(query, data)
    #Then we want to display what ever was inputed so we should redirect to the first rooute with the index.html file so it can display what is in list: because that is what def index() will do for us- it will query the DB and passover a dictionary with the results

    return redirect('/')

#
#below the flask syntax is < > which is why we have <user_id>, as oppossed to the double curly braces used in the index.html file, {{friend['id']}}...everytime we hit the edit button we want it to come here,below, for the corressponding id
@app.route('/friends/<user_id>/edit',methods = ["GET"])# This route will:Display the edit friend page for the particular friend, we want to use a separate html file called edit.html, which will display the particular user we want to edit and then allow us to tweak that user on the edit page but making sure the changes we make goes all the way back to the DB, so the changes will be consistent through out
def edit(user_id):
    query = "SELECT * FROM users WHERE id = :user_id"

    # the colon before user_id above,:, is a signifier to mysqlconnection.py letting it know that user_id is somethig that must be interpolated from the data, and it is going to look for a key value that matches user_id
    # this will protect us from sql injection, which is where a malicious user could decide to use the inspect function to alter the what is being sent through this route and although you can refresh the page and your display may be fine, the request they made will still go through and alter info in your DB.. just by using this notation SQLAlchemy is protecting us from any sql statements that are trying to be submitted
    # only the <user_id> corresponds with the one inside def edit()and the one at the end of data, the two remaining correspond with each other, the one after id =, and the first one in data
    data = {
    "user_id": user_id
    }
    # Then to get an individual user you will query and check their primary key because it is always unique for each single user, below it will get us a single user, or nothing if their is nothing with the corresponding primary key

    single_friend = mysql.query_db(query, data)
    # below we need to make sure to pass in the parameters and let the system know that friend will be single_friend
    return render_template("edit.html",friend = single_friend)
#
@app.route('/friends/<user_id>', methods=["POST"])# This route will:Handle the edit friend form submit and update the friend in the DB
def update(user_id):
    query = "UPDATE  users SET first_name = :first_name, last_name = :last_name, email = :email, updated_at= NOW() WHERE id = :user_id"
    #dont need to change created at, just updated at
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "user_id" : user_id
    }
    mysql.query_db(query, data)
    # print request.form <--this is to show what is being passed
    return redirect('/')


@app.route('/friends/<user_id>/delete', methods= ["POST"])# This route will: Delete the friend from the DB
def delete(user_id):
    query = "DELETE FROM users WHERE id = :user_id"#<-this doesnt coorelate to the user_id above, it coorelates with the key in our dictionary, the first one below in data
    data = {
        "user_id": user_id #<-and this one coorelates to the other two, the one in the route between friends & delete, and with the one inside def delete()

    }
    mysql.query_db(query, data)

    return redirect('/')


app.run(debug=True)
