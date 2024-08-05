from flask import Flask, render_template, request, redirect, url_for, session ,  flash
from flask_mysqldb import MySQL
from wtforms import StringField, PasswordField, SubmitField, DateField, SelectField , HiddenField
import MySQLdb.cursors, re, hashlib
from flask_login import  LoginManager,UserMixin,login_required,current_user,login_manager
from urllib.parse import urlparse, urljoin
from wtforms.validators import DataRequired, Email
from flask_wtf import FlaskForm
import os
import re
import pymysql

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Change this to your secret key (it can be anything, it's for extra protection)
app.secret_key = 'septiyan_h4rd_l1f3'

# Enter your database connection details below
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'python_login'


# Initialize MySQL
mysql = MySQL(app)
@app.route('/pythonlogin/admin', methods=['GET', 'POST'])
def admin():
    if 'loggedin' in session and session['role'] == 'admin':
        # Logic for the admin page
        return render_template('admin.html', username=session['username'])
    else:
        flash('Access denied: Admins only!', 'danger')
        return redirect(url_for('login'))
@app.route('/pythonlogin/', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        cursor.close()
        
        if account:
            # Check hashed password
            if (account['password'], password):
                session['loggedin'] = True
                session['id'] = account['id']
                session['username'] = account['username']
                session['role'] = account['role']
                msg = 'Logged in successfully!'
                if session['role'] == 'admin':
                    return redirect(url_for('admin'))
                else:
                    return render_template('main.html', account=account, msg=msg)
            else:
                msg = 'Incorrect password!'
        else:
            msg = 'Username not found!'

    return render_template('index.html', msg=msg)


@app.route('/pythonlogin/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/pythonlogin/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form and 'email' in request.form:
            username = request.form['username']
            image = request.files['image']
            password = request.form['password']
            email = request.form['email']
            role = request.form.get('role') 

            connection = mysql.connection
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
            account = cursor.fetchone()
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])

            # Save image to the upload directory
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            print(f"Saving file to: {file_path}")
            image.save(file_path)

            if account:
                msg = 'Account already exists!'
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                msg = 'Invalid email address!'
            elif not re.match(r'[A-Za-z0-9]+', username):
                msg = 'Username must contain only characters and numbers!'
            elif not username or not password or not email:
                msg = 'Please fill out the form!'
            else:
               with connection.cursor() as cursor:
                sql = """
                INSERT INTO accounts (username, image, password, email, role)
                VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (username, file_path, password, email, role))
            connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)

@app.route('/pythonlogin/home')
def home():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = %s', (session['id'],))
        account = cursor.fetchone()
        return render_template('main.html', username=session['username'],account=account)
    return redirect(url_for('login'))



@app.route('/pythonlogin/profile')
def profile():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = %s', (session['id'],))
        account = cursor.fetchone()
        image_path = account['image'].replace('static/', '').replace('\\', '/')
        return render_template('profile.html', account=account,image_path=image_path)
    return redirect(url_for('login'))


@app.route('/pythonlogin/edit-profile/<int:user_id>', methods=['GET', 'POST'])
def edit_profile(user_id):
    if 'loggedin' in session and session['id'] == user_id:
        if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']
            cur = mysql.connection.cursor()
            cur.execute("""
                UPDATE accounts
                SET username = %s, email = %s
                WHERE id = %s
            """, (username, email, user_id))
            mysql.connection.commit()
            cur.close()
            flash('Profile updated successfully!')
            return redirect(url_for('login'))

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM accounts WHERE id = %s", (user_id,))
        account = cur.fetchone()
        cur.close()
        return render_template('edit.html', account=account)
    return redirect(url_for('login'))

#SearchEngine
if __name__ == '__main__':
    app.run(debug=True)
