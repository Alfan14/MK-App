from flask_admin.contrib.sqla import ModelView
from flask import render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
from models import User
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

class AdminModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.role.name == 'Admin'

login_manager = LoginManager(app)
login_manager.login_view = 'login'


class UserAdmin(AdminModelView):
    column_list = ('username', 'email', 'role')
    column_labels = {'username': 'Username', 'email': 'Email Address', 'role': 'Role'}
    column_filters = ('username', 'email', 'role.name')

class RoleAdmin(AdminModelView):
    column_list = ('name',)
    column_labels = {'name': 'Role Name'}
    column_filters = ('name',)

class PostAdmin(AdminModelView):
    column_list = ('title', 'author', 'content')
    column_labels = {'title': 'Post Title', 'author': 'Author', 'content': 'Content'}
    column_filters = ('title', 'author.username')
class UserLogin(UserMixin):
    pass
#Register,Login,Logout
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if request.method == 'POST':
         username = request.form['username']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    pass
    return render_template('registration.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.method == 'POST':
         user = User.query.filter_by(email=request.form['email']).first()
        if user and check_password_hash(user.password, request.form['password']):
            login_user(user)
        return redirect(url_for('admin.index'))   
    pass
    return render_template('login.html')
 

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Inside the login view function
