from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key='bingo'

import random

@app.route('/')
def index():
    if 'randomNum' in session:
        pass
    else:
        session['randomNum'] = random.randrange(0,101)
    print session['randomNum']
    return render_template('index.html')

@app.route('/number', methods=['POST'])
def number():
    print request.form['guess']

    if session['randomNum'] == int(request.form['guess']):
        print "THAT'S THE RIGHT NUMBER"
        return render_template('index_win.html', win="Great Job! That's the right number.")
    elif session['randomNum'] < int(request.form['guess']):
        print 'too high'
        return render_template('index.html', highguess="Sorry, your guess was too high.")
    elif session['randomNum'] > int(request.form['guess']):
        print 'too low'
        return render_template('index.html', lowguess="Sorry, your guess was too low.")
@app.route('/win', methods=['POST'])
def win():
    session.pop('randomNum')
    return redirect('/')


app.run(debug=True)
