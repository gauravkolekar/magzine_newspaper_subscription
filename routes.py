import MySQLdb
from runserver import app
from flask import g
from database_configuration import database_configuration as db
from database_configuration import cursor as cur

@app.route('/')
def index():
    cur.execute("SELECT VERSION()")
    data = cur.fetchone()
    db.close()
    return 'Hello World! This website uses mysql: '+str(data)
