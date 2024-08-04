from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import MySQLdb.cursors, re, hashlib
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'septiyan_h4rd_l1f3'

# Enter your database connection details below
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'python_login'
db = MySQL(app)

admin = Admin(app, name='My Admin Panel', template_mode='bootstrap4')

def get_models():
    from models import User, Role, Post
    from views import UserAdmin, RoleAdmin, PostAdmin

    admin.add_view(UserAdmin(User, db.session))
    admin.add_view(RoleAdmin(Role, db.session))
    admin.add_view(PostAdmin(Post, db.session))

if __name__ == '__main__':
    with app.app_context():
        from models import User  # Import here to avoid circular import
        db.create_all()
        admin.add_view(ModelView(User, db.session))

    app.run(debug=True)