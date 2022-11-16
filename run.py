from flask import Flask, render_template,request,redirect,url_for
from flask_cors import CORS

app = Flask(__name__, static_folder='static',
 template_folder='templates')

@app.errorhandler(404)
def not_found(response):
    return render_template('404.html'), 404

@app.errorhandler(405)
def not_allowed(response):
    return render_template('405.html'), 404

@app.route("/", methods=["GET"])
def home():
    return render_template('index.html')

@app.route("/about", methods=["GET"])
def about():
    return render_template('about.html')

@app.route("/services", methods=["GET"])
def services():
    return render_template('services.html')

@app.route("/blog", methods=["GET"])
def blog():
    return render_template('blog.html')

@app.route("/shops", methods=["GET"])
def shops():
    return render_template('shops.html')

@app.route("/contact", methods=["GET"])
def contact():
    return render_template('contact.html')

@app.route("/livestream", methods=["GET"])
def livestreams():
    return render_template('livestream.html')

@app.route("/signup/user", methods=["GET", "POST"])
def signup_user():
    if request.method == "GET":
        return render_template('signupuser.html')
    elif request.method == "POST":
        return redirect(url_for('signin'))

@app.route("/signup/technician", methods=["GET", "POST"])
def signup_technician():
    if request.method == "GET":
        return render_template('signuptechnician.html')
    elif request.method == "POST":
        return redirect(url_for('signin'))

@app.route("/signup/company", methods=["GET", "POST"])
def signup_company():
    if request.method == "GET":
        return render_template('signuptechnician.html')
    elif request.method == "POST":
        return redirect(url_for('signin'))

@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "GET":
        return render_template('signin.html')
    elif request.method == "POST":
        return redirect(url_for('home'))
    else:
        return redirect(url_for('not_allowed'))


app.run()
