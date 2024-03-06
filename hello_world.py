# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def xyz():
#     return 'welcome'
# @app.route('/admin')
# def hello_admin():
#     return "HELLO admin"
# @app.route('/guest/<guest>')
# def hello_guest(guest):
#     return "welcome %s" % guest
# @app.route('/user/<name>')
# def hello_user(name):
#     if name == 'admin':
#         return redirect(url_for('hello_admin'))
#     else:
#         return redirect(url_for('hello_guest', guest=name))
# if __name__== '__main__':
#             app.run(debug = True)
#
# @app.route('/app')
# def hello():
#     return 'HELLO'
# @app.route('/')
# def hi():
#     return 'HI'
# @app.route('/hello/<name>')
# def hello_name(name):
#     return f'HELLO{name}'
# if __name__=='__main__':
#     app.run()
from flask import Flask, redirect, url_for, request,render_template
app = Flask(__name__)
@app.route("/home")
def fun():
    addition = 10 + 100
    return render_template("home.html",result = addition)
if __name__ =="__main__":
    app.run(debug=True)

