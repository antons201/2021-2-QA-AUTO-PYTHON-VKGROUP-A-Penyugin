import os
import shutil
import sys


def create_path(dir_name):
    if sys.platform.startswith('win'):
        return 'C:\\' + dir_name
    else:
        return '/tmp/' + dir_name


def create_dir(dir_name):
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)

    os.makedirs(dir_name)
