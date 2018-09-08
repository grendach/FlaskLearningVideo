
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse

from app import app, db
from app.models import User
from app.forms import LoginForm, RegistrationForm

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'dmytro'}
    posts = [
        {
            'author': user,
            'body': 'Linux',
        },
        {
            'author': {'username': 'Unknown User'},
            'body': "Let's do some code",
        }
    ]
    return render_template('index.html', title='Home', posts=posts)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Tech talk #1'},
        {'author': user, 'body': 'Tech talk #2'}
    ]
    return render_template('user.html', user=user, posts=posts)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    new_user_register = RegistrationForm()

    if new_user_register.validate_on_submit():
        new_user = User(username=new_user_register.username.data, email= new_user_register.email.data)
        new_user.set_password(new_user_register.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Wellcome to MyBlog. Now you are registered! Please log in')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=new_user_register)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user_login = LoginForm()
    if user_login.validate_on_submit():
        user = User.query.filter_by(username=user_login.username.data).first()
        if user is None or not user.check_password(user_login.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=user_login.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=user_login)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))