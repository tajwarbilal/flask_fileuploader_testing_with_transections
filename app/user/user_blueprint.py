from flask import Blueprint, request, render_template, redirect, session
from app.db.models import User
from app import db
from app import create_app
import logging

LOG = logging.getLogger(__name__)

user_blueprint = Blueprint('user_blueprint', __name__)


@user_blueprint.route('/signin')
@user_blueprint.route('/signin', methods=['POST', 'GET'])
def signin():

    if 'user' in session:
        LOG.info('Sign In Route Called But system was already in Session')
        return redirect('/')
    if request.method == 'POST':
        LOG.info('Sign In Route Called And fetch the forms value from frontend')
        username = request.form.get('email')
        password = request.form.get('password')
        if username and password is not None:
            user = User.query.filter_by(email=username).first()
            if user:
                if user.password == password:
                    session['user'] = username
                    LOG.info('succesfully signin')
                    return redirect('/')

    return render_template('signin.html')


"""
    This route is for Signup to create new account
"""


@user_blueprint.route('/signup')
@user_blueprint.route('/signup', methods=['POST', 'GET'])
def signup():
    LOG.info('Sign Up Route Called But system was already in Session')
    if 'user' in session:
        return redirect('/')
    if request.method == 'POST':
        LOG.info('Sign Up Route Called Fetching record from system')
        username = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        if username and password is not None:
            entry = User(username=username, email=email, password=password)
            db.session.add(entry)
            db.session.commit()
            LOG.info('Sign Up Route Called and register user successfully')
            return redirect('/signin')

    return render_template('signup.html')


@user_blueprint.route('/logout')
def logout():
    LOG.info('Logouts Route Called But system was already in Session')
    if 'user' in session is not None:
        LOG.info('Logout route called')
        session.pop('user')
    return redirect('/signin')
