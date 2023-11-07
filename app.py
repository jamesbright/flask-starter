from flask import Flask, render_template,jsonify
from models import storage
from models.user import User
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from wtforms.validators import ValidationError
from flask_bcrypt import Bcrypt
from functions import *
from forms import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
bcrypt = Bcrypt(app) 

login_manager = LoginManager() 
login_manager.init_app(app) 
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    """A function that loads the user from storage by id"""
    return storage.get_user_by_id(int(user_id))
  
@app.route("/")
def hello():
    return render_template('home.html', jobs=JOBS)


@app.route("/signup", strict_slashes=False,
           methods=['GET', 'POST'])
def signup():
    """A function that renders the signup page"""
    form = SignupForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            existing_user_email = storage.get_user(form.email.data)
            if existing_user_email:
                flash("That email already exists Please choose a different one.")
            hashed_password = bcrypt.generate_password_hash(form.password.data)
            storage.reload()
            new_user = User(first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            email=form.email.data,
                            password=hashed_password,
                            phone_no=form.phone_no.data,
                            address=form.address.data)
            storage.new(new_user)
            storage.save()
            return redirect(url_for('login'))
    return render_template("signup.html", form=form, title="Signup")

@app.route("/login", strict_slashes=False,
           methods=['GET', 'POST'])
def login():
    """A function that renders the login page"""
    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            user = storage.get_user(form.email.data)
            if user:
                if bcrypt.check_password_hash(user.password, form.password.data):
                    login_user(user)
                    return redirect(url_for('dashboard', user=user.github_username))
            flash('Invalid email or password', 'error')
    return render_template("login.html", form=form, title="Login")

@app.route('/logout', strict_slashes=False,
           methods=['GET', 'POST'])
@login_required
def logout():
    """A function that renders the logout page"""
    logout_user()
    flash("You have been loggged out!", "info")
    return redirect(url_for('login'))

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
