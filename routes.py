from flask import render_template, request, url_for, redirect, session
from runserver import app
#from database_configuration import database_configuration as db
from db_config import database_configuration as db
from datetime import datetime, date

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
        session['my_var'] = user_name
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

@app.route('/magazine_subscription', methods=['GET','POST'])
def magazine_subscription():
    name = request.args.get('name')
    frequency = request.args.get('freq')
    print type(frequency), frequency
    state = request.args.get('state')
    rate = request.args.get('rate')
    if request.method == 'GET':
        print type(frequency), frequency
        return render_template('magazine_subscription.html', mag_name=name, mag_frequency=frequency, mag_state=state, mag_rate=rate)
    elif request.method == 'POST':
        cur = db.cursor()
        my_var = session.get('my_var', None)
        cur.execute("SELECT id_no FROM customer WHERE cname = %s", (my_var,))
        cust_id_tup = cur.fetchone()
        cust_id_list = list(cust_id_tup)
        cust_id = int(cust_id_list[0])
        magazine_number_of_issues = int(request.form['number_of_issues_magazine'])
        magazine_start_date = request.form['start_date_magazine']
        magazine_end_date = request.form['end_date_magazine']
        magazine_start_date = datetime.strptime(magazine_start_date, '%Y-%m-%d')
        magazine_end_date = datetime.strptime(magazine_end_date, '%Y-%m-%d')
        print type(frequency), frequency
        act_freq = (magazine_end_date - magazine_start_date).days
        if frequency == 'Weekly':
            cost = (act_freq/7) * rate * magazine_number_of_issues
        elif frequency == 'Monthly':
            cost = (act_freq/30) * rate * magazine_number_of_issues	
        elif frequency == 'Yearly':
            cost = (act_freq/365) * rate * magazine_number_of_issues	
        print cust_id, magazine_number_of_issues, magazine_start_date, magazine_end_date
        print type(act_freq)
#        add_customer_sub = "INSERT INTO sub_magazine (id_no, pm_name, no_of_issues, start_date, end_date, actual_end_date, active_flag, cost ) values (%s, %s, %s, %s, %s,%s,%s,%s)"
#        data_customer_sub = (cust_id, name, magazine_number_of_issues, magazine_start_date, magazine_end_date, magazine_end_date, 1, cost)
#        cur.execute(add_customer_sub, data_customer_sub)
#        db.commit()