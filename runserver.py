from flask import Flask, session
#importing Flask from flask


app = Flask(__name__)

app.secret_key = 'db1'

from routes import *
#importing all the routes functions from the route file

if __name__ == '__main__':
    app.run(debug=True)
