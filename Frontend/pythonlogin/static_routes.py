from flask import Flask,Blueprint, send_from_directory

app = Flask(__name__)

static_routes = Blueprint('static_routes', __name__)

# CSS
@app.route('/css/style.css')
def serve_style_css():
    return send_from_directory('static/css', 'style.css')

@app.route('/css/style-login.css')
def serve_style_login_css():
    return send_from_directory('static/css', 'style-login.css')

@app.route('/css/register.css')
def serve_register_css():
    return send_from_directory('static/css', 'register.css')

@app.route('/css/profile.css')
def serve_profile_css():
    return send_from_directory('static/css', 'profile.css')

@app.route('/css/main.css')
def serve_main_css():
    return send_from_directory('static/css', 'main.css')

@app.route('/css/edit.css')
def serve_edit_css():
    return send_from_directory('static/css', 'edit.css')

@app.route('/css/admin.css')
def serve_admin_css():
    return send_from_directory('static/css', 'admin.css')

# JavaScript
@app.route('/js/admin.js')
def serve_admin_js():
    return send_from_directory('static/js', 'admin.js')

@app.route('/js/main.js')
def serve_main_js():
    return send_from_directory('static/js', 'main.js')

# Images
@app.route('/images/login-logo.png')
def serve_login_logo():
    return send_from_directory('static/images', 'login-logo.png')

@app.route('/images/sate-kelinci.jpg')
def serve_sate_kelinci():
    return send_from_directory('static/images', 'sate-kelinci.jpg')

@app.route('/images/dana.png')
def serve_dana():
    return send_from_directory('static/images', 'dana.png')

@app.route('/images/gmaps.png')
def serve_gmaps():
    return send_from_directory('static/images', 'gmaps.png')

@app.route('/images/gopay.png')
def serve_gopay():
    return send_from_directory('static/images', 'gopay.png')

# Uploads
@app.route('/uploads/1720439717-picsay.jpg')
def serve_picsay_jpg():
    return send_from_directory('static/uploads', '1720439717-picsay.jpg')

@app.route('/uploads/a853441f-21cc-45d8-89da-77866ce0a9d4_waifu2x_art_noise3_scale.png')
def serve_waifu2x_art_noise():
    return send_from_directory('static/uploads', 'a853441f-21cc-45d8-89da-77866ce0a9d4_waifu2x_art_noise3_scale.png')

@app.route('/uploads/WIN_20240629_08_12_44_Pro.jpg')
def serve_win_20240629_08_12_44_pro():
    return send_from_directory('static/uploads', 'WIN_20240629_08_12_44_Pro.jpg')

@app.route('/uploads/WIN_20240716_05_20_39_Pro.jpg')
def serve_win_20240716_05_20_39_pro():
    return send_from_directory('static/uploads', 'WIN_20240716_05_20_39_Pro.jpg')

@app.route('/uploads/WIN_20240805_08_52_25_Pro.jpg')
def serve_win_20240805_08_52_25_pro():
    return send_from_directory('static/uploads', 'WIN_20240805_08_52_25_Pro.jpg')
