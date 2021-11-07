from api.fixtures import *
from api.client import ApiClient

@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))

@pytest.fixture(scope='function')
def api_client():
    return ApiClient()