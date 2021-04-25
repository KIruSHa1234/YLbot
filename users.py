import sqlalchemy
from .db_session import SqlAlchemyBase


class Users(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    id_user = sqlalchemy.Column(sqlalchemy.Integer)
    bal = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    Done = sqlalchemy.Column(sqlalchemy.String, nullable=True, default='')
    Skip = sqlalchemy.Column(sqlalchemy.String, nullable=True, default='')
    Admin = sqlalchemy.Column(sqlalchemy.String, nullable=True, default='NO')
