from flask import Flask, render_template,request,redirect,url_for
from flask_cors import CORS

BASE_URL= "/"

app = Flask(__name__, static_folder='static',
 template_folder='templates')

@app.errorhandler(404)
def not_found(response):
    return render_template('404.html'), 404

@app.errorhandler(405)
def not_allowed(response):
    return render_template('405.html'), 404


CORS(app)

@app.route(f"{BASE_URL}", methods=["GET"])
def home():
    return render_template('index.html')

@app.route(f"{BASE_URL}about", methods=["GET"])
def about():
    return render_template('about.html')

@app.route(f"{BASE_URL}services", methods=["GET"])
def services():
    return render_template('services.html')

@app.route(f"{BASE_URL}blog", methods=["GET"])
def blog():
    return render_template('blog.html')

@app.route(f"{BASE_URL}shops", methods=["GET"])
def shops():
    return render_template('shops.html')

@app.route(f"{BASE_URL}contact", methods=["GET"])
def contact():
    return render_template('contact.html')

@app.route(f"{BASE_URL}livestream", methods=["GET"])
def livestreams():
    return render_template('livestream.html')

@app.route(f"{BASE_URL}signup/user", methods=["GET", "POST"])
def signup_user():
    if request.method == "GET":
        return render_template('signupuser.html')
    elif request.method == "POST":
        return redirect(url_for('signin'))

@app.route(f"{BASE_URL}signup/technician", methods=["GET", "POST"])
def signup_technician():
    if request.method == "GET":
        return render_template('signuptechnician.html')
    elif request.method == "POST":
        return redirect(url_for('signin'))

@app.route(f"{BASE_URL}signup/company", methods=["GET", "POST"])
def signup_company():
    if request.method == "GET":
        return render_template('signuptechnician.html')
    elif request.method == "POST":
        return redirect(url_for('signin'))

@app.route(f"{BASE_URL}signin", methods=["GET", "POST"])
def signin():
    if request.method == "GET":
        return render_template('signin.html')
    elif request.method == "POST":
        return redirect(url_for('home'))
    else:
        return redirect(url_for('not_allowed'))


app.run()