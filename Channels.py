import sqlalchemy
from .db_session import SqlAlchemyBase


class Channel(SqlAlchemyBase):
    __tablename__ = 'channel'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    id_channel = sqlalchemy.Column(sqlalchemy.Integer, default=0)
