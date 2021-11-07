import pytest
import os


@pytest.fixture(scope='session')
def file_path(repo_root):
    return os.path.join(repo_root, "files", "test_company_image.jpg")
