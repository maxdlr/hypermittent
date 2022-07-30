from pydoc import render_doc
from unicodedata import category
from flask import Blueprint, redirect, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db



auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
            else:
                flash('Nope, try again.', category='error')
        else:
            flash('Can\' find you', category='error')
    return render_template("login.html", is_authenticated=False)


@auth.route('/logout')
def logout():
    return render_template("logout.html")


@auth.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == "POST":
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists', category='error')
        elif len(email) < 4:
            flash('Email too short', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password too short', category='error')
        else:
            newUser = User(email=email, password=generate_password_hash(password1, method='sha256'))
            db.session.add(newUser)
            db.session.commit()
            flash('Account created', category='success')
            return redirect(url_for('views.home'))

            
    return render_template("signup.html")
