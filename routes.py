from flask import render_template, request, url_for, redirect
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
        user_name = str(request.form['name'])
        user_address = str(request.form['address'])
        #cur = db.cursor()
        #cur.execute('''INSERT INTO CUSTOMER VALUES(%s,%s)''', (user_name, user_address))
        #db.commit()
        print user_name, user_address
        if request.form['submit'] == 'Submit':
            return redirect(url_for('subscription'))

@app.route('/subscription')
def subscription():
    return render_template('subscription.html')

@app.route('/add_magazine', methods=['GET','POST'])
def add_magazine():
    if request.method == 'GET':
        return render_template('add_magazine.html')
    elif request.method == 'POST':
        magazine_name = str(request.form['magazine_name'])
        magazine_frequency = str(request.form['magazine_frequency'])
        magazine_editor_name = str(request.form['magazine_editor'])
        print magazine_name, magazine_frequency, magazine_editor_name
        if request.form['submit'] == 'Submit':
            return redirect(url_for('index'))

@app.route('/magazines', methods=['GET', 'POST'])
def magazines():
    if request.method == 'GET':
        cur = db.cursor()
        cur.execute("SELECT * FROM MAGAZINE;")
        data = str(cur.fetchall())
        return render_template('magazines.html', all_data=data)

@app.route('/daily_newspapers', methods=['GET', 'POST'])
def daily_newspapers():
    if request.method == 'GET':
        return render_template('daily_newspapers.html')

@app.route('/weekly_newspapers', methods=['GET', 'POST'])
def weekly_newspapers():
    if request.method == 'GET':
        return render_template('weekly_newspapers.html')
