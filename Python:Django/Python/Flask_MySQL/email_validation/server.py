from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = 'philemon'
mysql = MySQLConnector(app,'emailvalid')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():

	return render_template('index.html')

@app.route('/submit', methods=['POST'])
def create():

    if len(request.form['email']) < 1:
        flash('You must submit an email address')
	if not EMAIL_REGEX.match(request.form['email']):
		flash('Invalid email address!')
		return redirect('/')

	query = "INSERT INTO email (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"

	data = {
             'email': request.form['email'],
           }

	mysql.query_db(query, data)

	posting = 'SELECT * FROM email'
	emailData = mysql.query_db(posting)
	success = str(request.form['email'])
	flash('The email address you entered ' + success + ' is a VALID email address! Thank you!')

	return render_template('/success.html', info = emailData)

app.run(debug=True)
