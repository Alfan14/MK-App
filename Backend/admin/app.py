from flask import Flask,render_template
from flask_admin import Admin,BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_mysqldb import MySQL

# Flask and Flask-SQLAlchemy initialization here

app = Flask(__name__)


# Change this to your secret key (it can be anything, it's for extra protection)
app.secret_key = 'septiyan_h4rd_l1f3'

# Enter your database connection details below
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'python_login'


# Initialize MySQL
db = MySQL(app)

admin = Admin(app, name='microblog', template_mode='bootstrap3')
'''
admin = Admin(app, name='microblog', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))
'''

class AnalyticsView(BaseView):
    @expose('/admin')
    def index(self):
        return self.render('analytics_index.html')
admin.add_view(AnalyticsView(name='Analytics', endpoint='analytics'))

@app.route('/home')
def home():
    arg1 = 'Fuck you'
    return render_template('index.html',arg1=arg1)

app.run()

