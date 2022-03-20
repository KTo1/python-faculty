import os
import shutil

LEVEL_MARKER = '|--'


def create_file_or_folder(file_name):
    if '.' in file_name:
        with open(file_name, 'w') as f:
            pass
    else:
        if not os.path.isdir(file_name):
            os.mkdir(file_name)
        os.chdir(file_name)


def create_folder_tree(prev_level, file_tree):
    next_line = file_tree.readline()
    if not next_line:
        return
    cur_level = next_line.find(LEVEL_MARKER)//3
    cur_folder = next_line.replace(LEVEL_MARKER, '').replace('|', '').strip()
    if cur_level < prev_level:
        for i in range(prev_level - cur_level):
            os.chdir('..')

    create_file_or_folder(cur_folder)
    create_folder_tree(cur_level, file_tree)


print('Make project started...')
with open('config.yaml') as file_tree:
    root_folder = file_tree.readline().strip().replace(LEVEL_MARKER, '')

    # clear and create root folder
    shutil.rmtree(root_folder, ignore_errors=True)

    os.mkdir(root_folder)
    os.chdir(root_folder)

    create_folder_tree(0, file_tree)

print('Done...')
