# from flask import Flask,redirect, url_for
# app = Flask("first_app") # 


# @app.route("/")
# def index():
    # return "Hello"

# @app.route("/home")
# def home():
	# return "<h1> Home</h1>"

#app.run("0.0.0.0",8000)
# @app.route("/hello")
# def hello():
    # return '<h2 style="color:red">Hello World!<h2>'

# @app.route("/world")
# def world():
    # return redirect(url_for('hello'))
    # 
# app.run("0.0.0.0",7999)
#app.add_url_rule("/","hello",hello)

from flask import Flask,redirect,url_for
app=Flask('first app')

@app.route('/')
def index():
    return('hello')
@app.route('/hello')
def hello():
    return '<h2 style="color:red">Hello World!<h2>'
@app.route('/world')
def world():
    return redirect(url_for('hello'))
app.run("0.0.0.0",7999)
    
    
    

    
 





