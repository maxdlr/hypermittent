from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return "<p>Login</p>"


@auth.route('/logout')
def login():
    return "<p>Logout</p>"


@auth.route('/Sign-up')
def login():
    return "<p>Sign Up</p>"
