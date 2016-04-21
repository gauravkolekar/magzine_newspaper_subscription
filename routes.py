from flask import render_template, request, url_for, redirect
from runserver import app
#from database_configuration import database_configuration as db
from db_config import database_configuration as db

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
        cur = db.cursor()
        add_customer = "INSERT INTO CUSTOMER (cname, address) VALUES (%s, %s)"
        data_customer = (user_name, user_address)
        cur.execute(add_customer, data_customer)
        db.commit()
        #print user_name, user_address
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
        state_name = str(request.form['state_name'])
        rate = int(request.form['rate'])
        cur = db.cursor()
        try:
            add_magazine = "INSERT INTO MAGAZINE (pm_name , frequency, editorm_name) VALUES (%s,%s,%s)"
            data_magazine = (magazine_name,magazine_frequency,magazine_editor_name)
            cur.execute(add_magazine,data_magazine)
        except:
               pass
        add_magazine_sub_rate = "INSERT INTO magazine_subscription_rate (pm_name, state, rate) VALUES (%s,%s,%s)"
        data_magazine_sub_rate = (magazine_name,state_name,rate)
        cur.execute(add_magazine_sub_rate,data_magazine_sub_rate)
        db.commit()
        print magazine_name, magazine_frequency, magazine_editor_name
        if request.form['submit'] == 'Submit':
            return redirect(url_for('index'))


@app.route('/magazines', methods=['GET', 'POST'])
def magazines():
    if request.method == 'GET':
        cur = db.cursor()
        cur.execute("SELECT m1.pm_name, m1.frequency, m2.state, m2.rate FROM magazine m1,magazine_subscription_rate m2 WHERE m1.pm_name = m2.pm_name;")
        data = list(cur.fetchall())
        all_magazines = list()
        for row in data:
            all_magazines.append(list(row))
        return render_template('magazines.html', all_magazines=all_magazines)

@app.route('/daily_newspapers', methods=['GET', 'POST'])
def daily_newspapers():
    if request.method == 'GET':
        return render_template('daily_newspapers.html')

@app.route('/weekly_newspapers', methods=['GET', 'POST'])
def weekly_newspapers():
    if request.method == 'GET':
        return render_template('weekly_newspapers.html')
