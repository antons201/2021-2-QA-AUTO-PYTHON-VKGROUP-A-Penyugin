import pytest
import os


@pytest.fixture(scope='function')
def file_path(repo_root):
    yield os.path.join(repo_root, "files", "access.log")


@pytest.fixture(scope='function')
def logs_file(file_path):
    logs = open(file_path, 'r')
    yield logs
    logs.close()