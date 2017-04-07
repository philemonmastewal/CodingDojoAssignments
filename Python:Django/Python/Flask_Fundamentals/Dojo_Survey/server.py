from flask import Flask, render_template, redirect, request, flash, url_for
app = Flask(__name__)
app.secret_key="tacocat"


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():

    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comments = request.form['comments']

    print "Name:",name
    print "Location:",location
    print "Favorite Language:",language
    print "Comments:",comments
    #


    return render_template("result_index.html", name = name, location = location, language = language, comments = comments)




app.run(debug=True)
