import os
from PIL import Image
from secrets import token_hex
from flask import current_app


def save_picture(form_picture):
    random_hex = token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (150, 150)
    image = Image.open(form_picture)
    image.thumbnail(output_size)
    image.save(picture_path)
    image.close()

    return picture_fn
