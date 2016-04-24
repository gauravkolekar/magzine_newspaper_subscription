from flask import render_template, request, url_for, redirect, session
from runserver import app
from database_configuration import database_configuration as db
#from db_config import database_configuration as db
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
        session['sub_username'] = user_name
        try:
            add_customer = "INSERT INTO CUSTOMER (cname, address) VALUES (%s, %s)"
            data_customer = (user_name, user_address)
            cur.execute(add_customer, data_customer)
            db.commit()
        except:
            pass	
        #print user_name, user_address
        if request.form['submit'] == 'Submit':
            return redirect(url_for('subscription'))

@app.route('/subscription')
def subscription():
    return render_template('subscription.html')

#Gaurav Kolekar
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
        if request.form['submit'] == 'Submit':
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
            #print magazine_name, magazine_frequency, magazine_editor_name
            return redirect(url_for('index'))
        '''
        else:
            query = "UPDATE MAGAZINE SET frequency %s, editorm_name %s WHERE pm_name = %s"
            query_data = (magazine_frequency, magazine_editor_name, magazine_name)
            cur.execute(query, query_data)
            db.commit()
            return render_template('add_magazine.html')
        '''
#Gaurav Kolekar

@app.route('/add_daily_newspaper', methods=['GET','POST'])
def add_daily_newspaper():
    if request.method == 'GET':
        return render_template('add_daily_newspaper.html')
    elif request.method == 'POST':
        newspaper_name = str(request.form['newspaper_name'])
        newspaper_editor_name = str(request.form['newspaper_editor'])
        state_name = str(request.form['state_name'])
        rate = int(request.form['rate'])
        cur = db.cursor()
        try:
            add_newspaper_d = "INSERT INTO newspaper_daily (pn_name , editor_nd_name) VALUES (%s,%s)"
            data_newspaper_d = (newspaper_name,newspaper_editor_name)
            cur.execute(add_newspaper_d,data_newspaper_d)
        except:
               pass
        add_newspaper_sub_rate = "INSERT INTO daily_newspaper_rate (dnr_name, state, rate) VALUES (%s,%s,%s)"
        data_newspaper_sub_rate = (newspaper_name,state_name,rate)
        cur.execute(add_newspaper_sub_rate,data_newspaper_sub_rate)
        db.commit()
        print newspaper_name, newspaper_editor_name
        if request.form['submit'] == 'Submit':
            return redirect(url_for('index'))			

# Gaurav Kolekar
@app.route('/add_weekly_newspaper', methods=['GET', 'POST'])
def add_weekly_newspaper():
    if request.method == 'GET':
        return render_template('add_weekly_newspaper.html')
    elif request.method == 'POST':
        weekly_newspaper_name = str(request.form['weekly_newspaper_name'])
        weekly_newspaper_frequency = str(request.form['weekly_newspaper_frequency'])
        weekly_newspaper_editor_name = str(request.form['weekly_newspaper_editor'])
        weekly_newspaper_state_name = str(request.form['weekly_newspaper_state_name'])
        weekly_newspaper_rate = int(request.form['weekly_newspaper_rate'])
        cur = db.cursor()
        if request.form['submit'] == 'Submit':
            try:
                add_weekly_magazine = "INSERT INTO NEWSPAPER_WEEKLY (pn_name , editor_nw_name) VALUES (%s, %s)"
                data_weekly_newspaper = (weekly_newspaper_name, weekly_newspaper_editor_name)
                cur.execute(add_weekly_magazine, data_weekly_newspaper)
            except:
                pass
            add_weekly_newspaper_rate = "INSERT INTO weekly_newspaper_rate(wnr_name, state, rate) VALUES (%s,%s,%s)"
            data_weekly_newspaper_rate = (weekly_newspaper_name, weekly_newspaper_state_name, weekly_newspaper_rate)
            cur.execute(add_weekly_newspaper_rate, data_weekly_newspaper_rate)
            db.commit()
            # print weekly_newspaper_name, weekly_newspaper_state_name, weekly_newspaper_rate
            return redirect(url_for('index'))
        '''
        else:
            query = "UPDATE MAGAZINE SET frequency %s, editorm_name %s WHERE pm_name = %s"
            query_data = (magazine_frequency, magazine_editor_name, magazine_name)
            cur.execute(query, query_data)
            db.commit()
            return render_template('add_magazine.html')
        '''
#Gaurav Kolekar

#Gaurav Kolekar
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
#Gaurav Kolekar

@app.route('/daily_newspapers', methods=['GET', 'POST'])
def daily_newspapers():
    if request.method == 'GET':
        cur = db.cursor()
        cur.execute("SELECT dnr_name, state, rate FROM daily_newspaper_rate;")
        data = list(cur.fetchall())
        all_newspapers_d = list()
        for row in data:
            all_newspapers_d.append(list(row))
        return render_template('daily_newspapers.html', all_newspapers_d = all_newspapers_d)

#Gaurav Kolekar
@app.route('/weekly_newspapers', methods=['GET', 'POST'])
def weekly_newspapers():
    if request.method == 'GET':
        cur = db.cursor()
        get_all_weekly_newspaper_query = "SELECT wnr_name, state, rate FROM weekly_newspaper_rate"
        cur.execute(get_all_weekly_newspaper_query)
        data = cur.fetchall()
        all_weekly_newspaper = list()
        for row in data:
            all_weekly_newspaper.append(list(row))
        return render_template('weekly_newspapers.html', all_weekly_newspaper=all_weekly_newspaper)
#Gaurav Kolekar

@app.route('/magazine_subscription', methods=['GET','POST'])
def magazine_subscription():
    cost = 0
    name = request.args.get('name')
    frequency = request.args.get('freq')
    state = request.args.get('state')
    rate = request.args.get('rate')
    #print "Initial values: ",type(frequency), frequency, type(rate), rate
    if request.method == 'GET':
        return render_template('magazine_subscription.html', mag_name=name, mag_frequency=frequency, mag_state=state, mag_rate=rate)
    elif request.method == 'POST':
        print type(frequency), frequency, type(rate), rate
        cur = db.cursor()
        my_var = session.get('sub_username', None)
        cur.execute("SELECT id_no FROM customer WHERE cname = %s", [my_var])
        cust_id_tup = cur.fetchone()
        cust_id_list = list(cust_id_tup)
        cust_id = int(cust_id_list[0])
        magazine_number_of_issues = int(request.form['number_of_issues_magazine'])
        magazine_start_date = request.form['start_date_magazine']
        magazine_end_date = request.form['end_date_magazine']
        magazine_start_date = datetime.strptime(magazine_start_date, '%Y-%m-%d')
        magazine_end_date = datetime.strptime(magazine_end_date, '%Y-%m-%d')
        frequency = str(frequency)
        rate = float(rate)
        print "frequency is: ",frequency,"and rate is:", rate
        act_freq = (magazine_end_date - magazine_start_date).days
        if frequency == 'Weekly':
            cost = (act_freq/7) * rate * magazine_number_of_issues
        elif frequency == 'Monthly':
            cost = (act_freq/30) * rate * magazine_number_of_issues	
        elif frequency == 'Yearly':
            cost = (act_freq/365) * rate * magazine_number_of_issues	
        print "List of values: ",cust_id, magazine_number_of_issues, magazine_start_date, magazine_end_date
        print "Actual cost: ",cost
        add_customer_sub = "INSERT INTO sub_magazine (id_no, pm_name, no_of_issues, start_date, end_date, actual_end_date, active_flag, cost ) values (%s, %s, %s, %s, %s,%s,%s,%s)"
        data_customer_sub = (cust_id, name, magazine_number_of_issues, magazine_start_date, magazine_end_date, magazine_end_date, 1, cost)
        cur.execute(add_customer_sub, data_customer_sub)
        db.commit()
        return redirect(url_for('subscription'))

@app.route('/daily_newspaper_subscription', methods=['GET','POST'])
def daily_newspaper_subscription():
    cost = 0
    name = request.args.get('name')
    sub_type = request.args.get('sub_type')
    state = request.args.get('state')
    rate = request.args.get('rate')
    print "Initial values: ",type(sub_type), sub_type, type(rate), rate
    if request.method == 'GET':
        return render_template('daily_newspaper_subscription.html', newsd_name=name, newsd_sub_type=sub_type, newsd_state=state, newsd_rate=rate)
    elif request.method == 'POST':
        cur = db.cursor()
        my_var = session.get('sub_username', None)
        cur.execute("SELECT id_no FROM customer WHERE cname = %s", [my_var])
        cust_id_tup = cur.fetchone()
        cust_id_list = list(cust_id_tup)
        cust_id = int(cust_id_list[0])
        newsd_number_of_issues = int(request.form['number_of_issues_newspaperd'])
        newsd_start_date = request.form['start_date_newspaperd']
        newsd_end_date = request.form['end_date_newspaperd']
        newsd_start_date = datetime.strptime(newsd_start_date, '%Y-%m-%d')
        newsd_end_date = datetime.strptime(newsd_end_date, '%Y-%m-%d')
        sub_type = int(sub_type)
        rate = float(rate)
        act_freq = (newsd_end_date - newsd_start_date).days
        act_freq = act_freq / 7
        cost = sub_type * act_freq * newsd_number_of_issues * rate
        print "List of values: ",cust_id, newsd_number_of_issues, newsd_start_date, newsd_end_date
        print "Actual cost: ",cost
        add_customer_newsd_sub = "INSERT INTO sub_newspaper_daily (id_no, pnd_name, no_of_issues, sub_type, start_date, end_date, actual_end_date, active_flag, cost ) values (%s, %s, %s, %s, %s,%s,%s,%s, %s)"
        data_customer_newsd_sub = (cust_id, name, newsd_number_of_issues, sub_type, newsd_start_date, newsd_end_date, newsd_end_date, 1, cost)
        cur.execute(add_customer_newsd_sub, data_customer_newsd_sub)
        db.commit()
        return redirect(url_for('subscription'))

#Gaurav Kolekar
@app.route('/weekly_newspaper_subscription', methods=['GET', 'POST'])
def weekly_newspaper_subscription():
    cost = 0
    weekly_newspaper_name = request.args.get('weekly_newspaper_name')
    weekly_newspaper_frequency = 'Weekly'
    weekly_newspaper_state = request.args.get('weekly_newspaper_state')
    weekly_magazine_rate = request.args.get('weekly_magazine_rate')
    if request.method == 'GET':
        return render_template('weekly_newspaper_subscription.html', wnp_name=weekly_newspaper_name, wnp_state=weekly_newspaper_state, wnp_rate=weekly_magazine_rate)
    elif request.method == 'POST':
        cur = db.cursor()
        my_var = session.get('sub_username', None)
        cur.execute("SELECT id_no FROM customer WHERE cname = %s", [my_var])
        cust_id_tup = cur.fetchone()
        cust_id_list = list(cust_id_tup)
        cust_id = int(cust_id_list[0])
        weekly_newspaper_number_of_issues = int(request.form['number_of_issues_weekly_newspaper'])
        weekly_newspaper_start_date = request.form['start_date_weekly_newspaper']
        weekly_newspaper_end_date = request.form['end_date_weekly_newspaper']
        weekly_newspaper_start_date = datetime.strptime(weekly_newspaper_start_date, '%Y-%m-%d')
        weekly_newspaper_end_date = datetime.strptime(weekly_newspaper_end_date, '%Y-%m-%d')
        frequency = str(weekly_newspaper_frequency)
        rate = float(weekly_magazine_rate)
        act_freq = (weekly_newspaper_end_date - weekly_newspaper_start_date).days
        cost = (act_freq / 7) * rate * weekly_newspaper_number_of_issues
        query_weekly_newspaper_sub = "INSERT INTO sub_newspaper_weekly (id_no, pnw_name, no_of_issues, start_date, end_date, actual_end_date, active_flag, cost ) values (%s, %s, %s, %s, %s,%s,%s,%s)"
        data_weekly_newspaper_sub = (cust_id, weekly_newspaper_name, weekly_newspaper_number_of_issues, weekly_newspaper_start_date, weekly_newspaper_end_date, weekly_newspaper_end_date, 1, cost)
        cur.execute(query_weekly_newspaper_sub, data_weekly_newspaper_sub)
        db.commit()
        return redirect(url_for('subscription'))
#Gaurav Kolekar
