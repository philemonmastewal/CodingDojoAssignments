# -GET
# SELECT * FROM users #this will give back everythin in users DB
# @
# -GET
# -POST
# -UPDATE
# -DELETE
from flask import Flask
app = Flask(__name__)

@app.route('/users', methods=['GET'])
def indexUsers():
    pass
@app.route('/users/new', methods=['GET'])     #new just shows the form to create a new form
def newUser()
    pass
@app.route('/users', methods=['POST'])
    pass
@app.route('/users/<id>', methods=['GET'])
    pass
@app.route('/users/<id>', methods=['POST'])
    pass
@app.route('/users/<id>/edit', methods=['GET'])
    pass

app.run(debug=True)

|||||||||||||||||||||||||||||

from flask import Flask
app = Flask(name)
@app.route('/users', methods=['GET'])
def index():
    query = "SELECT * FROM users"
@app.route('/users', methods=['POST'])
def create():
    query = "INSERT INTO users (first_name,last_name) VALUES ('Philemon', 'Mastewal')"
@app.route('/users/<id>', methods=['GET'])
def show():
    query = "SELECT * FROM users WHERE usersid = id"
@app.route('/users/<id>', methods=['POST'])
def update():
    query = "INSERT INTO (first_name,last_name) VALUES ('Thomas', 'Jefferson') WHERE usersid = id  "
@app.route('/users/<id>/delete', methods=[''])
def delete():
@app.route('/users/new', methods=['GET'])
def new(): #just to show the create page
    pass
@app.route('/users/<id>/edit', methods=['GET'])
def edit(): #just to show the update page
    pass
app.run(debug=true)
