# Basic md5 Hashing
    # One of the most basic hashing algorithms is known as md5. Md5 is an algorithm that takes a value (most likely a password) and returns a hashed string. To see how this works, type the following into a new Python document:

import md5 # imports the md5 module to generate a hash
password = 'password';
# encrypt the password we provided as 32 character string
encrypted_password = md5.new(password).hexdigest();
print encrypted_password; #this will show you the encrypted value
# 5f4dcc3b5aa765d61d8327deb882cf99 -> nice!

# What you will see is that long string shown above. The md5 function returns a hashed version of the parameter it is passed. The md5 function yields the same value every time it is run with the same argument. That means the value it spits back is not random -- it is hashed. You may ask: why don't hackers just reverse engineer the values? Answer: the md5 algorithm is well known and solvable but it is very strong in the sense that it is not easily reverse engineered. Md5 is too insecure to be the industry standard but it is a good starting point.

# When you add your users to the database upon registration, you should save their passwords as an hashed md5 string. Similarly, when they log in, you should hash the input password to make sure it matches with the one saved in the database. Here's the idea:
#
# The user being put into your database:

import md5 # do this at the top of your file where you import modules
@app.route('/users/create', methods=['POST'])
def create_user():
     username = request.form['username']
     email = request.form['email']
     password = md5.new(request.form['password']).hexdigest();
     insert_query = "INSERT INTO users (username, email, password, created_at, updated_at) VALUES (:username,
     :email, :password, NOW(), NOW())"
     query_data = { 'username': username, 'email': email, 'password': password }
     mysql.query_db(insert_query, query_data)
#When your user is trying to log in:
password = md5.new(request.form['password']).hexdigest()
email = request.form['email']
user_query = "SELECT * FROM users where users.email = :email AND users.password = :password"
query_data = { 'email': email, 'password': password}
user = mysql.query_db(user_query, query_data)
# do the necessary logic to login if the user exists, otherwise redirect to login page with error message<br>
