from flask import Flask, render_template, redirect, url_for, flash, request
from flask_mysqldb import MySQL
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user

app = Flask(__name__)
app.secret_key = 'septiyan_h4rd_l1f3'

# Enter your database connection details
app.config['MYSQL_HOST'] = 'your_mysql_host'
app.config['MYSQL_USER'] = 'your_mysql_user'
app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
app.config['MYSQL_DB'] = 'your_database_name'

mysql = MySQL(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    published = BooleanField('Publish')
    submit = SubmitField('Post')

@app.route("/admin/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    if not current_user.is_admin:  
        flash('You do not have permission to access this page.', 'danger')
        return redirect(url_for('home'))
    
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        published = form.published.data
        author_id = current_user.id

        # Insert post into MySQL
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO posts(title, content, author_id, published) VALUES(%s, %s, %s, %s)",
                    (title, content, author_id, published))
        mysql.connection.commit()
        cur.close()
        
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post', form=form, legend='New Post')

@app.route("/home")
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT p.title, p.content, p.created_at, u.username FROM posts p JOIN users u ON p.author_id = u.id WHERE p.published = 1 ORDER BY p.created_at DESC")
    posts = cur.fetchall()
    cur.close()
    return render_template('home.html', posts=posts)
@login_manager.user_loader
def load_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s", [user_id])
    user_data = cur.fetchone()
    cur.close()
    if user_data:
        user = UserMixin()
        user.id = user_data[0]
        user.username = user_data[1]
        user.is_admin = user_data[5]  # Assuming is_admin is the 6th field
        return user
    return None
