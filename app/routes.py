# -*- coding: utf-8 -*-
import hashlib
from datetime import timedelta
from app import app, db, redis
from flask import render_template, request, flash, redirect, url_for, Response
from werkzeug.urls import url_parse
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from functools import wraps


def authenticated(function):
    @wraps(function)
    def wrapper():
        if current_user.is_authenticated:
            return redirect(url_for('input'))
        return function()

    return wrapper


@app.route('/login', methods=['GET', 'POST'])
@authenticated
def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for('input'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('input')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


def user_registered(function):
    @wraps(function)
    def wrapper():
        if not User.query.first():
            return redirect(url_for('login'))
        return function()

    return wrapper


@app.route('/register', methods=['GET', 'POST'])
@user_registered
@authenticated
def register():
    # if current_user.is_authenticated:
    #     return redirect(url_for('input'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Success! Please log in!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/input', methods=['GET', 'POST'])
@login_required
def input():
    if request.method == 'POST':
        msg = request.form.get('msg')
        messages = [(key, redis.get(key)) for key in sorted(redis.scan_iter())]
        key = hashlib.sha1(str(messages).encode('utf-8')).hexdigest()
        redis.setex(key, timedelta(minutes=5), value=msg)
    return render_template('input.html', title='Input')


@app.route('/output')
@login_required
def output():
    messages = [(key, redis.get(key).decode('utf-8')) for key in redis.scan_iter()]
    return render_template('output.html', title='Output', messages=messages)


@app.route('/output/<key>/delete')
@login_required
def delete_msg(key):
    redis.delete(key)
    return Response(status=204)


@app.route('/')
def main_page():
    user = User.query.first()
    return render_template('main.html', title='Main page', user=user)
