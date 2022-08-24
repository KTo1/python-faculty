from flask_blog import db, bcrypt
from flask_login import current_user, login_user, logout_user
from flask import render_template, Blueprint, redirect, url_for, flash

from flask_blog.models import User
from flask_blog.users.forms import RegistrationForm, LoginForm

users = Blueprint('users', __name__)

@users.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, form.remember.data)

            return redirect(url_for('main.home'))
        else:
            flash('Войти не удалось. Пожалуйста, проверьте электронную почту и пароль', 'внимание')

    return render_template('login.html', title='Login', form=form)


@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        user = User(username=form.username.data, email=form.email.data, password=hash)

        db.session.add(user)
        db.session.commit()

        flash('Ваша учетная запись успешно создана! Теперь вы можете войти в систему', 'success')

        return redirect(url_for('users.login'))

    return render_template('register.html', title='Register', form=form)
