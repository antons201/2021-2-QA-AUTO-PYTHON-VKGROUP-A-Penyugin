import os
import shutil
import sys


def create_dir(dir_name):
    if sys.platform.startswith('win'):
        new_dir = 'C:\\' + dir_name
    else:
        new_dir = '/tmp/' + dir_name

    if os.path.exists(new_dir):
        shutil.rmtree(new_dir)

    os.makedirs(new_dir)

    return new_dir
