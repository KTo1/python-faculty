import os
import shutil

root_dir = os.path.join(os.getcwd(), 'my_project')

# clear and create all template folder
template_folder = '_all-templates'
template_path = os.path.join(root_dir, template_folder)

shutil.rmtree(template_path, ignore_errors=True)
os.mkdir(template_path)

for root, dirs, files in os.walk(root_dir):
    if template_folder in root:
        continue

    files_upper = [name.upper() for name in files]
    if 'base.html'.upper() in files_upper and 'index.html'.upper() in files_upper:
        os.mkdir(os.path.join(template_path, os.path.basename(root)))
        shutil.copytree(root, os.path.join(template_path, os.path.basename(root)), dirs_exist_ok=True)
