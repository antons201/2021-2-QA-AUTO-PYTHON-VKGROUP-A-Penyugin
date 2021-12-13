import pytest


@pytest.fixture(scope='function')
def logs_file(config):
    logs = open(config['logs_file_path'], 'r')
    yield logs
    logs.close()
