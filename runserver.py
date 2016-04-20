from flask import Flask
#importing Flask from flask

app = Flask(__name__)

from routes import *
#from routes2 import *
#importing all the routes functions from the route file

if __name__ == '__main__':
    app.run(debug=True)
