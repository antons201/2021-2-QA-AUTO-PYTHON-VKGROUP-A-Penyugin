import os
import sys
import time
import logging
import pytest
import requests

import settings

from logging.handlers import RotatingFileHandler
from requests.exceptions import ConnectionError

from mock import mock
from utils.level_filter import LevelFilter
from utils import dir_helper, locations, errors


def wait_ready(host, port):
    started = False
    st = time.time()
    while time.time() - st <= 5:
        try:
            requests.get(locations.BASIC_URL.format(host, port))
            started = True
            break
        except ConnectionError:
            pass

    if not started:
        raise RuntimeError(errors.HOST_DID_NOT_STARTED.format(host, port))


def mock_handler(handler_dir, file, level, filtering=False, filtering_level=logging.ERROR):
    mock_stdout = dir_helper.create_path(handler_dir)
    dir_helper.create_dir(mock_stdout)
    handler = RotatingFileHandler(os.path.join(mock_stdout, file), backupCount=1)
    handler.setLevel(level)
    if filtering:
        handler.addFilter(LevelFilter(filtering_level))

    return handler


def pytest_configure(config):
    config.client_out = dir_helper.create_path("client_out")

    if not hasattr(config, 'workerinput'):
        info_handler = mock_handler("mock_stdout", "std_out.txt", logging.INFO, True)
        error_handler = mock_handler("mock_stderr", "std_err.txt", logging.ERROR)

        logging.root.handlers = [info_handler, error_handler]

        mock.run_mock()

        wait_ready(settings.MOCK_HOST, settings.MOCK_PORT)

        dir_helper.create_dir(config.client_out)


@pytest.fixture(scope='session')
def client_logger(client_out_root):
    log_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s\n%(message)s')
    log_file = client_out_root
    log_level = logging.INFO

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    log = logging.getLogger('client')
    log.propagate = False
    log.setLevel(log_level)
    log.handlers.clear()
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()


def pytest_unconfigure(config):
    if not hasattr(config, 'workerinput'):
        requests.get(f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}/shutdown')


@pytest.fixture(scope='session')
def client_out_root(request):
    client_out_file = os.path.join(request.config.client_out, "client_out.txt")
    yield client_out_file
