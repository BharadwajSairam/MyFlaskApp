from flask import Flask,render_template,request

#inform flask to make the name of the file(application.py) as the flask application
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", name =request.args.get("name"))
