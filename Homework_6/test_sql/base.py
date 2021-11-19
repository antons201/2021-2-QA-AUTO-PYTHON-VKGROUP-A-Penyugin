import collections
import re

import pytest

from models.model import CountRequests, CountRequestsByType, TopPopularRequests, Top5RequestsWithClientError, \
    Top5ClientsWithServerError
from mysql_orm.client import MysqlORMClient


class MysqlBase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_orm_client):
        self.mysql: MysqlORMClient = mysql_orm_client

    def create_count_requests(self, logs_file):
        count_requests = CountRequests(
            count=sum(1 for _ in logs_file)
        )

        self.mysql.session.add(count_requests)
        self.mysql.session.commit()

        return [count_requests]

    def create_count_requests_by_type(self, logs_file):
        request_types = collections.Counter()
        count_requests_by_type_list = []

        for line in logs_file:
            request_types[line.split(" ")[5].split("\"")[1]] += 1

        for request_type in request_types:
            count_requests_by_type = CountRequestsByType(
                type=request_type,
                count=request_types[request_type]
            )
            self.mysql.session.add(count_requests_by_type)
            count_requests_by_type_list.append(count_requests_by_type)
        self.mysql.session.commit()

        return count_requests_by_type_list

    def create_top_popular_requests(self, logs_file):
        request_urls = collections.Counter()
        top_popular_requests_list = []

        for line in logs_file:
            request_urls[line.split(" ")[6]] += 1

        for request_url in request_urls.most_common(10):
            top_popular_requests = TopPopularRequests(
                url=request_url[0],
                count=request_url[1]
            )
            self.mysql.session.add(top_popular_requests)
            top_popular_requests_list.append(top_popular_requests)
        self.mysql.session.commit()

        return top_popular_requests_list

    def create_top_5_requests_with_client_error(self, logs_file):
        requests_info = []
        top_5_requests_with_client_error_list = []

        for line in logs_file:
            if line.split(" ")[9] != "-" and re.match('4[0-9][0-9]', line.split(" ")[8]) is not None:
                requests_info.append(
                    [line.split(" ")[0], line.split(" ")[6], int(line.split(" ")[8]), int(line.split(" ")[9])])
        requests_info.sort(key=lambda x: x[3], reverse=True)

        for i in range(5):
            top_5_requests_with_client_error = Top5RequestsWithClientError(
                url=requests_info[i][1],
                status=requests_info[i][2],
                size=requests_info[i][3],
                ip=requests_info[i][0]
            )
            self.mysql.session.add(top_5_requests_with_client_error)
            top_5_requests_with_client_error_list.append(top_5_requests_with_client_error)
        self.mysql.session.commit()

        return top_5_requests_with_client_error_list

    def create_top_5_clients_with_server_error(self, logs_file):
        requests_info = []
        requests_users_count = collections.Counter()
        top_5_clients_with_server_error_list = []

        for line in logs_file:
            if re.match('5[0-9][0-9]', line.split(" ")[8]) is not None:
                requests_info.append([line.split(" ")[0], int(line.split(" ")[8])])

        for request in requests_info:
            requests_users_count[request[0]] += 1

        for requests_user_count in requests_users_count.most_common(5):
            top_5_clients_with_server_error = Top5ClientsWithServerError(
                ip=requests_user_count[0],
                count=requests_user_count[1]
            )
            self.mysql.session.add(top_5_clients_with_server_error)
            top_5_clients_with_server_error_list.append(top_5_clients_with_server_error)
        self.mysql.session.commit()

        return top_5_clients_with_server_error_list
