from flask_blog import db, bcrypt
from flask_login import current_user
from flask import render_template, Blueprint, redirect, url_for, flash

from flask_blog.models import User
from flask_blog.users.forms import RegistrationForm

users = Blueprint('users', __name__)

@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hash = bcrypt.generate_hash_password(form.password.data).decode('utf-8')

        user = User(username=form.username.data, email=form.email.data, password=hash)

        db.session.add(user)
        db.session.commit()

        flash('Ваша учетная запись успешно создана! Теперь вы можете войти в систему', 'success')

        return redirect(url_for('users.login'))

    return render_template('register.html', title='Register', form=form)
