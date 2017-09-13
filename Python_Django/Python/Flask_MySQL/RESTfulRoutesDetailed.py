from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
# Create a class [below]that will give us an object that we can use to connect to a database
class MySQLConnection(object):
    def init(self, app, db):
        config = {
                'host': 'localhost',
                'database': db, # we got db as an argument
                'user': 'root',
                'password': 'root',
                'port': '3306' # change the port to match the port your SQL server is running on
        }
    # this will use the above values to generate the path to connect to your sql database
    DATABASE_URI = "mysql://{}:{}@127.0.0.1:{}/{}".format(config['user'], config['password'], config['port'], config['database'])
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    # establish the connection to database
    self.db = SQLAlchemy(app)
# this is the method we will use to query the database
def query_db(self, query, data=None):
    result = self.db.session.execute(text(query), data)
    if query[0:6].lower() == 'select':
        # if the query was a select
        # convert the result to a list of dictionaries
        list_result = [dict(r) for r in result]
        # return the results as a list of dictionaries
        return list_result
    elif query[0:6].lower() == 'insert':
        # if the query was an insert, return the id of the
        # commit changes
        self.db.session.commit()
        # row that was inserted
        return result.lastrowid
    else:
        # if the query was an update or delete, return nothing and commit changes
        self.db.session.commit()
This is the module method to be called by the user in server.py. Make sure to provide the db name!
def MySQLConnector(app, db):
    return MySQLConnection(app, db)
#====================================================================================================#
app = Flask(name)
mysql = MySQLConnector(app, "restful_demo")
@app.route('/users', methods=['GET'])
def index():
    query = "SELECT  from users"
    users = mysql.query_db(query)
    return render_template('index.html')
@app.route('/users', methods=['POST'])
def create():
    query = "INSERT INTO users (first_name, last_name, created_at, updated_at) VALUES (:one, :two, now(), now())"
    data = {
        "one":request.form["first_name"],
        "two":request.form["last_name"]
    }
    result = mysql.query_db(query, data)
    return redirect('/users')
@app.route('/users/<id>', methods=['GET'])
def show(id):
    query = "SELECT  FROM users where id=" + id
    return render_template('show.html')
@app.route('/users/<id>', methods=['POST'])
def update(id):
    query = "UPDATE users SET first_name=:one, last_name=:two, updated_at=now() WHERE id=:three"
    data = {
        "one":request.form["first_name"],
        "two":request.form["last_name"],
        "three":id
    }
    result = mysql.query_db(query, data)
    return redirect('/users/'+id)
@app.route('/users/<id>/delete', methods=["POST"])
def delete(id):
        query = "DELETE FROM table where id = " + id
        result = mysql.query_db(query)
        return redirect('/users')
@app.route('/users/new', methods=['GET'])
def new(): #just to show the create page
        return render_template('new.html')
@app.route('/users/<id>/edit', methods=['GET'])
def edit(id): #just to show the update page
        return render_template('edit.html', user_id=id)
app.run(debug=True)
