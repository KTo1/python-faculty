from flask import render_template, Blueprint, request, flash, redirect, url_for
from flask_blog import db
from flask_login import login_required, current_user
from flask_blog.models import Post
from flask_blog.posts.forms import PostForm

posts = Blueprint('posts', __name__)


@posts.route('/allposts')
@login_required
def all_posts():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('all_posts.html', posts=posts)


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data,
                    author=current_user)

        db.session.add(post)
        db.session.commit()

        flash('Ваш пост создан!', 'success')

        return redirect(url_for('posts.all_posts'))

    return render_template('create_post.html',
                           title='Новый пост', form=form, legend='Новый пост')


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)
