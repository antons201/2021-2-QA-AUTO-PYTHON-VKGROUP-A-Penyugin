import sqlalchemy
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker

from models.model import Base


class MysqlORMClient:

    def __init__(self, user, password, db_name, host='127.0.0.1', port=3306):
        self.user = user
        self.password = password
        self.db_name = db_name

        self.host = host
        self.port = port

        self.engine = None
        self.connection = None
        self.session = None

    def connect(self, db_created=True):
        db = self.db_name if db_created else ''
        url = f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{db}'

        self.engine = sqlalchemy.create_engine(url, encoding='utf8')
        self.connection = self.engine.connect()

        sm = sessionmaker(bind=self.connection.engine)  # session creation wrapper
        self.session = sm()

    def recreate_db(self):
        self.connect(db_created=False)

        self.execute_query(f'DROP database if exists {self.db_name}', fetch=False)
        self.execute_query(f'CREATE database {self.db_name}', fetch=False)

        self.connection.close()

    def execute_query(self, query, fetch=True):
        res = self.connection.execute(query)
        if fetch:
            return res.fetchall()

    def create_count_requests(self):
        if not inspect(self.engine).has_table('countRequests'):
            Base.metadata.tables['countRequests'].create(self.engine)

    def create_count_requests_by_type(self):
        if not inspect(self.engine).has_table('countRequestsByType'):
            Base.metadata.tables['countRequestsByType'].create(self.engine)

    def create_top_popular_requests(self):
        if not inspect(self.engine).has_table('topPopularRequests'):
            Base.metadata.tables['topPopularRequests'].create(self.engine)

    def create_top_5_requests_with_client_error(self):
        if not inspect(self.engine).has_table('top5RequestsWithClientError'):
            Base.metadata.tables['top5RequestsWithClientError'].create(self.engine)

    def create_top_5_clients_with_server_error(self):
        if not inspect(self.engine).has_table('top5ClientsWithServerError'):
            Base.metadata.tables['top5ClientsWithServerError'].create(self.engine)
