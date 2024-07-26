from flask import Flask,request, redirect, url_for
from flask import url_for
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('template.html', title='Home Page',
name='John Doe', messages=['Hello', 'Hi', 'Hey'])

@app.route('/')
def home():
    return "Welcome to the Homepage!"
@app.route('/user/<username>')
def show_user_profile(username):
# show the user profile for that user
    return f'User {username}'
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/handle_form', methods=['POST'])
def handle_form():
    name = request.form['name']
    email = request.form['email']
# Process or store the form data here
    return redirect(url_for('thank_you'))
@app.route('/post/<int:post_id>')
def show_post(post_id):
# show the post with the given id, the id is an integer
    return f'Post {post_id}'
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
     return do_the_login()
    else:
        return show_the_login_form()
@app.route('/login')
def login():
    return 'login'
@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'
with app.test_request_context():
    print(url_for('index'))
print(url_for('login'))
print(url_for('login', next='/'))
print(url_for('profile', username='John Doe'))

@app.errorhandler(404)
def page_not_found(error):
    return "This page does not exist.", 404
@app.errorhandler(500)
def internal_server_error(error):
    return "Internal server error.", 500