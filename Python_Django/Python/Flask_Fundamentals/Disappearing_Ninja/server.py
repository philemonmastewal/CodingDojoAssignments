from flask import Flask, render_template, redirect, request
app = Flask(__name__)
app.secretkey= "dogs"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninjas():
    Flag = True
    return render_template('ninja.html', Flag = Flag)

@app.route('/ninja/<color>')
def ninjacolor(color):
    Flag = False

    return render_template('ninja.html', color = color, Flag = Flag)


app.run(debug=True)
