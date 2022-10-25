from sqlalchemy import Column, Integer, String, Text

from src.db.postgres import Base


class Template(Base):
    __tablename__ = 'templates'
    id = Column(Integer, primary_key=True, index=True)
    event = Column(String, unique=True, index=True)
    title = Column(String)
    text = Column(Text)
