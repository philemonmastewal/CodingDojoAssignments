from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "burrito"

#count += 1 on refresh
#count += 2 on button
#count reset on reset button



@app.route("/")
def index():
    print session
    if "counter" in session:
        session['counter'] += 1
    else:
        session['counter'] = 0

    return render_template("index.html")

@app.route("/count", methods=["POST"])
def count():
    # plus two to count
    session['counter'] += 1
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    # session['counter'] = 0
    session.clear()    #either will work^or down
    #session.pop("counter")
    return redirect("/")

app.run(debug=True)
