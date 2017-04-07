from flask import Flask, render_template, redirect, session, request
from random import randint

app = Flask(__name__)
app.secret_key = "tacocat"

@app.route("/") #localhost:5000
def index():
    # session.clear() <-- this will test if its 0 or 1 and if gold is in here

    if 'gold' in session:
        pass
    else:
        session['gold'] = 0

    return render_template("index.html")

@app.route("/process", methods=['POST']) #localhost:5000/process
def process():
    if request.form['building'] == "house":
        found_gold = randint(2,5) #second number is included
        print found_gold
        session['gold'] += found_gold
        print "at the house"
    if request.form['building'] == "farm":
        found_gold = randint(10,20) #you can set session['gold ']
        session['gold'] += found_gold
        print "at the farm"

    return redirect("/")   #this will redirect back to localhost:5000

@app.route("/reset")
def reset():
    session.clear()
    print "Your session has been reset"
    return redirect("/")

app.run(debug=True)
