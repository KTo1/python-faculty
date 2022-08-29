from flask_blog import db, bcrypt
from flask_login import current_user, login_user, logout_user, login_required
from flask import render_template, Blueprint, redirect, url_for, flash, request

from flask_blog.models import User
from flask_blog.users.forms import RegistrationForm, LoginForm, UpdateProfileForm
from flask_blog.users.utils import save_picture

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


@users.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    posts = []

    form = UpdateProfileForm()

    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()

        flash('Ваш аккаунт был обновлен!', 'success')

        return redirect(url_for('users.profile'))

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        page = request.args.get('page', 1, type=int)
        user = User.query.filter_by(username=form.username.data).first_or_404()
        # posts = Post.query.filter_by(author=user).order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)

    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)

    return render_template('profile.html', title='Profile',
                           image_file=image_file, form=form, posts=posts)
