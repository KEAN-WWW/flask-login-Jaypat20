from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from application.bp.authentication.forms import LoginForm
from application.database import User

authentication = Blueprint('authentication', __name__, template_folder='templates')

@authentication.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # 1) Lookup
        user = User.find_user_by_email(form.email.data)
        if not user:
            flash('User Not Found', 'danger')
            return redirect(url_for('authentication.login'))
        # 2) Password check
        if not user.check_password(form.password.data):
            flash('Password Incorrect', 'danger')
            return redirect(url_for('authentication.login'))
        # 3) Success!
        login_user(user)
        return redirect(url_for('authentication.dashboard'))
    return render_template('login.html', form=form)

@authentication.route('/dashboard')
@login_required
def dashboard():
    # your template displays {{ name }}
    return render_template('dashboard.html', name=current_user.id)

@authentication.route('/logout')
@login_required
def logout():
    logout_user()
    # After logging out, redirect to homepage
    return redirect(url_for('homepage.homepage'))

@authentication.route('/registration', methods=['POST', 'GET'])
def registration():
    pass