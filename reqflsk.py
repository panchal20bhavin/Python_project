from flask import request,Flask

app=Flask(__name__)

@app.route("/")
def fun():
    user = request.headers.get("us")
    return "<h1>Your is %s</h1>" % user

if __name__=="__main__":
    app.run(debug=True)



   
   