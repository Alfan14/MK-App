from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.config['SECRET_KEY'] = 'a1lf4n-s3cr3t-k3y'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
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