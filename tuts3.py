from flask import Flask,make_response,session,redirect,abort

app=Flask(__name__)

# @app.route('/')
# def fun():
#     res=make_response("<h1>THis is BHavin Panchal</h1>")
#     res.set_cookie("answer","42")
#     return res
# @app.route('/')
# def fun():
#     return redirect("https://www.google.com")
@app.route('/user/<id>')
def fun(id):
    user=load_user(id)
    if not user:
        abort(404)
    return "<h1>Hello %s</h1>" %user.name





if __name__=="__main__":
    app.run(debug=True)