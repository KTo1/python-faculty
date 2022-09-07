from flask import render_template, Blueprint, request
from flask_login import login_required
from flask_blog.models import Post


posts = Blueprint('posts', __name__)


@posts.route('/allpost')
@login_required
def allpost():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('allpost.html', posts=posts)

