frrom flask import Flask, render_template  # Import Flask to allow us to create our app. Also have to make sure to add render_template if you want to return it later
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
@app.route('/')          # The "@" symbol designates a "decorator" which       attaches the following
                         # function to the '/' route. This means that whenever we send a request to
                         # localhost:5000/ we will run the following "hello_world" function.
def hello_world():
  return render_template("index.html", name="Philemon")  # This will load the template.

app.run(debug=True)      # Run the app in debug mode.
