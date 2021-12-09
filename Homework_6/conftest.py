import os
from mysql_orm.client import MysqlORMClient
from mysql_orm.fixtures import *


def pytest_addoption(parser):
    parser.addoption('--logs_file_path', default=os.path.join(os.path.abspath(os.path.join(__file__, os.path.pardir)),
                                                              "files", "access.log"))


@pytest.fixture()
def config(request):
    logs_file_path = request.config.getoption('--logs_file_path')

    return {'logs_file_path': logs_file_path}

def pytest_configure(config):
    mysql_orm_client = MysqlORMClient(user='root', password='pass', db_name='TEST_SQL')
    if not hasattr(config, 'workerinput'):
        mysql_orm_client.recreate_db()
    mysql_orm_client.connect(db_created=True)
    if not hasattr(config, 'workerinput'):
        mysql_orm_client.create_count_requests()
        mysql_orm_client.create_count_requests_by_type()
        mysql_orm_client.create_top_popular_requests()
        mysql_orm_client.create_top_5_requests_with_client_error()
        mysql_orm_client.create_top_5_clients_with_server_error()

    config.mysql_orm_client = mysql_orm_client


@pytest.fixture(scope='session')
def mysql_orm_client(request) -> MysqlORMClient:
    client = request.config.mysql_orm_client
    yield client
    client.connection.close()


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))
