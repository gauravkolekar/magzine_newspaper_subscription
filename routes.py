from flask import render_template
from runserver import app
from database_configuration import database_configuration as db

@app.route('/')
@app.route('/index')
def index():
    cur = db.cursor()
    cur.execute("SELECT VERSION();")
    data = str(cur.fetchone())
    #db.close()
    return render_template('index.html', sqlversion=data)

@app.route('/add_magazine')
def add_magazine():
    #cur = db.cursor()
    #cur.execute()
    #data = str(cur.fetchone())
    #db.close()
    return render_template('add_magazine.html')
