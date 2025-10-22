from flask import Flask
''''
It creates an instance of the Flask class, 
which is the WSGI application.
'''
##WSGI Application
app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to this Flask Application and it uses Flask. this is the home page."

@app.route('/index')
def index():
    return "This is the index page of this Flask Application."


if __name__ == "__main__":
    app.run(debug=True)