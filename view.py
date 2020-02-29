"""
Файл с маршрутами и обработчиками приложения.
"""

from flask import render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required

from app import app
from models import User, City
from forms import LoginForm

@app.route('/')
@login_required
def index():
    continents = {"Азия": None, "Америка": None, "Африка": None, "Европа": None}
    for continent in continents:
        continents[continent] = City.query.filter(City.continent == continent).all()
    return render_template('tables.html', continents=continents)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.login == form.login.data).first()

        if user is None or not user.check_password(form.password.data):
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))

    return render_template('login.html', form=form)

@app.route('/logout/')
def logout():
    logout_user()
    return render_template('logout.html')
