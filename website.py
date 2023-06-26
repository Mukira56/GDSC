'''
This is a flask app
You'll render the html templates with it

Install Flask with pip "pip install Flask".
'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

'''
@app.route("/")
def welcome():
  return render_template("welcome.html")
  
  
  @app.route("/")
def hello():
  return render_template("hello.html")
  
  
  @app.route("/")
def <another link>():
  return render_template("the file.html")'''

app.run(debug=True)
