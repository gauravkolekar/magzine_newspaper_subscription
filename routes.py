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

@app.route('/magazines', methods=['GET', 'POST'])
def magazines():
    if request.method == 'GET':
        return render_template('magazines.html')

@app.route('/daily_newspapers', methods=['GET', 'POST'])
def daily_newspapers():
    if request.method == 'GET':
        return render_template('daily_newspapers.html')

@app.route('/weekly_newspapers', methods=['GET', 'POST'])
def weekly_newspapers():
    if request.method == 'GET':
        return render_template('weekly_newspapers.html')
