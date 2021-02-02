from flask import Flask,render_template,request,session,redirect
from flask_session import Session

#inform flask to make the name of the file(application.py) as the flask application
app=Flask(__name__)

app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)


Gender=["Male","Female","Other"]
Volunteers={}

@app.route("/")
def index():
    if not session.get("name"):
        return redirect("/login")
    else:
        return render_template("index.html")

@app.route("/register", methods=["POST"])
def greet():
    return render_template("index.html", name =request.form.get("name","My Mind"))

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
        session["name"]=request.form.get("Username")
        print(session.values)
        return redirect("/")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session["name"]=None
    return redirect("/")