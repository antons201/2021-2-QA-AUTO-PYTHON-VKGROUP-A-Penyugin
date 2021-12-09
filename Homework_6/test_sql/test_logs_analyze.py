from models.model import CountRequests, CountRequestsByType, TopPopularRequests, Top5RequestsWithClientError, \
    Top5ClientsWithServerError
from test_sql.base import MysqlBase


class TestMysqlCreate(MysqlBase):

    def test_count_requests(self, logs_file):
        assert self.create_count_requests(logs_file) == self.mysql.session.query(CountRequests).all()

    def test_count_requests_by_type(self, logs_file):
        assert self.create_count_requests_by_type(logs_file) == self.mysql.session.query(CountRequestsByType).all()

    def test_top_popular_requests(self, logs_file):
        assert self.create_top_popular_requests(10, logs_file) == self.mysql.session.query(TopPopularRequests).all()

    def test_top_5_requests_with_client_error(self, logs_file):
        assert self.create_top_requests_with_client_error(5, logs_file) == \
               self.mysql.session.query(Top5RequestsWithClientError).all()

    def test_top_5_clients_with_server_error(self, logs_file):
        assert self.create_top_clients_with_server_error(5, logs_file) == \
               self.mysql.session.query(Top5ClientsWithServerError).all()
