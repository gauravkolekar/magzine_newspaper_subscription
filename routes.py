from flask import render_template
from runserver import app
from database_configuration import database_configuration as db
#from database_configuration import cursor as cur

@app.route('/')
@app.route('/index')
def index():
    cur = db.cursor()
    cur.execute("SELECT VERSION()")
    data = str(cur.fetchone())
    db.close()
    return render_template('index.html', sqlversion=data)
