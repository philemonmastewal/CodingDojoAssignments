from flask import Flask, render_template, redirect, request
app=Flask(__name__)
app.secret_key = "philemon"
@app.route('/', methods=['GET','POST'])
def index():
    return render_template ("index.html")

@app.route('/process', methods=['POST'])
def submit():
    # print "Got the name"
    # name = "name"
    name = request.form['name']

    return render_template ("result.html", viewname = name)


app.run(debug=True)
