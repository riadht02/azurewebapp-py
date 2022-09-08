from flask import flask
app = flask(_name_)
@app.route("/")
def hello():
 return "<h1> Hello from GTS COE azfdemo webapp!</h1>"
