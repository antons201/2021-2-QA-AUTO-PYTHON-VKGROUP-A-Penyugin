from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class CountRequests(Base):
    __tablename__ = 'countRequests'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"countRequests(" \
               f"id='{self.id}'," \
               f"count='{self.count}'" \
               f")"

    id = Column(Integer, primary_key=True, autoincrement=True)
    count = Column(Integer, nullable=False)


class CountRequestsByType(Base):
    __tablename__ = 'countRequestsByType'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"countRequestsByType(" \
               f"id='{self.id}'," \
               f"type='{self.type}', " \
               f"count='{self.count}'" \
               f")"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(300), nullable=False)
    count = Column(Integer, nullable=False)


class TopPopularRequests(Base):
    __tablename__ = 'topPopularRequests'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"topPopularRequests(" \
               f"id='{self.id}'," \
               f"url='{self.url}', " \
               f"count='{self.count}'" \
               f")"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(100), nullable=False)
    count = Column(Integer, nullable=False)


class Top5RequestsWithClientError(Base):
    __tablename__ = 'top5RequestsWithClientError'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"top5RequestsWithClientError(" \
               f"id='{self.id}'," \
               f"url='{self.url}', " \
               f"status='{self.status}'" \
               f"size='{self.size}" \
               f"ip='{self.ip}" \
               f")"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(300), nullable=False)
    status = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False)
    ip = Column(String(20), nullable=False)


class Top5ClientsWithServerError(Base):
    __tablename__ = 'top5ClientsWithServerError'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"top5ClientsWithServerError(" \
               f"id='{self.id}'," \
               f"ip='{self.ip}', " \
               f"count='{self.count}'" \
               f")"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(100), nullable=False)
    count = Column(Integer, nullable=False)
