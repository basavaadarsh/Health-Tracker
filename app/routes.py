from flask import render_template, flash, redirect, url_for, request
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm
from app.models import User, Meal
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Hash the password before storing it
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # Create a new user instance with form data
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        # Add the user to the database
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('tracker'))
        else:
             flash('Login unsuccessful. Please check your email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)
@app.route('/tracker')
@login_required
def tracker():
    # Fetch the user's meals from the database
    meals = Meal.query.filter_by(user_id=current_user.id).all()
    return render_template('tracker.html', title='Nutrition Tracker', meals=meals)       

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))