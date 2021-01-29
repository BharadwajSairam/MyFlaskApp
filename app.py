from flask import Flask,render_template,request

#inform flask to make the name of the file(application.py) as the flask application
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def greet():
    return render_template("greet.html", name =request.form.get("name","My Mind"))