from flask import Flask, render_template, request, redirect, url_for, session
from flask_googlemaps import GoogleMaps
from flask_bootstrap import Bootstrap
from flask_googlemaps import Map
from flask_mysqldb import MySQL 
from flask_cors import CORS
import MySQLdb.cursors 
import re 


app = Flask(__name__)
app.secret_key = 'wfCy&4wmm*^Z'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'geeklogin'

bootstrap = Bootstrap(app)
mysql = MySQL(app) 
GoogleMaps(app, key="my-key")

@app.route('/', methods=["GET"])
def start():
    return render_template ('start.html');

@app.route('/users', methods=["GET", "POST"])
def user_details():
    msg = '' 
    if request.method == 'POST' and 'name' in request.form and 'email' in request.form : 
        name = request.form['name']  
        email = request.form['email'] 
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor) 
        cursor.execute('SELECT * FROM users WHERE username = % s', (name, )) 
        account = cursor.fetchone() 
        if not re.match(r'[^@]+@[^@]+\.[^@]+', email): 
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', name): 
            msg = 'Username must contain only characters and numbers !'
        elif not name or not email: 
            msg = 'Please fill out the form !'
        else: 
            cursor.execute('INSERT INTO users VALUES (NULL, % s, % s)', (name, email, )) 
            mysql.connection.commit() 
            return redirect (url_for('survey'))  
    return render_template('users.html', msg=msg)

@app.route('/survey', methods=["GET" , "POST"])
def survey():
    msg = '' 
    if request.method == 'POST' and 'userName' in request.form and 'phone' in request.form and 'address' in request.form and 'age' in request.form and 'test' in request.form and 'dtest' in request.form and 'ctest' in request.form and 'htest' in request.form and 'group' in request.form: 
        username = request.form['userName']  
        phone = request.form['phone'] 
        address = request.form['address']
        test = request.form['test']
        age = request.form['age']
        dtest = request.form['dtest']
        ctest = request.form['ctest']
        htest = request.form['htest']
        group = request.form['group']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor) 
        cursor.execute('SELECT * FROM survey WHERE Uname = % s', (username, )) 
        account = cursor.fetchone() 
        if not re.match(r'[A-Za-z0-9]+', username): 
            msg = 'name must contain only characters and numbers !'
        elif not phone or not address or not age or not dtest or not ctest or not htest or not group: 
            msg = 'Please fill out the form !'
        else: 
            cursor.execute('INSERT INTO survey VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s)', (username, phone, group, age, address, test, dtest, ctest, htest, )) 
            mysql.connection.commit() 
            if (test == 'negative'):
                return redirect (url_for('my_map'))  
            else:
                return redirect (url_for('info'))
    return render_template('survey.html', msg=msg)

@app.route('/ER', methods=["GET"])
def er():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("select * from EmergenyContact")
    if (resultValue > 0) :
        userDetails = cur.fetchall()
        return render_template('emergency.html', userDetails=userDetails)
    else:
        return 'No data'
        
@app.route('/info')
def info():
     return render_template('info.html')

@app.route('/hospitals', methods=["GET"])
def hospital():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("select hospital.hid,hospital.hname,hospital.haddress,hospital.hphonenumber,isolationward.isoid,isolationward.isobeds from hospital inner join isolationward on hospital.hid=isolationward.hid order by hid;")
    if (resultValue > 0) :
        userDetails = cur.fetchall()
        return render_template('hospitals.html', userDetails=userDetails)
    else:
        return 'No data'

@app.route('/qcenter', methods=["GET"])
def qCenter():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM QuarantineCenter")
    if (resultValue > 0) :
        userDetails = cur.fetchall()
        return render_template('qcenter.html', userDetails=userDetails)

@app.route('/doctors', methods=["GET"])
def doctors():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("select doctors.docid,doctors.docname,doctors.docaddress,docphonenumbers.docphonenumber from doctors inner join docphonenumbers on doctors.docid=docphonenumbers.docid order by docid")
    if (resultValue > 0) :
        userDetails = cur.fetchall()
        return render_template('doctors.html', userDetails=userDetails)

@app.route('/labs', methods=["GET"])
def labs():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM labs")
    if (resultValue > 0) :
        userDetails = cur.fetchall()
        return render_template('labs.html', userDetails=userDetails)
  
@app.route('/map', methods=["GET"])
def my_map():
    mymap = Map(

                identifier="view-side",

                varname="mymap",

                style="height:720px;width:1100px;margin:0;", 

                lat=37.4419, 

                lng=-122.1419, 

                zoom=15,

                markers=[(37.4419, -122.1419)] 

            )
    
    return render_template('map.html', mymap=mymap)

@app.route('/admin', methods =['GET', 'POST']) 
def admin(): 
    msg = '' 
    if request.method == 'POST' and 'latitude' in request.form and 'longitude' in request.form and 'population' in request.form : 
        latitude = request.form['latitude'] 
        longitude = request.form['longitude'] 
        population = request.form['population'] 
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor) 
        cursor.execute('SELECT * FROM redZone') 
        account = cursor.fetchone() 
        cursor.execute('INSERT INTO redZone VALUES ( % s, % s, % s)', (latitude, longitude, population, )) 
        mysql.connection.commit() 
        msg = 'You have successfully added new Red Zone!'
    elif request.method == 'POST': 
        msg = 'Please fill out the form !'
    return render_template('redzone.html', msg = msg) 

@app.route('/login', methods =['GET', 'POST']) 
def login(): 
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form: 
        username = request.form['username'] 
        password = request.form['password'] 
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor) 
        cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password, )) 
        account = cursor.fetchone() 
        if account: 
            session['loggedin'] = True
            session['id'] = account['id'] 
            session['username'] = account['username'] 
            return redirect (url_for('admin'))  
        else: 
            msg = 'Incorrect username / password !'
    return render_template('login.html') 
  
@app.route('/logout') 
def logout(): 
    session.pop('loggedin', None) 
    session.pop('id', None) 
    session.pop('username', None) 
    return redirect(url_for('login')) 
  
@app.route('/register', methods =['GET', 'POST']) 
def register(): 
    msg = '' 
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form : 
        username = request.form['username'] 
        password = request.form['password'] 
        email = request.form['email'] 
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor) 
        cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, )) 
        account = cursor.fetchone() 
        if account: 
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email): 
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username): 
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email: 
            msg = 'Please fill out the form !'
        else: 
            cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s)', (username, password, email, )) 
            mysql.connection.commit() 
            msg = 'You have successfully registered !'
    elif request.method == 'POST': 
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg) 


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)