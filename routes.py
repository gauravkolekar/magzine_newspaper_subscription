from flask import render_template, request, url_for
from runserver import app
from database_configuration import database_configuration as db

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        cur = db.cursor()
        cur.execute("SELECT VERSION();")
        data = str(cur.fetchone())
        #db.close()
        return render_template('index.html', sqlversion=data)
    elif request.method == 'POST':
        user_name = request.form['name']
        user_address = request.form['address']
        print user_name, user_address
        if request.form['submit'] == 'Submit':
            return render_template('subscription.html')

@app.route('/add_magazine', methods=['GET','POST'])
def add_magazine():
    if request.method == 'GET':
        return render_template('add_magazine.html')
