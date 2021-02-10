from flask import Flask, request, render_template
from markupsafe import escape
app=Flask(__name__)

@app.route("/")
def fun1():
    return "<h1> HEllo </h1>"

@app.route("/about/<int:id1>")
def fun2(id1):
    return "Hello %d" %id1

@app.route("/home/<path:subpath>")
def fun3(subpath):
    return "subpath %s" % escape(subpath)

@app.route("/pot/")
def fun4():
    return "Hello world"

@app.route("/service", methods = ["GET","POST"])
def fun5():
    if request.form == "POST":
        return do_login
    else:
        return show.login

@app.route("/post/<id>")
def fun6(id=None):
    return render_template("hello.html", name=id)

app.run(debug=True)