from flask import Flask, render_template, request, redirect, url_for, session ,  flash
from flask_mysqldb import MySQL
from wtforms import StringField, PasswordField, SubmitField, DateField, SelectField , HiddenField
import MySQLdb.cursors, re, hashlib
from flask_login import  LoginManager,UserMixin,login_required,current_user,login_manager
from wtforms.validators import DataRequired, Email
from flask_wtf import FlaskForm

app = Flask(__name__)

# Change this to your secret key (it can be anything, it's for extra protection)
app.secret_key = 'septiyan_h4rd_l1f3'

# Enter your database connection details below
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'python_login'


# Initialize MySQL
mysql = MySQL(app)


# Initialize the LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'editaccount'

# User model definition
class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

# User loader function
@login_manager.user_loader
def load_user(user_id):
    cursor = mysql.connect().cursor()
    cursor.execute('SELECT id, username, password FROM accounts WHERE id = %s', (user_id,))
    user_data = cursor.fetchone()
    cursor.close()
    if user_data:
        return User(*user_data)
    return None

@app.route('/pythonlogin/', methods=['GET', 'POST'])
def login():
    msg = ''
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
            msg = 'Logged in successfully !'
            return render_template('main.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('index.html', msg = msg)

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
            password = request.form['password']
            email = request.form['email']
            
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
            account = cursor.fetchone()
            
            if account:
                msg = 'Account already exists!'
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                msg = 'Invalid email address!'
            elif not re.match(r'[A-Za-z0-9]+', username):
                msg = 'Username must contain only characters and numbers!'
            elif not username or not password or not email:
                msg = 'Please fill out the form!'
            else:
                cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s)', (username, password, email, ))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)


@app.route('/pythonlogin/home')
def home():
    if 'loggedin' in session:
        return render_template('main.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/pythonlogin/profile')
def profile():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = %s', (session['id'],))
        account = cursor.fetchone()
        return render_template('profile.html', account=account)
    return redirect(url_for('login'))

class EditAccountForm(FlaskForm):
    username = HiddenField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[Email()])
    submit = SubmitField('Submit')

@app.route('/pythonlogin/editaccount', methods=['GET', 'POST'])
@login_required
def editaccount():
    form = EditAccountForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            username = current_user.username
            email = form.email.data

            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            try:
                cursor.execute('UPDATE accounts SET email = %s WHERE username = %s', (email, username))
                mysql.connection.commit()
                flash('Profile updated successfully!', 'success')
            except MySQLdb.Error as e:
                flash(f'An error occurred: {e}', 'danger')
            finally:
                cursor.close()
            
            return redirect('/editaccount')
    else:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute('SELECT * FROM accounts WHERE username = %s', (current_user.username,))
            account = cursor.fetchone()
            if account:
                form.username.data = account['username']
                form.email.data = account['email']
        except MySQLdb.Error as e:
            flash(f'An error occurred: {e}', 'danger')
        finally:
            cursor.close()

        return render_template('edit.html', title='Edit Account', form=form)
    return redirect(url_for('edit'))
#SearchEngine
if __name__ == '__main__':
    app.run(debug=True)
