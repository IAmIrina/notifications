import sqlalchemy

from src.db.postgres import Base


class Template(Base):
    __tablename__ = 'templates'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    event = sqlalchemy.Column(sqlalchemy.String, unique=True, index=True)
    instant_event = sqlalchemy.Column(sqlalchemy.BOOLEAN)
    title = sqlalchemy.Column(sqlalchemy.String)
    text = sqlalchemy.Column(sqlalchemy.Text)
