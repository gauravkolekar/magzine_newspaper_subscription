from runserver import app
from database_configuration import database_configuration as db
#using the database configuration to execute SQL statements

cur = db.cursor()
# creating a cursor object to execute queries on the database

cur.execute("SELECT VERSION()")
# query to find out the database version

data = cur.fetchone()
# Fetch a single row using fetchone() method.

db.close()
#disconnect from database

@app.route('/')
def index():
    return 'Hello World! This website uses mysql: '+str(data)
